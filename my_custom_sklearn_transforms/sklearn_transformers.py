from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

    
class ConvertCatColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.jobs_encoder = LabelBinarizer()

    def fit(self, X, y=None):
        self.jobs_encoder.fit(X[self.columns])
        return self
    
    def transform(self, X):
        transformed = self.jobs_encoder.transform(X[self.columns])
        ohe_df = pd.DataFrame(transformed)
        X.drop(columns=self.columns, inplace=True)
        return pd.concat([X, ohe_df], axis=1)
