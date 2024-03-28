import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff

data = arff.loadarff('Base-de-dados/bank.arff')
df = pd.DataFrame(data[0])
df['poutcome'] = df['poutcome'].apply(lambda x: x.decode('utf-8'))

features = df.drop('poutcome', axis=1)
target = df['poutcome']

categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'subscribed']
for column in categorical_columns:
    features[column] = pd.Categorical(features[column])
    features[column] = features[column].cat.codes

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

Arvore = DecisionTreeClassifier(criterion='entropy')
Arvore.fit(X_train, y_train)

plt.figure(figsize=(25,10))
tree.plot_tree(Arvore, feature_names=list(features.columns), class_names=['unknown','other','failure','success'], filled=True, rounded=True)
plt.show()

fig, ax = plt.subplots(figsize=(25, 10))
metrics.ConfusionMatrixDisplay.from_estimator(Arvore, X_test, y_test, display_labels=['unknown','other','failure','success'], values_format='d', ax=ax)
plt.show()