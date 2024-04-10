from  sklearn.datasets  import  load_iris
from  sklearn.neural_network  import  MLPClassifier
from  sklearn.metrics  import plot_confusion_matrix
import  matplotlib.pyplot  as  plt

data = load_iris()
features =data.data
target = data.target

plt.figure(figsize=(16,8))
plt.subplot(2,2,1)
plt.scatter(features[:,0], features[:,1], c=target,marker='o',cmap='viridis')


# Classificador = MLPClassifier(hidden_layer_sizes = (400), alpha=2, max_iter=600)

Classificador = MLPClassifier(hidden_layer_sizes = (5), alpha=30 max_iter=100)
Classificador.fit(features,target)
predicao = Classificador.predict(features)

plt.subplot(2,2,3)
plt.scatter(features[:,0], features[:,1], c=predicao,marker='d',cmap='viridis',s=150)
plt.scatter(features[:,0], features[:,1], c=target,marker='o',cmap='viridis',s=15)

plot_confusion_matrix(Classificador, features, target,include_values=True,display_labels=data.target_names)
plt.show()