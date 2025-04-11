import matplotlib.pyplot as plt 
from skfuzzy import control as ctrl
from regras import regras
from variaveis import qualidade, servico, gorjeta

# Sistema de controle
sistema_controle = ctrl.ControlSystem(regras)
sistema = ctrl.ControlSystemSimulation(sistema_controle)

def calcular_gorjeta(nota_qualidade, nota_servico, mostrar_grafico=False):
    sistema.input['qualidade'] = nota_qualidade
    sistema.input['servico'] = nota_servico
    sistema.compute()
    
    if mostrar_grafico:
        gorjeta.view(sim=sistema)
        plt.show()

    return sistema.output['gorjeta']
