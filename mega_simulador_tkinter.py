import tkinter as tk
from tkinter import messagebox
from collections import Counter
import pandas as pd

# Carregar os dados da planilha
df = pd.read_excel('resultados_limpos.xlsx', engine='openpyxl')
df_numeros = df[['Número 1', 'Número 2', 'Número 3', 'Número 4', 'Número 5', 'Número 6']]
numeros_flat = df_numeros.values.flatten()
frequencia = Counter(numeros_flat)

# Função para validar os números
def validar_numeros(numeros):
    if len(numeros) != 6:
        return "Erro: Insira exatamente 6 números."
    if any(n < 1 or n > 60 for n in numeros):
        return "Erro: Os números devem estar entre 1 e 60."
    if len(set(numeros)) != 6:
        return "Erro: Não repita números."
    return None

# Função para calcular a probabilidade ajustada
def calcular_probabilidade_ajustada(numeros_usuario):
    TOTAL_COMBINACOES = 50063860
    peso_comb = sum(frequencia[num] for num in numeros_usuario)
    probabilidade_base = 1 / TOTAL_COMBINACOES
    probabilidade_ajustada = probabilidade_base * (peso_comb / sum(frequencia.values()))
    return f"A probabilidade ajustada de essa combinação ser sorteada é de aproximadamente {probabilidade_ajustada:.15f}%."

# Função acionada pelo botão
def calcular_probabilidade():
    entrada = numeros_entry.get()
    try:
        numeros_usuario = list(map(int, entrada.split()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números separados por espaço.")
        return

    erro = validar_numeros(numeros_usuario)
    if erro:
        messagebox.showerror("Erro", erro)
        return

    resultado = calcular_probabilidade_ajustada(numeros_usuario)
    messagebox.showinfo("Resultado", resultado)

# Criar a interface gráfica
root = tk.Tk()
root.title("Simulador da Mega-Sena")

tk.Label(root, text="Insira 6 números separados por espaço:").pack(pady=10)
numeros_entry = tk.Entry(root, width=40)
numeros_entry.pack(pady=10)

calcular_button = tk.Button(root, text="Calcular Probabilidade", command=calcular_probabilidade)
calcular_button.pack(pady=10)

root.mainloop()
