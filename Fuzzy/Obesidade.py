
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
       
       obesidade.automf(names=['inexistente', 'baixo', 'medio', 'alto', 'extremo'])


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

       alimentacao['baixo'] = fuzz.trimf(alimentacao.universe, [0, 3, 6])
       alimentacao['medio'] = fuzz.trimf(alimentacao.universe, [3, 6, 8])
       alimentacao['alto'] = fuzz.trimf(alimentacao.universe, [6, 8, 10])
       
       obesidade['inexistente'] = fuzz.trimf(obesidade.universe, [0, 0, 25])
       obesidade['baixo'] = fuzz.trimf(obesidade.universe, [0, 25, 50])
       obesidade['medio'] = fuzz.trimf(obesidade.universe, [25, 50, 75])
       obesidade['alto'] = fuzz.trimf(obesidade.universe, [50, 75, 100])
       obesidade['extremo'] = fuzz.trimf(obesidade.universe, [75, 100, 100])

def gaugasiana():
       # Funções gaussianas
       altura['baixo'] = fuzz.gaussmf(altura.universe, 50, 30)
       altura['medio'] = fuzz.gaussmf(altura.universe, 150, 40)
       altura['alto'] = fuzz.gaussmf(altura.universe, 250, 30)

       peso['baixo'] = fuzz.gaussmf(peso.universe, 70, 20) 
       peso['medio'] = fuzz.gaussmf(peso.universe, 120, 30)
       peso['alto'] = fuzz.gaussmf(peso.universe, 170, 20)

       sedentarismo['baixo'] = fuzz.gaussmf(sedentarismo.universe, 2, 1)
       sedentarismo['medio'] = fuzz.gaussmf(sedentarismo.universe, 6, 2)
       sedentarismo['alto'] = fuzz.gaussmf(sedentarismo.universe, 9, 1)

       alimentacao['baixo'] = fuzz.gaussmf(alimentacao.universe, 3, 1)
       alimentacao['medio'] = fuzz.gaussmf(alimentacao.universe, 7, 2)
       alimentacao['alto'] = fuzz.gaussmf(alimentacao.universe, 9, 1)
       
       obesidade['inexistente'] = fuzz.gaussmf(obesidade.universe, 10, 5)
       obesidade['baixo'] = fuzz.gaussmf(obesidade.universe, 30, 10)
       obesidade['medio'] = fuzz.gaussmf(obesidade.universe, 50, 10)
       obesidade['alto'] = fuzz.gaussmf(obesidade.universe, 70, 10)
       obesidade['extremo'] = fuzz.gaussmf(obesidade.universe, 90, 5)



def trapezoidais():
       # Funções trapezoidais
       altura['baixo'] = fuzz.trapmf(altura.universe, [150, 150, 200, 225])
       altura['medio'] = fuzz.trapmf(altura.universe, [200, 225, 275, 300])
       altura['alto'] = fuzz.trapmf(altura.universe, [275, 300, 350, 350])

       peso['baixo'] = fuzz.trapmf(peso.universe, [0, 0, 30, 50])
       peso['medio'] = fuzz.trapmf(peso.universe, [30, 50, 70, 90])
       peso['alto'] = fuzz.trapmf(peso.universe, [70, 90, 100, 100])

       sedentarismo['baixo'] = fuzz.trapmf(sedentarismo.universe, [0, 0, 2, 3])
       sedentarismo['medio'] = fuzz.trapmf(sedentarismo.universe, [2, 3, 7, 8])
       sedentarismo['alto'] = fuzz.trapmf(sedentarismo.universe, [7, 8, 10, 10])

       alimentacao['baixo'] = fuzz.trapmf(alimentacao.universe, [0, 0, 3, 4])
       alimentacao['medio'] = fuzz.trapmf(alimentacao.universe, [3, 4, 7, 8])
       alimentacao['alto'] = fuzz.trapmf(alimentacao.universe, [7, 8, 10, 10])
       
       obesidade['inexistente'] = fuzz.trapmf(obesidade.universe, [0, 0, 20, 30])
       obesidade['baixo'] = fuzz.trapmf(obesidade.universe, [20, 30, 40, 50])
       obesidade['medio'] = fuzz.trapmf(obesidade.universe, [40, 50, 60, 70])
       obesidade['alto'] = fuzz.trapmf(obesidade.universe, [60, 70, 80, 90])
       obesidade['extremo'] = fuzz.trapmf(obesidade.universe, [80, 90, 100, 100])

if grafico == 1:
       triangulo()
elif grafico == 2:
       trapezoidais()
elif grafico == 3:
       gaugasiana()
elif grafico == 4:
       automatico()
else:
       print("Opção inválida. Escolha um número de 1 a 4 para o tipo de gráfico.")
       exit(1)
            
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

# notaAltura = int(input('Altura(Cm): '))
# notaPeso = int(input('peso(Kg): '))
# notaSedentarismo = int(input('De 0 a 10 qual seu nivel de sedentarismo: '))
# notaAlimentacao = int(input('De 0 a 10 qual a qualidade de suas refeicoes: '))


notaAltura = 170
notaPeso = 85
notaSedentarismo = 6
notaAlimentacao = 8


CalculoObesidade.input['altura'] = notaAltura
CalculoObesidade.input['peso'] = notaPeso
CalculoObesidade.input['sedentarismo'] = notaSedentarismo
CalculoObesidade.input['alimentacao'] = notaAlimentacao

CalculoObesidade.compute()

valorObesidade = CalculoObesidade.output['obesidade']


print("\naltura: %d \nPeso: %d \nSedentarismo: %d \nAlimentacao: %d \nGrau de obesidade: %5.2f" %(
       notaAltura,
       notaPeso,
       notaSedentarismo,
       notaAlimentacao,
       valorObesidade
       ))


altura.view(sim=CalculoObesidade)
peso.view(sim=CalculoObesidade)
sedentarismo.view(sim=CalculoObesidade)
alimentacao.view(sim=CalculoObesidade)
plt.show()      