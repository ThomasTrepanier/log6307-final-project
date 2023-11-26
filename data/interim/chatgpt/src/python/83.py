import html5lib

class StreamHTMLTransformer:
    def __init__(self):
        self.parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"))
        self.serializer = html5lib.serializer.HTMLSerializer(quote_attr_values=True)

    def transform(self, html):
        dom_tree = self.parser.parse(html)

        for p_element in dom_tree.getElementsByTagName('p'):
            if 'class' in p_element.attributes:
                if 'foo' not in p_element.attributes['class'].split():
                    p_element.attributes['class'] += ' foo'
            else:
                p_element.attributes['class'] = 'foo'

        return self.serializer.serialize(dom_tree, tree='dom')

if __name__ == "__main__":
    transformer = StreamHTMLTransformer()
    html_input = '<html><head><title>Test</title></head><body><p class="bar">Hello, world!</p><p>Hello again, world!</p></body></html>'
    transformed_html = transformer.transform(html_input)
    print(''.join(transformed_html))
