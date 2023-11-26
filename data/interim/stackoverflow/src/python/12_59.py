def preprocess_text(text):
   ...
   mystem = Mystem()
   tokens = mystem.lemmatize(text)
   ...
   text = " ".join(tokens)
   return text
