import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff
from sklearn.preprocessing import OneHotEncoder


data,meta = arff.loadarff('bank.arff')

attributes = meta.names()
data_value = np.asarray(data)


encoder = OneHotEncoder()



age = np.asarray(data['age']).reshape(-1,1)
job = np.asarray(data['job']).reshape(-1,1)
marital = np.asarray(data['marital']).reshape(-1,1)
education = np.asarray(data['education']).reshape(-1,1)
default = np.asarray(data['default']).reshape(-1,1)
average = np.asarray(data['average']).reshape(-1,1)
housing = np.asarray(data['housing']).reshape(-1,1)
loan = np.asarray(data['loan']).reshape(-1,1)
contact = np.asarray(data['contact']).reshape(-1,1)
day = np.asarray(data['day']).reshape(-1,1)
month = np.asarray(data['month']).reshape(-1,1)
duration = np.asarray(data['duration']).reshape(-1,1)
campaign = np.asarray(data['campaign']).reshape(-1,1)
pdays = np.asarray(data['pdays']).reshape(-1,1)
previous = np.asarray(data['previous']).reshape(-1,1)
subscribed = np.asarray(data['previous']).reshape(-1,1)

job = encoder.fit_transform(job).reshape(-1,1)
marital = encoder.fit_transform(marital).reshape(-1,1)
education = encoder.fit_transform(education).reshape(-1,1)
default = encoder.fit_transform(default).reshape(-1,1)
housing = encoder.fit_transform(housing).reshape(-1,1)
loan = encoder.fit_transform(loan).reshape(-1,1)
contact = encoder.fit_transform(contact).reshape(-1,1)
month = encoder.fit_transform(month).reshape(-1,1)

features = np.concatenate((age, job, marital, education, default, average, housing, loan, contact, day, month, duration, campaign, pdays, previous, subscribed), axis=1)


# features = np.concatenate((age, job, subscribed), axis=1)
target = data['poutcome'].reshape(-1, 1)


Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

plt.figure(figsize=(10, 6.5))
tree.plot_tree(Arvore,feature_names=['age','job','subscribed'],class_names=['unknown','other','failure','success'],
                   filled=True, rounded=True)
plt.show()

fig, ax = plt.subplots(figsize=(25, 10))
metrics.ConfusionMatrixDisplay.from_estimator(Arvore,features,target,display_labels=['Aprovado', 'Reprovado'], values_format='d', ax=ax)



plt.show()






# import pandas as pd
# import numpy as np
# from sklearn import tree, metrics
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
# from scipy.io import arff

# data = arff.loadarff('bank.arff')
# df = pd.DataFrame(data[0])
# df['subscribed'] = df['subscribed'].apply(lambda x: x.decode('utf-8'))

# features = df.drop('subscribed', axis=1)
# target = df['subscribed']

# categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
# for column in categorical_columns:
#     features[column] = pd.Categorical(features[column])
#     features[column] = features[column].cat.codes

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Arvore = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)
# Arvore.fit(X_train, y_train)

# plt.figure(figsize=(25,10))
# tree.plot_tree(Arvore, feature_names=list(features.columns), class_names=['yes', 'no'], filled=True, rounded=True)
# plt.show()

# fig, ax = plt.subplots(figsize=(25, 10))
# metrics.plot_confusion_matrix(Arvore, X_test, y_test, display_labels=['yes', 'no'], values_format='d', ax=ax)
# plt.show()