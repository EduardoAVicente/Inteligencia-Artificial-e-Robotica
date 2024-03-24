import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from os import system

system('clear')

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

gorjeta = ctrl.Consequent(np.arange(0,31,1),'tip')

qualidade.automf(names=['ruim', 'boa', 'otima'],)
servico.automf(names=['pessimo', 'bom', 'otimo'],)
gorjeta.automf(names=['minima', 'baixa', 'alta'],)
qualidade.view()


regra_1 = ctrl.Rule(qualidade['ruim'] & servico['pessimo'], gorjeta['minima'])
regra_2 = ctrl.Rule(qualidade['ruim'] | servico['pessimo'], gorjeta['baixa'])
regra_3 = ctrl.Rule(servico['bom'], gorjeta['baixa'])
regra_4 = ctrl.Rule(servico['bom'] | qualidade['otima'], gorjeta['alta'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3,regra_4])



CalculoGorjeta = ctrl .ControlSystemSimulation(controlador)
CalculoGorjeta.input['qualidade'] = 6
CalculoGorjeta.input['servico'] = 8

CalculoGorjeta.compute()

print(CalculoGorjeta.output[ 'tip'])

qualidade.view(sim=CalculoGorjeta)
servico.view(sim=CalculoGorjeta)
gorjeta.view(sim=CalculoGorjeta)
