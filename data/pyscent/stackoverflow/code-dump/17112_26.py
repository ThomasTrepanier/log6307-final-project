import spacy
nlp = spacy.load('en_core_web_lg')

def printInfo(doc):
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_,
            token.shape_, token.is_alpha,
       token.is_stop, token.ent_type_, token.dep_, token.head.text)

doc = nlp("Barack Obama was not born in Hawaii")
printInfo(doc)
