Simulador de Probabilidade da Mega-Sena
Este projeto é um programa que calcula a probabilidade ajustada de uma combinação de números ser sorteada na Mega-Sena, considerando os resultados históricos de todos os sorteios. Ele utiliza dados reais, analisa a frequência dos números sorteados e apresenta os resultados por meio de uma interface gráfica amigável.

📋 Funcionalidades
Calcula a probabilidade de uma combinação de números ser sorteada.
Ajusta a probabilidade com base na frequência histórica de cada número.
Interface gráfica simples, criada com Tkinter.
Processamento eficiente de dados históricos usando Pandas.
🚀 Como o Programa Funciona?
Dados Históricos: Os números de todos os sorteios anteriores são carregados de um arquivo Excel.
Análise Estatística: A frequência dos números sorteados é calculada.
Probabilidade Ajustada: A probabilidade base de 1 em 50.063.860 combinações é ajustada pela frequência relativa dos números inseridos.
Resultado: A probabilidade é exibida em formato amigável para o usuário.
📂 Estrutura do Projeto
plaintext
Copiar código
projeto_mega_sena/
├── .gitignore                 # Arquivos e pastas ignorados pelo Git
├── README.md                  # Documentação do projeto
├── mega_simulador_tkinter.py  # Código principal do programa
├── resultados.xlsx            # Dados brutos dos sorteios
├── resultados_limpos.xlsx     # Dados limpos, usados no programa
├── Untitled.ipynb             # Notebook para análise de dados (opcional)
💻 Pré-requisitos
Python 3.10 ou superior instalado no sistema.
As bibliotecas necessárias podem ser instaladas com:
bash
Copiar código
pip install -r requirements.txt
Ou individualmente:
bash
Copiar código
pip install pandas openpyxl
🛠️ Instruções de Execução
Clone este repositório:

bash
Copiar código
git clone https://github.com/Letycia-Locha/mega_simulador_ficticiio.git
cd mega_simulador_ficticiio
Certifique-se de que o arquivo resultados_limpos.xlsx está na pasta principal do projeto.

Execute o programa:

bash
Copiar código
python mega_simulador_tkinter.py
Insira 6 números separados por espaço na interface gráfica e clique no botão "Calcular Probabilidade" para obter o resultado.

📊 Exemplo de Uso
Digite os números: 5 10 23 34 37 53
O programa calculará a probabilidade ajustada e exibirá o resultado, considerando a frequência desses números nos sorteios anteriores.
🔗 Contribuições
Contribuições são bem-vindas! Abra um issue ou envie um pull request para adicionar funcionalidades ou corrigir problemas.

📜 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

