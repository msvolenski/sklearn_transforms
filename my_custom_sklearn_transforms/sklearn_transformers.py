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
        # Realiza a cópia do dataframe 'X' de entrada
        data = X.copy()
      
        # Define condição para remover linhas
        condition = (((data['NOTA_DE'] == 0) & (data['REPROVACOES_DE'] == 0))
         | ((data['NOTA_MF'] == 0) & (data['REPROVACOES_MF'] == 0))
         | ((data['NOTA_GO'] == 0) & (data['REPROVACOES_GO'] == 0))
         | ((data['NOTA_EM'] == 0) & (data['REPROVACOES_EM'] == 0)))

        # Separa as linhas indesejadas
        rm_index = data[condition].index.values
        
        # Retorna um novo dataframe sem as linhas indesejadas        
        return data.drop(labels=rm_index, axis='index')
