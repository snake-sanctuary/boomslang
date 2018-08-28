
from django.conf import settings
from django.shortcuts import Http404

from django.core.files import File
from os.path import basename
import requests
from tempfile import TemporaryFile
from urllib.parse import urlsplit

from packages.models import Package


def check_pkg_download_permission(user, package):
    if package.is_public:
        return True
    else:
        return False


def check_signature_consistency(signature, file):
    """"""
    print("PLEASE IMPLEMENT ME")
    return True


def check_ecosystem_consistency(build, user):
    """Check that the current upload is allowed in terms of namespace."""
    organisation = user.organization
    pkg = build.version.package
    # check if there is another public package with the same name within the
    # organization, if not we can return early.
    try:
        package = Package.objects.filter(
            organization=organisation,
            is_public=True,
        ).get(name=pkg.name)
    except Package.DoesNotExist:
        return True
    # now if there is already package with this name, we can fail early
    # if it doesn't belong to the user to which we are uploading
    if package.user_owner != user:
        return False
    # if the same package belongs already to the current user, is it the same
    # version?
    latest_version = package.version_set.latest('id')

    return True


def check_consistency(build, signature):
    """"""
    signature_valid = check_signature(build, signature)
    ecosystem_valid = check_ecosystem()
    return


def serve_file(response, file=None, file_path=None, filename=None):
    """"""

    if not settings.DEBUG:
        file_name = filename or file.name
        response['X-Accel-Redirect'] = f'/protected/{file_name}'
        return response

    if file:
        response.content = file.read()
        return response

    try:
        with open(settings.MEDIA_ROOT/file_path) as file:
            response.content = file.read()
            #response['Content-Type'] = 'application/zip'
            response['Content-Disposition'] = f'attachment; filename=Hello.zip'
            return response
    except Exception as e:
        print(e)
        raise Http404


def download_to_file_field(url, field, name=None):
    """Snippet found here.

    https://goodcode.io/articles/django-download-url-to-file-field/
    """
    with TemporaryFile() as tf:
        r = requests.get(url, stream=True)
        for chunk in r.iter_content(chunk_size=4096):
            tf.write(chunk)

        tf.seek(0)
        name = name or basename(urlsplit(url).path)
        field.save(name, File(tf))
