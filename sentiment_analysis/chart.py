import matplotlib.pyplot as plt
import json

x_pos, y_pos = None, None
with open('40_positive.json', 'r') as f:
    content = json.load(f)
    x_pos = content['x']
    y_pos = content['y']

x_neg, y_neg = None, None
with open('40_negative.json', 'r') as f:
    content = json.load(f)
    x_neg = content['x']
    y_neg = content['y']

y = y_neg+y_pos
x = x_neg+x_pos

colors = ['green' if coef > 0 else 'red' for coef in y]
plt.figure(figsize=(16, 6))
plt.bar(x_neg+x_pos, y_neg+y_pos, color=colors)
plt.xticks(rotation=45, ha='right')
plt.title('negative/positive review')
plt.xlabel('token')
plt.ylabel('coeficient')
plt.tight_layout()
plt.savefig('coefs.png')