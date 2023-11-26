import asyncio
from html.parser import HTMLParser

class AddClassToPTagParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "p":
            attrs = dict(attrs)
            if 'class' in attrs:
                if 'foo' not in attrs['class'].split():
                    attrs['class'] += ' foo'
            else:
                attrs['class'] = 'foo'

            attrs_str = ' '.join([f'{k}="{v}"' for k, v in attrs.items()])
            self.modified_html += f"<{tag} {attrs_str}>"
        else:
            self.modified_html += self.get_starttag_text()

    def handle_endtag(self, tag):
        self.modified_html += f"</{tag}>"

    def handle_data(self, data):
        self.modified_html += data

    def handle_entityref(self, name):
        self.modified_html += f"&{name};"

    def handle_charref(self, name):
        self.modified_html += f"&#${name};"

    def feed(self, data):
        self.modified_html = ''
        super().feed(data)
        return self.modified_html

async def transform_html(async_generator):
    parser = AddClassToPTagParser()

    async for chunk in async_generator:
        yield parser.feed(chunk)

async def test():
    async def html_generator():
        chunks = [
            "<html><head><title>Test</title></head><body><p class=",
            '"bar">Hello, world!</p><p>',
            'Hello again, world!</p></body></html>'
        ]
        for chunk in chunks:
            yield chunk
            await asyncio.sleep(0.1)

    async for transformed_chunk in transform_html(html_generator()):
        print(transformed_chunk)

# Run the test coroutine
asyncio.run(test())
