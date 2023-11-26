# Supporting code
import perfplot
import pandas as pd
import string

def with_translate(s):
    vowels = 'aeiouAEIOU'
    cons = ''.join(set(string.ascii_letters).difference(set(vowels)))
    trans = str.maketrans(vowels+cons, 'v'*len(vowels)+'c'*len(cons))

    return s.str.translate(trans)


def with_replace(s):
    return s.replace({"[^aeiouAEIOU]":'c', '[aeiouAEIOU]':'v'}, regex=True)


perfplot.show(
    setup=lambda n: pd.Series(np.random.choice(['foo', 'bAR', 'foobar', 'APPLE', 'ThisIsABigWord'], n)), 
    kernels=[
        lambda s: with_translate(s),
        lambda s: with_replace(s),
    ],
    labels=['Translate', 'Replace'],
    n_range=[2 ** k for k in range(19)],
    equality_check=None,  
    xlabel='len(s)'
)
