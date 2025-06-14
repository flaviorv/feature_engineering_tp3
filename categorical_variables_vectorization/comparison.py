from dummy import dummies
from effect_coding import effect
from one_hot import onehot
from sklearn.linear_model import LogisticRegression
from tennis import df

def train(x, y):
    model = LogisticRegression()
    model.fit(x, y)
    return model, x.columns

target = df['Jogar_Tenis']
model_onehot, col_onehot = train(onehot, target)
model_dummies, col_dummies = train(dummies, target)
model_effect, col_effect = train(effect, target)

def print_coef(model, columns, name):
    print('\n', name, 'coeficients')
    print(f'Intercept: {model.intercept_[0]:.2f}')
    for col, coef in zip(columns, model.coef_[0]):
        print(f'{col}: {coef:.2f}')

print(model_effect.coef_)
#onehot uses the 0 as reference for the deviation
print_coef(model_onehot, col_onehot, 'One Hot')
#dummies uses the droped feature (reference var)
print_coef(model_dummies, col_dummies, 'Dummies')
#effect uses the mean of the target as reference
print_coef(model_effect, col_effect, 'Effect')