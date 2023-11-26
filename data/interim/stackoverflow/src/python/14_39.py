from django.db import models
from django_enum import EnumField

class MyModel(models.Model):

    class TextEnum(models.TextChoices):

        VALUE0 = 'V0', 'Value 0'
        VALUE1 = 'V1', 'Value 1'
        VALUE2 = 'V2', 'Value 2'

    class IntEnum(models.IntegerChoices):

        ONE   = 1, 'One'
        TWO   = 2, 'Two',
        THREE = 3, 'Three'

    # this is equivalent to:
    #  CharField(max_length=2, choices=TextEnum.choices, null=True, blank=True)
    txt_enum = EnumField(TextEnum, null=True, blank=True)

    # this is equivalent to
    #  PositiveSmallIntegerField(choices=IntEnum.choices)
    int_enum = EnumField(IntEnum)
