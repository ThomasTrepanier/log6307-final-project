import re
string = 'asfd @@@ fdsfd @@@ ffds @@@ asdf'
kv = {'1': 'hi', '2': 'there', '3': 'bla'}
class repl:
    def __init__(self):
        self.called=0
    def __call__(self,match):
        self.called+=1
        return kv[str(self.called)]
print(re.sub('@@@',repl(),string))
