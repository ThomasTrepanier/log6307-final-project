def add_translatable_field_to_model(model, field_name, field):
    """
    This is functionally identical, except usage syntax.

    Example usage:

        # models.py
        class Acme(models.Model):
            code = models.CharField()

        add_translatable_field_to_model(Acme, "name", models.CharField(blank=True, verbose_name=_("common name")))
        add_translatable_field_to_model(Acme, "description", models.TextField())
    """
    for code, name in settings.LANGUAGES:
        field.clone().contribute_to_class(model, f"{field_name}_{code}")

    def local_translation_getter(self):
        language_code = get_language_code()
        return getattr(self, f"{field_name}_{language_code}", "")

    setattr(model, field_name, property(local_translation_getter))
