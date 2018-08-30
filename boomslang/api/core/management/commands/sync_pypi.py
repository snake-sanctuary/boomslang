from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import json
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree
from core.fixtures.safety import INSECURE

import yaml
from packages.models import Package, Version, Build, LicenseChoices
from django.conf import settings
from core.utils import download_to_file_field


def get_anaconda_pkg_list():
    """Returns the list of packages pre-installed in Anaconda.

    This is quite useful to know since that's a decent preselection of packages.
    Some of them are pre-installed, some others are available on download from
    the Anaconda repo.
    """
    anaconda_preinstalled = set()
    anaconda_icebox = set()

    resp = requests.get('https://docs.anaconda.com/anaconda/packages/py3.6_linux-64.html')
    soup = BeautifulSoup(resp.content, 'html.parser')
    table = soup.find('table', class_='docutils')

    for row in table.find_all('tr')[1:]:
        title, version, _, installed = row.find_all('td')
        title = str(title.string)
        installed = bool(installed.i)
        if installed:
            anaconda_preinstalled.add(title)
        else:
            anaconda_icebox.add(title)
    return anaconda_preinstalled, anaconda_icebox


def get_pypi_pkg_list():
    """Return the complete list of packages on pypi."""
    resp = requests.get('https://pypi.python.org/simple')
    soup = BeautifulSoup(resp.content, 'html.parser')
    packages = {str(tag.string) for tag in soup.find_all('a')}

    # to_import = anaconda_pkgs.intersection(packages)
    #
    # licenses = set()
    # for pkg in to_import:
    #     resp = requests.get(f'https://pypi.python.org/pypi/{pkg}/json')
    #     pkg_json = json.loads(resp.content)
    #     if resp.status_code == 200:
    #         licenses.add((json.loads(resp.content)['info']['license']))


def check_license(license):
    """"""
    if 'GPL' in license:
        return LicenseChoices.GPL
    elif 'MIT' in license:
        return LicenseChoices.MIT
    elif 'BSD' in license:
        return LicenseChoices.MIT
    elif 'ubli' in license:
        return LicenseChoices.FREE
    return LicenseChoices.NAN


def import_version(name, releases, package):
    """"""
    version = Version.objects.create(
        name=name,
        package=package,
        latest=True,
        active=True,
    )
    for release in releases:
        if release['packagetype'] == 'sdist':
            extension = '.tar.gz'
            build_type = Build.TypeChoices.PYPI_SDIST
        else:
            extension = '.whl'
            build_type = Build.TypeChoices.PYPI_WHEEL
        build = Build.objects.create(
            version=version,
            build_type=build_type,
            build=release['python_version'],
            build_number=0,
            depends=[],
            md5=release['md5_digest'],
            sha256=release['digests']['sha256'],
            size=release['size'],
            filename=release['filename'],
        )

        url = release['url']
        filename = '{}{}'.format(release['digests']['sha256'], extension)
        path = settings.MEDIA_ROOT/'pypi_pkg'/filename
        download_to_file_field(url, build.file, path)
        build.save()


@transaction.atomic()
def import_package(pkg, pkgs_done, latest_only=True, version=None, follow_dependencies=False):
    """"""
    resp = requests.get(f'https://pypi.python.org/pypi/{pkg}/json')
    data = json.loads(resp.content)
    info = data['info']
    releases = data['releases']
    package = Package.objects.create(
        name=pkg,
        license_type=check_license(info['license']),
        author=info['author'],
        summary=info['summary'],
        description=info['description'] or '',
        docs_url=info['docs_url'] or '',
        home_page=info['home_page'] or '',
        package_url=info['package_url'] or '',
        project_url=info['project_url'] or '',
        bugtrack_url=info['bugtrack_url'] or '',
        requires_dist=info['requires_dist'] or [],
        last_serial=data['last_serial'],
        active=True,
        is_public=True,
    )
    if latest_only:
        import_version(info["version"], releases[info["version"]], package)
    pkgs_done.add(pkg)


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            '--config-file',
            action='store',
            dest='config_file',
            help='The config file to use',
        )

    def handle(self, *args, **options):
        """"""

        with open(options['config_file'], 'r') as stream:
            try:
                config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        pkgs = set(config['whitelist'])
        pkgs_done = set()

        while pkgs:
            pkg = pkgs.pop()
            import_package(pkg, pkgs_done)
