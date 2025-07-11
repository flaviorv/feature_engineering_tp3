from tennis import df
import pandas as pd

features = ["Aspecto", "Temperatura", "Umidade", "Vento"]

# Count the frequency of each categorical value per feature
category_frequencies = {}
for feat in features:
    for cat in df[feat]:
        key = f"{feat}_{cat}"
        if key not in category_frequencies:
            category_frequencies[key] = 1
        else:
            category_frequencies[key] += 1

# Map frequency to each sample
frequency_encoded_df = pd.DataFrame()
for feat in features:
    frequency_encoded_df[feat] = df[feat].map(lambda cat: category_frequencies[f"{feat}_{cat}"])

print('Category Frequencies:\n', category_frequencies)
print('Frequency-Encoded Features:\n', frequency_encoded_df)