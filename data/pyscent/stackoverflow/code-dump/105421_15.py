# workaround to suppress color logging in werkzeug
try:
    import click
    old_color = click.style

    def _color(text, fg=None, bg=None, bold=None, dim=None, underline=None, blink=None, reverse=None, reset=True):
        return click.unstyle(text)

    click.style = _color
except:
    pass
