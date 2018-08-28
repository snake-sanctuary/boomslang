
from django.db.models import (
    CASCADE, DateTimeField, ForeignKey, GenericIPAddressField,
    Model,
)
from django.utils import timezone

from packages.models import Build
from users.models import User


class DownloadHistory(Model):
    """"""
    user = ForeignKey(User, on_delete=CASCADE)
    ip = GenericIPAddressField()
    build = ForeignKey(Build, on_delete=CASCADE)
    timestamp = DateTimeField(default=timezone.now)
