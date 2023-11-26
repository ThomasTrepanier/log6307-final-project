import re
from mediawiki import MediaWiki

#TermFind will search through a list a given term
def TermFind(term,termList):
    responce=False
    for val in termList:
        if re.match('(.*)'+term+'(.*)',val):
            responce=True
            break
    return responce

#Find if the links and backlinks lists contains a given term 
def BoundedTerm(wikiPage,term):
    aList=wikiPage.links
    bList=wikiPage.backlinks
    responce=False
    if TermFind(term,aList)==True and TermFind(term,bList)==True:
         responce=True
    return responce

container=[]
wikipedia = MediaWiki()
for val in termlist:
    cpage=wikipedia.page(val)
    if BoundedTerm(cpage,'term')==True:
        container.append('medical')
    else:
        container.append('nonmedical')
