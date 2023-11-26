from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_cell = False
        self.cell_index = -1

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.cell_index = -1
        if tag == 'td':
            self.in_cell = True
            self.cell_index += 1
        # print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_cell = False
        # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.in_cell and self.cell_index == 1:
            print(data.strip())

parser = MyHTMLParser()
parser.feed('''<table callspacing="0" cellpadding="0">
    <tbody><tr>
    <td>1text&nbsp;2text</td>
    <td>3text&nbsp;</td>
    </tr>
    <tr>
    <td>4text&nbsp;5text</td>
    <td>6text&nbsp;</td>
    </tr>
</tbody></table>''')
