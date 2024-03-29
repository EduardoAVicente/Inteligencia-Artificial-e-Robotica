import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff
from sklearn.preprocessing import OneHotEncoder

data, meta = arff.loadarff('Base-de-dados/bank.arff')

df = pd.DataFrame(data)

encoder = OneHotEncoder()

categorical_features = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month','poutcome']
categorical_data = df[categorical_features]

encoded_data = encoder.fit_transform(categorical_data)

numeric_features = ['age', 'average', 'day', 'duration', 'campaign', 'pdays', 'previous']
numeric_data = df[numeric_features]

features = np.concatenate((encoded_data.toarray(), numeric_data), axis=1)

target = df['subscribed'].astype(str)

Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

all_feature_names = list(encoder.get_feature_names_out(categorical_features)) + numeric_features

plt.figure(figsize=(15, 10))
tree.plot_tree(Arvore, feature_names=all_feature_names, class_names=np.unique(target), filled=True, rounded=True)
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
metrics.ConfusionMatrixDisplay.from_estimator(Arvore, features, target, ax=ax, display_labels=np.unique(target), cmap=plt.cm.Blues)
plt.show()
