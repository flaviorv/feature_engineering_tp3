from tennis import df
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[['Aspecto', 'Temperatura', 'Umidade', 'Vento']])
onehot = pd.DataFrame(encoded.toarray(), columns=encoder.get_feature_names_out())

if __name__ == '__main__':
    print(onehot)