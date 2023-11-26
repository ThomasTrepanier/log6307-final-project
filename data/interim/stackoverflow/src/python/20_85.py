# File1.py

import spacy
class ml:
   def __init__(self, model_path):
       self.nlp = spacy.load(model_path) # 'model'
   def get_vec(self, post):
       return self.nlp(post).vector


