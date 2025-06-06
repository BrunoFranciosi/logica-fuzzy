# Lógica Fuzzy - Sistema Fuzzy de Gorjetas

Este projeto implementa um sistema de lógica fuzzy para sugerir a **porcentagem de gorjeta** com base na **qualidade da comida** e no **atendimento**.

---

## 📊 Lógica Fuzzy

### Entradas:
- **Qualidade da comida** (0 a 10): `ruim`, `boa`, `saborosa`
- **Serviço** (0 a 10): `ruim`, `aceitável`, `ótimo`

### Saída:
- **Gorjeta (%)**: `baixa`, `média`, `alta`

### Regras Fuzzy:
1. Se a **qualidade** for *ruim* ou o **serviço** for *ruim*, então a **gorjeta** será *baixa*
2. Se o **serviço** for *aceitável*, então a **gorjeta** será *média*
3. Se o **serviço** for *ótimo* ou a **qualidade** for *saborosa*, então a **gorjeta** será *alta*

---

## Estrutura do Projeto

- `variaveis.py`: Define variáveis fuzzy e funções de pertinência
- `regras.py`: Define as regras fuzzy 
- `fuzzy_gorjeta.py`: Função para calcular gorjeta com gráfico opcional
- `main.py`: script principal para executar o algoritmo