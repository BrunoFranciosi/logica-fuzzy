import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variáveis de entrada
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

# Variável de saída
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

# Funções de pertinência
qualidade.automf(3, names=['ruim', 'boa', 'saborosa'])
servico.automf(3, names=['ruim', 'aceitável', 'ótimo'])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [2, 10, 18])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])
