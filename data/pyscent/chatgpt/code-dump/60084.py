from html.parser import HTMLParser

class AddClassToPTagParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "p":
            attrs = dict(attrs)  # Convert attrs to dictionary for easier handling
            if 'class' in attrs:
                if 'foo' not in attrs['class'].split():
                    attrs['class'] += ' foo'
            else:
                attrs['class'] = 'foo'

            # Reconstruct the tag with the updated attributes
            attrs_str = ' '.join([f'{k}="{v}"' for k, v in attrs.items()])
            print(f"<{tag} {attrs_str}>", end='')
        else:
            print(self.get_starttag_text(), end='')

    def handle_endtag(self, tag):
        print(f"</{tag}>", end='')

    def handle_data(self, data):
        print(data, end='')

    def handle_entityref(self, name):
        print(f"&{name};", end='')

    def handle_charref(self, name):
        print(f"&#${name};", end='')

html = """<html>
<head>
    <title>Test</title>
</head>
<body>
    <p class="bar">Hello, world!</p>
    <p>Hello again, world!</p>
</body>
</html>"""

parser = AddClassToPTagParser()
parser.feed(html)
