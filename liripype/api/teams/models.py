from django.db.models import (
    CASCADE, CharField, ForeignKey, ManyToManyField, Model, OneToOneField,
)
from users.models import User
from core.structures import ChoiceEnum


class Team(Model):
    """"""
    name = CharField(max_length=100)
    process = OneToOneField(User, on_delete=CASCADE, related_name="process")
    users = ManyToManyField(User, through='TeamUserRelation')


class TeamUserRelation(Model):
    """"""
    
    class PermissionChoices(ChoiceEnum):
        """"""
        READ = "Read"
        WRITE = "Read/Write"
        ADMIN = "Admin"

    user = ForeignKey(User, on_delete=CASCADE)
    team = ForeignKey(Team, on_delete=CASCADE)
    permission = CharField(max_length=5, choices=PermissionChoices.choices())
