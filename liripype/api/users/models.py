"""As specified by the doc, we create a custom User to simplify
later updates

https://docs.djangoproject.com/en/2.0/topics/auth/customizing/
"""

import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    token = models.UUIDField(default=uuid.uuid4)
