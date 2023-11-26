import re
from nltk.corpus import stopwords 
def performStemAndLemma(textcontent):
    # Write your code here
    lancaster = nltk.LancasterStemmer()
    porter = nltk.PorterStemmer()
    wnl = nltk.WordNetLemmatizer()
    tokens2_3 = nltk.regexp_tokenize(textcontent,  r'\w+')
    stop_words = set(stopwords.words('english'))
    tokenisedwords=[words for words in set(tokens2_3) if not words.lower() in  stop_words ]
    #print(tokenizedwords)
    return [porter.stem(word.lower()) for word in set(tokenisedwords)],[lancaster.stem(word.lower()) for word in set(tokenisedwords)],[wnl.lemmatize(word.lower()) for word in set(tokenisedwords)]
