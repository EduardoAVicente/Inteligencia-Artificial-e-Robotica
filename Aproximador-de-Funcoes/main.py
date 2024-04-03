import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

print('Carregando Arquivo de teste')
arquivo = np.load('teste2.npy')
x = arquivo[0]
y = np.ravel(arquivo[1])
media_exec = [] 
desvio_padrao_exec = [] 


loss_values = []  # Lista para armazenar os valores da curva de perda

for i in range(10):
    regr = MLPRegressor(hidden_layer_sizes=(10, 10),  # primeiro neuronioc depois camada
                        max_iter=1000,
                        activation='relu',  # {'identity', 'logistic', 'tanh', 'relu'},
                        solver='adam',
                        learning_rate='adaptive',
                        n_iter_no_change=50)
    print('Treinando RNA')
    regr = regr.fit(x, y)

    print('Preditor')
    y_est = regr.predict(x)

    # Adiciona os valores da curva de perda à lista
    loss_values.append(regr.loss_curve_)

    plt.figure(figsize=[14, 7])

    # plot curso original
    plt.subplot(1, 3, 1)
    plt.plot(x, y)

    # plot aprendizagem
    plt.subplot(1, 3, 2)
    plt.plot(regr.loss_curve_)

    # plot regressor
    plt.subplot(1, 3, 3)
    plt.plot(x, y, linewidth=1, color='yellow')
    plt.plot(x, y_est, linewidth=2)

    plt.show()

    media.add(np.mean(regr.loss_curves))
desvio_padrao = np.std(loss_curves_3)
