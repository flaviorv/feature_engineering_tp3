from tennis import df
from sklearn.feature_extraction import FeatureHasher
import pandas as pd
from one_hot import onehot

x = df[["Aspecto", "Temperatura", "Umidade", "Vento"]].to_dict(orient="records")
hasher = FeatureHasher(n_features=8, input_type='dict')
hashed = hasher.transform(x)
hashed_df = pd.DataFrame.sparse.from_spmatrix(hashed)

print(hashed_df)
print('Hashing Trick shape:', hashed_df.shape)
print('One Hot shape:', onehot.shape)