from fuzzy_gorjeta import calcular_gorjeta

if __name__ == '__main__':
    qualidade = float(input("Nota da qualidade da comida (0 a 10): "))
    servico = float(input("Nota do serviço (0 a 10): "))

    mostrar = input("Deseja exibir o gráfico do sistema fuzzy? (s/n): ").lower() == 's'
    resultado = calcular_gorjeta(qualidade, servico, mostrar_grafico=True)

    print(f"Gorjeta sugerida: {resultado:.2f}%")
