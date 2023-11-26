s = '''
def translate_():
    symbols = '`,~,!,@,#,$,%,^,&,*,(,),_,-,+,=,{,[,],},|,\,:,;,",<,,,>,.,?,/'
    s = '~this@is!a^test @'
    t = str.maketrans(dict.fromkeys(symbols, ' '))
    s.translate(t)
    return s

def replace_():
    symbols = '`,~,!,@,#,$,%,^,&,*,(,),_,-,+,=,{,[,],},|,\,:,;,",<,,,>,.,?,/'
    s = '~this@is!a^test @'
    for symbol in symbols:
        s = s.replace(symbol, ' ')
    return s
'''

print(timeit.timeit('replace_()', setup=s, number=100000))
print(timeit.timeit('translate_()', setup=s, number=100000))
