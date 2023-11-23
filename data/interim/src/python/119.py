from jinja2 import nodes
from jinja2.ext import Extension

class MarkdownExtension(Extension):
    tags = set(['markdown'])

    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)

    def parse(self, parser):
        lineno = parser.stream.next().lineno

        # Look for an extra_attrs option after the tag name
        args = []
        if parser.stream.skip_if('comma'):
            args.append(parser.parse_expression())
        else:
            args.append(nodes.Const(None))

        body = parser.parse_statements(['name:endmarkdown'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_render_markdown', args), [], [], body).set_lineno(lineno)

    def _render_markdown(self, extra_attrs, caller):
        # Use extra_attrs somehow...
        return render_markdown(caller(), extra_attrs)
