#Representa um tabela de dados contendo colunas, as quais possuem o mesmo tipo, com índices nas linhas e colunas.

#Podemos pensar no DataFrame como um conjunto de Series.

#Embora o DataFrame seja bidimensional em sua maioria das vezes, podemos usar representações com mais dimensões ao usar índices múltiplos/hierárquicos.

import pandas as pd
import numpy as np

# Vamos transformar dados populacionais de SP, PB e RS em um dataframe:
dados = [45.54, 3.94, 11.29]
df = pd.DataFrame(dados)
df = pd.DataFrame(dados, columns=['população'])

# Criando um dicionário com os dados
dados = {'estado': ['SP', 'PB', 'RS'], 'populacao': [45.54, 3.94, 11.29], 'area': [249209, 56585, 281748]}
df = pd.DataFrame(dados)

# Reordenando colunas:
df = pd.DataFrame(dados, columns = ['area', 'estado', 'populacao', 'n_cidades'])

# Indexando colunas e linhas:
df['estado']
df.loc[0]
df.loc[0, 'estado'] # apenas a linha 0 e a coluna 'estado'
df.loc[0]['estado'] # mesmo efeito
df.loc[:, 'estado'] # todas as linhas e a coluna 'estado'
df.loc[:, 'estado':'populacao'] # todas as linhas e as colunas entre 'estado' e 'populacao'
df.loc[:, ['estado', 'area']] # todas as linhas e as colunas 'estado' e 'area', nessa ordem

# Alterando valores:
df.loc[1, 'populacao'] = 4

# Adicionando novas colunas:
n_col = pd.Series([0]*3)
df['nova_coluna'] = n_col

df['nova_coluna'] = [0]*3

# Algumas outras funcionalidades úteis:

dados = {'estado': ['SP', 'PB', 'RS'],
         'populacao': [45.54, 3.94, 11.29],
         'area': [249209, 56585, 281748]}

df = pd.DataFrame(dados)

# Primeiras 2 linhas de `df`:
df.head(2)

# Últimas 2 linhas de `df`:
df.tail(2)

# Inspecionar os índices:
df.index

# Inspecionar as colunas:
df.columns

# Contar elementos:
df.estado.value_counts()

# Inspecionar tipos:
df.dtypes

#remove mas não salva
df.drop('nova_coluna',axis=1) #axis=1 (coluna) ou axis=0 (linha)

#remove e salva
df.drop('nova_coluna',axis=1,inplace=True)

#setando index
df.set_index('estado', inplace=True)

#resetando index
df.reset_index(inplace=True)