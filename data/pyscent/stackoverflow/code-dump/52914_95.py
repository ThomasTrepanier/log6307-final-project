from django.db.models.enums import TextChoices

class AutoEnumChoices(TextChoices):
    def _generate_next_value_(name, start, count, last_values):  # @NoSelf
        return name.lower()
    
    @property
    def choices(cls):  # @NoSelf
        empty = [(None, cls.__empty__)] if hasattr(cls, '__empty__') else []
        return empty + [(member.value, member.label) for member in cls]
