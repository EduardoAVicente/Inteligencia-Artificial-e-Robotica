
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


# Variaveis antecedentes
altura = ctrl.Antecedent(np.arange(0, 300, 1), 'altura')
peso = ctrl.Antecedent(np.arange(0, 200, 1), 'peso')
sedentarismo = ctrl.Antecedent(np.arange(0, 11, 1), 'sedentarismo')
alimentacao = ctrl.Antecedent(np.arange(0, 11, 1), 'alimentacao')


#Variaveis conseguente
obesidade = ctrl.Consequent(np.arange(0, 100, 1), 'obesidade')

# automf -> Atribuição de categorias automaticamente
altura.automf(names=['baixo','medio','alto'],)
peso.automf(names=['baixo','medio','alto'])
sedentarismo.automf(names=['baixo','medio','alto'])
alimentacao.automf(names=['baixo','medio','alto'])


obesidade.automf(names=['inexistente','baixo','medio','alto','extremo'])

#Visualizando as variáveis
altura.view()
peso.view()
sedentarismo.view()
alimentacao.view()
obesidade.view()



#Criando as regras
regra_1 = ctrl.Rule(altura['baixo'] & peso['baixo'] & sedentarismo['alto'] & alimentacao['medio'], obesidade['medio'])
regra_2 = ctrl.Rule(altura['medio'] & peso['medio'] & sedentarismo['medio'] & alimentacao['medio'], obesidade['medio'])
regra_3 = ctrl.Rule(altura['alto'] & peso['alto'] & sedentarismo['baixo']& alimentacao['baixo'], obesidade['medio'])
regra_4 = ctrl.Rule(altura['alto'] & peso['alto'] & sedentarismo['alto'] & alimentacao['baixo'], obesidade['extremo'])
regra_5 = ctrl.Rule(altura['baixo'] & peso['alto'] & sedentarismo['baixo'] & alimentacao['baixo'], obesidade['medio'])
regra_6 = ctrl.Rule(altura['alto'] & peso['baixo'] & sedentarismo['baixo'] & alimentacao['alto'], obesidade['inexistente'])
regra_7 = ctrl.Rule(altura['alto'] & peso['baixo'] & sedentarismo['baixo'] & alimentacao['medio'], obesidade['baixo'])
regra_8 = ctrl.Rule(altura['alto'] & peso['medio'] & alimentacao['alto'] & sedentarismo['medio'], obesidade['medio'])
regra_9 = ctrl.Rule(altura['medio'] & peso['medio'] & alimentacao['alto'] & sedentarismo['medio'], obesidade['medio'])
regra_10 = ctrl.Rule(altura['alto'] & peso['medio'] & alimentacao['alto'] & sedentarismo['baixo'], obesidade['medio'])
regra_11 = ctrl.Rule(sedentarismo['alto'] & alimentacao['baixo'], obesidade['extremo'])
regra_12 = ctrl.Rule(altura['alto'] & alimentacao['baixo'], obesidade['medio'])
regra_13 = ctrl.Rule(peso['baixo'] & sedentarismo['alto'], obesidade['medio'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3, regra_4, regra_5, regra_6, regra_7, regra_8, regra_9, regra_10, regra_11, regra_12, regra_13])




#Simulando
CalculoObesidade = ctrl.ControlSystemSimulation(controlador)

notaAltura = int(input('Altura(Cm): '))
notaPeso = int(input('peso(Kg): '))
notaSedentarismo = int(input('De 0 a 10 qual seu nivel de sedentarismo: '))
notaAlimentacao = int(input('De 0 a 10 qual a qualidade de suas refeicoes: '))

CalculoObesidade.input['altura'] = notaAltura
CalculoObesidade.input['peso'] = notaPeso
CalculoObesidade.input['sedentarismo'] = notaSedentarismo
CalculoObesidade.input['alimentacao'] = notaAlimentacao

CalculoObesidade.compute()

valorObesidade = CalculoObesidade.output['obesidade']


print("\naltura %d \nPeso %d \nsedentarismo de %5.2f" %(
       notaAltura,
       notaPeso,
       valorObesidade,
       ))


altura.view(sim=CalculoObesidade)
peso.view(sim=CalculoObesidade)
sedentarismo.view(sim=CalculoObesidade)
alimentacao.view(sim=CalculoObesidade)

plt.show()      