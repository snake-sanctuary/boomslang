"""As specified by the doc, we create a custom User to simplify
later updates

https://docs.djangoproject.com/en/2.0/topics/auth/customizing/
"""

import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from core.structures import ChoiceEnum


class User(AbstractUser):

    class NatureChoices(ChoiceEnum):
        human = "Human"
        process = "Process"

    token = models.UUIDField(default=uuid.uuid4)
    nature = models.CharField(max_length=7, choices=NatureChoices.choices())
