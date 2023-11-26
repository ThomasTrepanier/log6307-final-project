def static(prefix, view=serve, **kwargs):
    """
    Version of the static views that DOESN'T check for the DEBUG flag since we're
    checking it elsewhere and static items are needed for e2e tests.

    NOTICE: Sometimes the Staticfiles app decides to do whatever it wants and then
    reports this view was the one that did it. If you can't print from the serve
    function, it's full of shit. Check the STATICFILES_DIRS instead.
    """
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    elif '://' in prefix:
        # No-op if not in debug mode or a non-local prefix.
        return []
    return [
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs),
    ]

urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
