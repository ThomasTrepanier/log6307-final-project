def render_template(template):
    """decorator to render a template with a context"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            # access request object
            request = kwargs.get('request')

            context = func(*args, **kwargs)
            if context is None:
                context = {}
            return templates.TemplateResponse(template, {**context, 'request': request})
        return wrapper
    return decorator
