import pandas as pd
from IPython.display import display
import plotly.express as px
import pyautogui
import time
import pyperclip


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 1: Importar a base de Dados
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

tabela = pd.read_csv("telecom_users.csv")


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 2: Visualizar a Base de dados
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# Excluir coluna não utilizada
# axis = 0 -> eixo da Linha
# axis = 1 -> eixo da Coluna
# para excluir coluna = tabela.drop("nomedacoluna", axis=1)
# para excluir linha = tabela.drop(numerodalinha, axis=0)
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 3: Tratamento de Dados
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Olhar os tipos que o python esta lendo para cada coluna
#print(tabela.info())

# Informações de Tipo Errado (Total Gasto)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Informações vazias
# Colunas completamente Vazias -> Excluir
tabela = tabela.dropna(how = "all" , axis=1)
# Linhas que tem informações Vazias -> Excluir
tabela = tabela.dropna(how ="any", axis=0)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 4: Análise Inicial dos Dados
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Como estão os cancelamentos?
print(tabela["Churn"].value_counts())

# Percentual de Cancelamentos em relação ao Total
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 5: Descobrir os motivos do Cancelamento
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Etapa 1: Cria o Gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color = "Churn", text_auto=True)
    # Etapa 2: Exibe o Gráfico



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Conclusões
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Clientes que estão a pouco tempo estão cancelando muito
    # Pode Estar fazendo alguma promoção de 1° mês Grátis
    # O inicio do serviço pode estar sendo confuso
    # A 1° experiência do cliente pode estar sendo ruim.
    # Podemos criar incentivos nos primeiros meses

# Boleto eletrônico tem muito mais cancelamentos
    # Dar desconto nas outras formas de pagamento onde a taxa de cancelamento é menor

# Onde os contratos são mensais a taixa de cancelamento é muito maior
    # Dar desconto para planos Anuais

# Quanto mais serviços o cliente tem, menor a chance de cancelar.
    # Oferecer mais serviços com planos mais baratos

# Clientes com mais linhas (família maior) tem menos chances de cancelar
    # 2 linha de graça ou com desconto


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 6: Entrar no Email
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


pyautogui.press("win")
time.sleep(2)
pyautogui.write("chrome")
time.sleep(3)
pyautogui.press("enter")
time.sleep(4)

pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox") #copiando o link
pyautogui.hotkey("ctrl", "v") #colando o link
pyautogui.press("enter")
time.sleep(5)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Passo 7: Mandar um email para a diretoria com os indicadores
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

pyautogui.click(x=44, y=268) # clicar no +
time.sleep(5)
#escrevendo o destinatário
pyperclip.copy("caahjoannes@gmail.com") #copiando o email
pyautogui.hotkey("ctrl", "v") #colando o email
pyautogui.press("tab") # passando para o assunto

#escrevendo o assunto
pyperclip.copy("Relatório Diário") #copiando o assunto
pyautogui.hotkey("ctrl", "v") #colando o assunto
pyautogui.press("tab") #passando para o texto

#escrevendo o texto
texto = f"""
Prezados, Bom dia.

Encontrei algumas inconsistências nos dados.
* Clientes que estão a pouco tempo estão cancelando muito
    - Pode estar fazendo alguma promoção de 1° mês Grátis
    - O inicio do serviço pode estar sendo confuso
    - A 1° experiência do cliente pode estar sendo ruim.
    - Podemos criar incentivos nos primeiros meses

* Boleto eletrônico tem muito mais cancelamentos
    - Dar desconto nas outras formas de pagamento onde a taxa de cancelamento é menor

* Onde os contratos são mensais a taxa de cancelamento é muito maior
    - Dar desconto para planos Anuais

* Quanto mais serviços o cliente tem, menor a chance de cancelar.
    - Oferecer mais serviços com planos mais baratos

* Clientes com mais linhas (família maior) tem menos chances de cancelar
    - 2° linha de graça ou com desconto

* Clientes com fatura Digital tem mais chance de cancelar
    - Imprimir os boletos.  

* Clientes que não usam o nosso serviço de suporte cancelam mais
    - Informar mais do nosso sistema de Suporte.
    - Deixá-lo mais acessível.

Segue abaixo os Gráficos relevantes para a Análise.


Ass
Camilli Joannes - Gerente de Vendas
"""
pyperclip.copy(texto) #copiando o texto
pyautogui.hotkey("ctrl", "v") #colando o texto
time.sleep(2)
pyautogui.click(x=1347, y=965)
time.sleep(2)
pyautogui.click(x=109, y=324)
pyautogui.click(x=304, y=320, clicks=2)
pyautogui.hotkey("ctrl", "a") 
pyautogui.press("enter")
time.sleep(15)

#enviar o email
pyautogui.hotkey("ctrl", "enter")

