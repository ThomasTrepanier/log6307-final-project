from jinja2 import nodes
from jinja2.ext import Extension

class MarkdownExtension(Extension):
    tags = set(['markdown'])

    def __init__(self, environment):
        super(MarkdownExtension, self).__init__(environment)

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        body = parser.parse_statements(['name:endmarkdown'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_render_markdown', []), [], [], body).set_lineno(lineno)

    def _render_markdown(self, caller):
        return render_markdown(caller())
