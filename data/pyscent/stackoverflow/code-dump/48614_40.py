from enum_properties import s
from django_enum import TextChoices  # use instead of Django's TextChoices
from django.db import models

class TextChoicesExample(models.Model):

    class Color(TextChoices, s('rgb'), s('hex', case_fold=True)):

        # name   value   label       rgb       hex
        RED     = 'R',   'Red',   (1, 0, 0), 'ff0000'
        GREEN   = 'G',   'Green', (0, 1, 0), '00ff00'
        BLUE    = 'B',   'Blue',  (0, 0, 1), '0000ff'

        # any named s() values in the Enum's inheritance become properties on
        # each value, and the enumeration value may be instantiated from the
        # property's value

    color = EnumField(Color)

instance = TextChoicesExample.objects.create(
    color=TextChoicesExample.Color('FF0000')
)
assert instance.color == TextChoicesExample.Color('Red')
assert instance.color == TextChoicesExample.Color('R')
assert instance.color == TextChoicesExample.Color((1, 0, 0))

# direct comparison to any symmetric value also works
assert instance.color == 'Red'
assert instance.color == 'R'
assert instance.color == (1, 0, 0)

# save by any symmetric value
instance.color = 'FF0000'

# access any enum property right from the model field
assert instance.color.hex == 'ff0000'

# this also works!
assert instance.color == 'ff0000'

# and so does this!
assert instance.color == 'FF0000'

instance.save()

# filtering works by any symmetric value or enum type instance
assert TextChoicesExample.objects.filter(
    color=TextChoicesExample.Color.RED
).first() == instance

assert TextChoicesExample.objects.filter(color=(1, 0, 0)).first() == instance

assert TextChoicesExample.objects.filter(color='FF0000').first() == instance
