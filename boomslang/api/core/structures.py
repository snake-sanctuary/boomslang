from enum import Enum, unique

UniqueEnum = unique(Enum)


class ChoiceEnum(UniqueEnum):
    """"""
    @classmethod
    def choices(cls):
        return [(member.name, member.value) for member in cls]
