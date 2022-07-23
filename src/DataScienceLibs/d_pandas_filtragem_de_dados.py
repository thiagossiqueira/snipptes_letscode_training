#Preparação dos dados: Em geral, 80% do tempo gasto com análise e modelagem é buscando e preparando os dados.

import pandas as pd


# Lendo tabela
df = pd.read_csv('microsoft.csv')
df.head()


# Verificando indices das colunas
df.columns


# Modificando indices para as colunas
df.set_axis(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
df.head()

df['Open'].head()


# Criando filtro com | (or)
filtro = (df['Open']>130) | (df['Low']>140)
filtro


# Aplicando filtro
df[filtro]


# Verificando se a mudança foi feita
df


# Criando lista para datas a serem filtradas
dias = range(8,27)
lista_datas = []
for dia in dias:
    string = '2019-04-{:02d}'.format(dia)
    lista_datas.append(string)

lista_datas


# Aplicando em uma máscara
mascara = df['Date'].isin(lista_datas)
mascara


# Verificando resultado
df[mascara]