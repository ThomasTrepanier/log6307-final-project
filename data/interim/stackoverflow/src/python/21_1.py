from nltk.corpus import stopwords
from nltk import PorterStemmer
from nltk import LancasterStemmer

def performStemAndLemma(textcontent):
    pattern =r'\w+'
    tokenizewords=nltk.regexp_tokenize(textcontent,pattern)
    tokenizewords = [w.lower() for w in set(tokenizewords)]
    stopper = stopwords.words("english")
    filteredwords = [w for w in tokenizewords if w not in stopper]
    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()
    porterstemmedwords = [porter.stem(w) for w in filteredwords]
    lancasterstemmedwords = [lancaster.stem(w) for w in filteredwords]
    wnl = nltk.WordNetLemmatizer()
    lemmatizedwords = [wnl.lemmatize(word) for word in filteredwords]
    return porterstemmedwords, lancasterstemmedwords, lemmatizedwords
