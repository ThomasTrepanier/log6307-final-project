from pymystem3 import Mystem
mystem = Mystem()
    
def preprocess_text(text):
   ...
   tokens = mystem.lemmatize(text)
   ...
   text = " ".join(tokens)
   return text

data_set = Parallel(n_jobs=-1)(delayed(preprocess_text)(article) for article in tqdm(articles))
