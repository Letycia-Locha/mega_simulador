import pandas as pd
from collections import Counter

# Carregar a planilha limpa com os dados dos sorteios
df = pd.read_excel('resultados_limpos.xlsx', engine='openpyxl')
df_numeros = df[['Número 1', 'Número 2', 'Número 3', 'Número 4', 'Número 5', 'Número 6']]

# Calcular a frequência de cada número
numeros_flat = df_numeros.values.flatten()
frequencia = Counter(numeros_flat)

# Números que mais saíram até hoje
mais_frequentes = {5, 10, 23, 34, 37, 53}

# Total de combinações possíveis na Mega-Sena
TOTAL_COMBINACOES = 50063860

# Função para validar entrada do usuário
def validar_numeros(numeros):
    if len(numeros) != 6:
        return "Erro: Insira exatamente 6 números."
    if any(n < 1 or n > 60 for n in numeros):
        return "Erro: Os números devem estar entre 1 e 60."
    if len(set(numeros)) != 6:
        return "Erro: Não repita números."
    return None

# Função para calcular probabilidade ajustada
def calcular_probabilidade_ajustada(numeros_usuario, df, frequencia, mais_frequentes):
    # Ordenar os números do usuário para comparação
    numeros_usuario = sorted(numeros_usuario)

    # Verificar se a combinação já foi sorteada
    historico = df.values.tolist()
    ja_sorteada = numeros_usuario in [sorted(sorteio) for sorteio in historico]

    if ja_sorteada:
        return "Essa combinação já foi sorteada antes! Possibilidade de ocorrer de novo: extremamente baixa."

    # Calcular o peso baseado na frequência dos números
    peso_comb = sum(frequencia[num] for num in numeros_usuario)

    # Adicionar bônus para os números mais frequentes
    bonus = sum(10 for num in numeros_usuario if num in mais_frequentes)  # Exemplo: bônus de 10 para cada número mais frequente
    peso_total = peso_comb + bonus

    # Normalizar o peso em relação à probabilidade total
    probabilidade_base = 1 / TOTAL_COMBINACOES
    probabilidade_ajustada = probabilidade_base * (peso_total / (sum(frequencia.values()) + len(mais_frequentes) * 10))

    return f"A probabilidade ajustada de essa combinação ser sorteada no próximo sorteio é de aproximadamente {probabilidade_ajustada:.15f}%."

# Programa principal
print("Bem-vindo ao simulador fictício da Mega-Sena!")
entrada = input("Insira 6 números separados por espaço: ")
numeros_usuario = list(map(int, entrada.split()))

# Validar os números
erro = validar_numeros(numeros_usuario)
if erro:
    print(erro)
else:
    # Calcular a probabilidade ajustada
    resultado = calcular_probabilidade_ajustada(numeros_usuario, df_numeros, frequencia, mais_frequentes)
    print(resultado)
