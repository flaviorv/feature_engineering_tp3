from tennis import df
import pandas as pd

columns = ['Aspecto', 'Temperatura', 'Umidade', 'Vento']
effect = pd.DataFrame()

for col in columns:
    dummies = pd.get_dummies(df[col], dtype=int, prefix=col)
    reference = dummies.columns[0]
    dummies.loc[:,:] = dummies.apply(lambda row: row -1 if row[reference] == 1 else row, axis=1)
    dummies = dummies.drop(columns=[reference])
    effect = pd.concat([dummies, effect], axis=1)

if __name__ == '__main__':
    print(effect)