import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder

class CategoricalOneHot(BaseEstimator, TransformerMixin):
    def __init__(self, list_key_words=None):
        self.oh_dict = {}
        self.list_key_words = list_key_words

    def fit(self, X, y=None):
        self.list_cat_col = []
        for key_word in self.list_key_words:
            self.list_cat_col += [col for col in X.columns if key_word in col]
        for col in self.list_cat_col:
            oh = OneHotEncoder(handle_unknown="ignore", sparse=False)
            oh.fit(X[[col]])
            names = oh.get_feature_names_out()
            self.oh_dict[col] = (oh, names)
        return self

    def transform(self, X):
        _X = X.copy()
        for col in self.list_cat_col:
            oh = self.oh_dict[col][0]
            df_oh = pd.DataFrame(
                data=oh.transform(_X[[col]]),
                columns=self.oh_dict[col][1],
                index=_X.index)
            _X = pd.concat([_X, df_oh], axis=1)
            _X.drop(col, axis=1, inplace=True)
        return _X

if __name__ == "__main__":
    tex = pd.DataFrame({'city': ['a', 'a', 'e', 'b'], 'state': ['f', 'c', 'd', 'd']})
    coh = CategoricalOneHot(list_key_words=['city', 'state'])
    print(coh.fit_transform(tex))
