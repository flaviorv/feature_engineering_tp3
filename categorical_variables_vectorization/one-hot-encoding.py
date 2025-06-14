from tennis import df
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded = encoder.fit_transform(df[['Aspecto', 'Temperatura', 'Umidade', 'Vento']])

x = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
print(x)
