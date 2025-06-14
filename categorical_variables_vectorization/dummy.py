from tennis import df
import pandas as pd

columns = ['Aspecto', 'Temperatura', 'Umidade', 'Vento']
dummies = pd.get_dummies(df[columns], columns=columns, dtype=int, drop_first=True)

if __name__ == '__main__':
    print(dummies)