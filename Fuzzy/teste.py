import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

grafico = int(input("Inseira o tipo de grafico que deseja: \n1 - Triangulo\n2 - Trapezio\n3 - Gaussiana\n4 - Automatico \nTipo de grafico: "))

# Variaveis antecedentes
altura = ctrl.Antecedent(np.arange(0, 300, 1), 'altura')
peso = ctrl.Antecedent(np.arange(0, 200, 1), 'peso')
sedentarismo = ctrl.Antecedent(np.arange(0, 11, 1), 'sedentarismo')
alimentacao = ctrl.Antecedent(np.arange(0, 11, 1), 'alimentacao')

#Variaveis conseguente
obesidade = ctrl.Consequent(np.arange(0, 100, 1), 'obesidade')

def automatico():
    # automf -> Atribuição de categorias automaticamente
    altura.automf(names=['baixo','medio','alto'],)
    peso.automf(names=['baixo','medio','alto'])
    sedentarismo.automf(names=['baixo','medio','alto'])
    alimentacao.automf(names=['baixo','medio','alto'])

def triangulo():
    # Funções Triangulo
    altura['baixo'] = fuzz.trimf(altura.universe, [0, 50, 100])
    altura['medio'] = fuzz.trimf(altura.universe, [50, 100, 150])
    altura['alto'] = fuzz.trimf(altura.universe, [100, 150, 300])

    peso['baixo'] = fuzz.trimf(peso.universe, [0, 80, 100])
    peso['medio'] = fuzz.trimf(peso.universe, [80, 100, 140])
    peso['alto'] = fuzz.trimf(peso.universe, [100, 140, 200])

    sedentarismo['baixo'] = fuzz.trimf(sedentarismo.universe, [0, 2, 4])
    sedentarismo['medio'] = fuzz.trimf(sedentarismo.universe, [2, 4, 7])
    sedentarismo['alto'] = fuzz.trimf(sedentarismo.universe, [4, 7, 10])

    
