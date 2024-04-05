import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

print('Carregando Arquivo de teste')
arquivo = np.load('teste2.npy')
x = arquivo[0]
y = np.ravel(arquivo[1])

# Matrizes para armazenar média e desvio padrão em cada ciclo de execução
mean_losses = []
std_losses = []

# 10 10 1000

# 10 1 1000 

# 10 10 300000

for i in range(10):
    regr = MLPRegressor(hidden_layer_sizes=(10,1),  # primeiro neurônio depois camada
                        max_iter=1000,  # Reduzindo o número de iterações
                        activation='relu',  # {'identity', 'logistic', 'tanh', 'relu'},
                        solver='adam',
                        learning_rate='adaptive',
                        n_iter_no_change=50)
    print('Treinando RNA')
    regr = regr.fit(x, y)
    y_est = regr.predict(x)
    loss_values = regr.loss_curve_  # Curva de perda para este ciclo de execução

    plt.figure(figsize=[14, 7])

    # plot curso original
    plt.subplot(1, 3, 1)
    plt.plot(x, y)

    # plot aprendizagem
    plt.subplot(1, 3, 2)
    plt.plot(loss_values)

    # plot regressor
    plt.subplot(1, 3, 3)
    plt.plot(x, y, linewidth=1, color='yellow')
    plt.plot(x, y_est, linewidth=2)

    plt.show()

    # Calcula a média e o desvio padrão da curva de perda para este ciclo
    mean_loss = np.mean(loss_values)
    std_loss = np.std(loss_values)

    mean_losses.append(mean_loss)
    std_losses.append(std_loss)

    print("Media: %.2f" %mean_loss)
    print("Desvio padrão do erro final: %.2f" % std_loss)

# # Calcula a média e o desvio padrão dos valores finais da curva de perda
# mean_loss_overall = np.mean(mean_losses)
# std_loss_overall = np.mean(std_losses)

# print("\nMédia dos valores finais da média da curva de perda: %.2f" % mean_loss_overall)
# print("Média dos valores finais do desvio padrão da curva de perda: %.2f" % std_loss_overall)
