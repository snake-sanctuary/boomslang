
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db.models import (
    BooleanField, CASCADE, CharField, DateTimeField, FileField,
    ForeignKey, Model,
    PositiveIntegerField, PositiveSmallIntegerField, SET_NULL,
    TextField, URLField,
)
from django.urls import reverse
from django.utils import timezone
from core.structures import ChoiceEnum

from teams.models import Team
from users.models import User


class LicenseChoices(ChoiceEnum):
    """"""
    MIT = "MIT"
    GPL = "GPL"
    BSD = "BSD"
    ALV = "Apache v2"
    PUBL = "Public"
    FREE = "Other free"
    PROPR = "Proprietary"
    NAN = "Undefined"


class Package(Model):
    """A Package."""

    class QualityCheckChoices(ChoiceEnum):
        """"""
        OFF = "off"
        QA_1 = "QA level 1"
        QA_2 = "QA level 2"
        PROD = "production"

    class VisibilityChoices(ChoiceEnum):
        """"""
        PRIVATE = "private"
        TEAM = "team"
        PUBLIC = "public"

    name = CharField(max_length=100)

    # PYPI DATA
    license_type = CharField(max_length=20, choices=LicenseChoices.choices())
    author = CharField(max_length=100, blank=True)
    summary = TextField(blank=True)
    description = TextField(blank=True)
    docs_url = URLField(blank=True)
    home_page = URLField(blank=True)
    package_url = URLField(blank=True)
    project_url = URLField(blank=True)
    bugtrack_url = URLField(blank=True)
    requires_dist = ArrayField(CharField(max_length=100))
    last_serial = PositiveIntegerField()

    # ACCESS DATA
    team_owner = ForeignKey(Team, null=True, on_delete=SET_NULL)
    user_owner = ForeignKey(User, null=True, on_delete=SET_NULL)
    active = BooleanField(default=False)
    is_public = BooleanField(default=False)
    quality_check = CharField(
        max_length=4, choices=QualityCheckChoices.choices(),
    )
    visibility = CharField(
        max_length=7, choices=VisibilityChoices.choices(),
    )


class Version(Model):
    """Version of a package"""
    package = ForeignKey(Package, on_delete=CASCADE)
    name = CharField(max_length=20)
    latest = BooleanField(default=False)
    active = BooleanField(default=False)


class Build(Model):
    """"""

    class TypeChoices(ChoiceEnum):
        """"""
        PYPI_SDIST = "sdist"
        PYPI_WHEEL = "bdist_wheel"
        CONDA_LINUX64 = "linux-64"
        CONDA_WIN64 = "win-64"
        CONDA_NOARCH = "noarch"

    version = ForeignKey(Version, on_delete=CASCADE)
    build_type = CharField(max_length=20, choices=TypeChoices.choices())
    build = CharField(max_length=20)
    build_number = PositiveSmallIntegerField(default=int)
    depends = ArrayField(CharField(max_length=100))
    md5 = CharField(max_length=32)
    sha256 = CharField(max_length=64)
    size = PositiveIntegerField(default=int)
    timestamp = DateTimeField(default=timezone.now)
    file = FileField(null=True, blank=True)
    filename = CharField(max_length=120)

    def get_download_url(self, user):
        protocol = settings.PROTOCOL
        basic_auth = f'{user.username}:{user.token}'
        domain = settings.DOMAIN_NAME
        path = reverse(
            'download-build', kwargs={'pk': self.id, 'filename': self.filename}
        )
        return(f'{protocol}://{basic_auth}@{domain}{path}')
