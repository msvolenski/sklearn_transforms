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

# All sklearn Transforms must have the `transform` and `fit` methods
class DropRows(BaseEstimator, TransformerMixin):
    def __init__(self, condition_to_drop):
        self.condition = condition_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        
        # Separamos as linhas indesejadas
        rm_index = data[self.condition].index.values
        
        # Retornamos um novo dataframe sem as linhas indesejadas        
        return data.drop(labels=rm_index, axis='index')
