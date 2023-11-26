def get_language_code():
    """
    Gets the two letter code of the currently selected language, or the default 
   language if none specified, set by Django LocaleMiddleware.
    """
    language = translation.get_language()
    if language is None:
        return settings.DEFAULT_LANGUAGE
    available_language_codes = set(code for code, _ in settings.LANGUAGES)
    if language not in available_language_codes and "-" in language:
        language = language.split("-")[0]
    if language in available_language_codes:
        return language
    return settings.DEFAULT_LANGUAGE
