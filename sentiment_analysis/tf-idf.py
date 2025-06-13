from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from bs4 import BeautifulSoup
import numpy as np
import json

train_data = load_files('aclImdb/train', categories=['pos', 'neg'], encoding='utf-8')
test_data = load_files('aclImdb/test', categories=['pos', 'neg'], encoding='utf-8')

x_train = [BeautifulSoup(rev, 'html.parser').get_text() for rev in train_data.data]

tfidf = TfidfVectorizer(stop_words='english', token_pattern=r'\b\w{3,}\b', min_df=5, max_df=0.9)
x_train = tfidf.fit_transform(train_data.data)
y_train = train_data.target

x_test = tfidf.transform(test_data.data)
y_test = test_data.target

_max = np.asarray(x_train.mean(axis=0)).flatten()
feature_names = tfidf.get_feature_names_out()
_sorted = _max.argsort()

highest = feature_names[_sorted[-20:]]
lowest = feature_names[_sorted[:20]]

print('highest values:', highest)
print('lowest values:', lowest)

model = LogisticRegression()
model.fit(x_train, y_train)

predicted_train = model.predict(x_train)
predicted_test = model.predict(x_test)

print('\nTrain data:')
print(classification_report(y_train, predicted_train))

print('Test data:')
print(classification_report(y_test, predicted_test))

coefs = model.coef_[0]

top_positive_idx = np.argsort(coefs)[-40:]
top_negative_idx = np.argsort(coefs)[:40]

top_positive = feature_names[top_positive_idx]
top_negative = feature_names[top_negative_idx]

file = open('40_positive.json', 'w')
content = {'x': top_positive.tolist(), 'y': coefs[top_positive_idx].tolist()}
file.write(json.dumps(content, indent=2))
file.close()

file = open('40_negative.json', 'w')
content = {'x': top_negative.tolist(), 'y': coefs[top_negative_idx].tolist()}
file.write(json.dumps(content, indent=2))
file.close()
