#Pandas é uma biblioteca de Data Science do Python que nos permite ler e analisar dados de maneira bastante prática e intuitiva.

#Vantagens:

#Constante evolução, com mais de 800 contribuidores;
#Uso em conjunto com outras bibliotecas, como Numpy e Matplotlib;
#Contém estruturas de dados e ferramentas para manipulação;
#Projetado para trabalhar com dados tabulares e heterogêneos.

#Instalação: pip install pandas

#Series
#Series é um objeto do tipo array unidimensional contendo uma sequência com valores de tipos semelhantes e um array associado de rótulos, chamados de índices (index).

import pandas as pd
import numpy as np

# Criando uma Series
col = pd.Series([4, 7, -5, 3])

#Acessando dados como um lista
col[1]

# Especificando os nomes dos índices
col = pd.Series([4, 7, -5, 3], index =['d', 'b', 'a', 'c'])

# Selecionando valores específicos
col['a']
col[['c', 'a', 'd']] # Não esquecer de passar o argumento como uma lista

# Comparando todos elementos
col > 0

# Máscaras: selecionando apenas os elementos para os quais elemento > 0
col[col > 0]

# Outras operações elemento a elemento
col*2
np.exp(col)

# Operações com mais de uma series
dic1 = {"Brasil":10,"EUA":10,"Japão":10}
serie1 = pd.Series(dic1)
dic2 = {"Brasil":10,"Bolivia":10,"Japão":10}
serie2 = pd.Series(dic2)
serie1 + serie2

#Contando valores
serie1.value_counts()

#isin - Para filtar valores
mask = serie1.isin(['b', 'c'])
mask

serie1[mask]

#unique
serie1 = pd.Series(['a','b','c','a','d','e','c','a','e','d'])
serie1.unique()

# Pode-se criar uma Series a partir de um dicionário:
pop_dic = {'Sao Paulo': 12.25, 'Guarulhos': 1.38, 'Santo Andre': 0.72}
pop = pd.Series(pop_dic)

# Analisando algumas cidades na Series
cidades = ['Santo Andre', 'Osasco', 'Guarulhos']
pop = pd.Series(pop_dic, index = cidades)
pd.isnull(pop)