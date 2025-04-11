from skfuzzy import control as ctrl
from variaveis import qualidade, servico, gorjeta

# Regras fuzzy
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['saborosa'], gorjeta['alta'])

regras = [regra1, regra2, regra3]