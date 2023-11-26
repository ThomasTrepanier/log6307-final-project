from bs4 import BeautifulSoup


def parse_form(content):
    data = {}
    html = BeautifulSoup(content, features="lxml")
    form = html.find('form', recursive=True)
    fields = form.find_all(('input', 'select', 'textarea'))
    for field in fields:
        name = field.get('name')
        if name:
            if field.name == 'input':
                value = field.get('value')
            elif field.name == 'select':
                try:
                    value = field.find_all('option', selected=True)[0].get('value')
                except:
                    value = None
            elif field.name == 'textarea':
                value = field.text
            else:
                # checkbox ? radiobutton ? file ? 
                continue
            data[name] = value
    return data
