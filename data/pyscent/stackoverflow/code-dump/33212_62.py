from bs4 import BeautifulSoup

def selected_option(select):
    option = select.find("option", selected=True)
    if option: 
        return option['value']

# tag name => how to extract its value
tags = {  
    "input": lambda t: t['value'],
    "textarea": lambda t: t.text,
    "select": selected_option
}


def parse_form(html):
    soup = BeautifulSoup(html, 'html.parser')
    form = soup.find("form")
    return {
        e['name']: tags[e.name](e)
        for e in form.find_all(tags.keys())
    }
