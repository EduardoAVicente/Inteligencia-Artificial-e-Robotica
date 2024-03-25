import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
calorias = ctrl.Antecedent(np.arange(0, 9, 1), 'calorias')
TAtividade = ctrl.Antecedent(np.arange(0,11, 1), 'TAtividade')
#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 11, 1), 'peso')


calorias['pouco'] = fuzz.trapmf(calorias.universe, [-1,0,2,4])
calorias['razoavel'] = fuzz.trapmf(calorias.universe,[ 2,4,6,8])
calorias['bastante'] = fuzz.trapmf(calorias.universe, [4,6,8,9])

TAtividade['pouco'] = fuzz.gaussmf(TAtividade.universe, 0,1)
TAtividade['razoavel'] = fuzz.gaussmf(TAtividade.universe,5,2)
TAtividade['bastante'] = fuzz.gaussmf(TAtividade.universe, 10,2)
'''
#triangulo
TAtividade['pouco'] = fuzz.trimf(TAtividade.universe, 1, 4,6)
TAtividade['razoavel'] = fuzz.trimf(TAtividade.universe, 4, 7, 10)
TAtividade['bastante'] = fuzz.trimf(TAtividade.universe, 8, 10,11)
'''
'''
#trapesio
TAtividade['pouco'] = fuzz.trapmf(TAtividade.universe, 1,3,4,6)
TAtividade['razoavel'] = fuzz.trapmf(TAtividade.universe, 4, 6, 8, 10)
TAtividade['bastante'] = fuzz.trapmf(TAtividade.universe, 8, 9, 10,11)
'''

peso['peso pena'] = fuzz.gaussmf(peso.universe, 0,2)
peso['peso medio'] = fuzz.gaussmf(peso.universe, 7, 2)
peso['peso pesado'] = fuzz.gaussmf(peso.universe, 10,1)

'''
#triangulo
peso['peso pena'] = fuzz.trimf(peso.universe, [1, 4,6])
peso['peso medio'] = fuzz.trimf(peso.universe, [4, 7, 10])
peso['peso pesado'] = fuzz.trimf(peso.universe, [8, 10,11])


#trapesio
peso['peso pena'] = fuzz.trapmf(peso.universe, [1,3,4,6])
peso['peso medio'] = fuzz.trapmf(peso.universe, [4, 6, 8, 10])
peso['peso pesado'] = fuzz.trapmf(peso.universe, [8, 9, 10,11])
'''
#Visualizando as variáveis
calorias.view()
TAtividade.view()
peso.view()

#Criando as regras
regra_1 = ctrl.Rule(calorias['pouco'] & (TAtividade['pouco'] | TAtividade['razoavel']), peso['peso pena'])
regra_2 = ctrl.Rule(calorias['pouco'] & TAtividade['bastante'], peso['peso medio'])
regra_3 = ctrl.Rule(calorias['razoavel'] & (TAtividade['razoavel'] | TAtividade['bastante']), peso['peso pena'])
regra_4 = ctrl.Rule(calorias['razoavel'] & TAtividade['pouco'], peso['peso medio'])
regra_5 = ctrl.Rule(calorias['bastante'] & TAtividade['pouco'], peso['peso pesado'])
regra_6 = ctrl.Rule(calorias['bastante'] & (TAtividade['razoavel']| TAtividade['bastante']), peso['peso medio'])


controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3,regra_4,regra_5,regra_6])

#Simulando
calculoPeso = ctrl.ControlSystemSimulation(controlador)

notaCalorias =int(input("calorias: "))
calculoPeso.input['calorias'] =notaCalorias
notaAtv = int(input('Tempo de atividade: '))
calculoPeso.input['TAtividade'] = notaAtv
calculoPeso.compute()

valorpeso = calculoPeso.output['peso']

print("\ncalorias %d \nTempo de de atividade %d \npeso de %5.2f" %(
        notaCalorias,
        notaAtv,
        valorpeso))


calorias.view(sim=calculoPeso)
TAtividade.view(sim=calculoPeso)
peso.view(sim=calculoPeso)

plt.show()