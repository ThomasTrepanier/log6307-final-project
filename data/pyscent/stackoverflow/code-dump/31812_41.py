from collections import UserDict

class FormData(UserDict):
    def __init__(self, *args, **kwargs):
        self.frozen = False
        super().__init__(*args, **kwargs)
        self.frozen = True
        
    def __setitem__(self, key, value):
        if self.frozen and key not in self:
            raise ValueError('Key %s is not in the dict. Available: %s' % (
                key, self.keys()
            ))
        super().__setitem__(key, value)

def parse_form(content):
    """
    Parse the first form in the html in content.
    """
    
    import lxml.html
    tree = lxml.html.fromstring(content)
    return FormData(tree.forms[0].fields)
