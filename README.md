#Simulador de Probabilidade da Mega-Sena

Este programa calcula a probabilidade ajustada de uma combinação específica de números ser sorteada na Mega-Sena. Ele utiliza uma interface gráfica simples (Tkinter) e analisa os dados de sorteios anteriores para fornecer uma estimativa baseada na frequência dos números sorteados.

#Pré-requisitos
Antes de executar o programa, certifique-se de que o ambiente atende aos seguintes pré-requisitos:

Python 3.10 ou superior: Baixe e instale o Python em https://www.python.org/.
Bibliotecas Python necessárias:
pandas
openpyxl
tkinter (já incluído por padrão na maioria das instalações do Python)
Instalar Dependências
Execute o comando abaixo no terminal para instalar as bibliotecas necessárias:

bash
Copiar código
pip install pandas openpyxl
Instruções de Instalação e Execução
Clone o repositório ou baixe os arquivos do programa.

Certifique-se de que o arquivo resultados_limpos.xlsx (com os dados de sorteios anteriores) esteja no mesmo diretório do programa.

Execute o programa com o comando:

bash
Copiar código
python mega_simulador_tkinter.py
A interface gráfica será aberta. Insira os 6 números separados por espaço e clique no botão "Calcular Probabilidade" para obter a estimativa.

Como o Programa Calcula a Probabilidade
O cálculo da probabilidade ajustada é baseado em três fatores principais:

Frequência dos Números:

O programa analisa a frequência com que cada número foi sorteado no histórico de sorteios.
Números que aparecem com mais frequência recebem um peso maior no cálculo da probabilidade.
Total de Combinações Possíveis:

A Mega-Sena possui 50.063.860 combinações possíveis de 6 números, considerando que os números variam de 1 a 60 e não se repetem.
Ajuste com Base no Histórico:

A probabilidade base é ajustada proporcionalmente ao peso total dos números inseridos pelo usuário, considerando sua frequência relativa no histórico de sorteios.
Exemplo de Cálculo
Se você inserir os números 5, 10, 23, 34, 37, 53, o programa:
Soma os pesos correspondentes às frequências desses números.
Ajusta a probabilidade base (1/50.063.860) proporcionalmente à soma dos pesos.
Exibe a probabilidade ajustada em uma mensagem.
Estrutura do Projeto
bash
Copiar código
projeto_mega_sena/
│
├── resultados_limpos.xlsx   # Arquivo Excel com os dados de sorteios anteriores
├── mega_simulador_tkinter.py # Código principal do programa
├── README.md                # Instruções e informações do projeto
Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.

Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

