#Matplotlib é a biblioteca de plot mais famosa do python. Ela é extremamente completa, permitindo criação de gráficos de diversas maneiras, e manipulação de vários aspectos do gráficos. Seus plots vão desde de linhas, barras e pizza até plotagem de imagens gráficos de 3d.

#Primeiramente, temos que importar o pacote pyplot da biblioteca; ele nos permitirá criar os gráficos em python. Caso estiver usando o jupyter notebook, também podemos usar a função mágica %matplotlib inline, que nos permite visualizar os gráficos no meio de nosso documento ipynb. Em outros ambientes precisamos da função plt.show().

import numpy as np
# Importando matplotlib e utilizando a função mágica
import matplotlib.pyplot as plt
#%matplotlib inline
#Plots simples
#Criando array sequencial de 0 a 19
array = np.arange(0,10,0.1)
plt.plot(array)
#Plot seno
#Criando seno
seno = np.sin(array)
plt.plot(seno)
#Vários plots em uma mesma figura
plt.plot(seno)
plt.plot(seno*-1)
#Alterando tamanho do gráfico
#mudando tamanho
figure = plt.figure(figsize=(20,10))
plt.plot(seno)
plt.plot(seno*-1)
#Salvando figura
#Para verificar os tipos suportados, tente salvar a figura com um tipo inexistente; o jupyter notebook dará um warning com todos os tipos aceitos pelo matplotlib.

figura = plt.figure(figsize=(15,7))
plt.plot(seno)
figura.savefig('Saida.png')
#Nomes dos eixos e título
figure = plt.figure(figsize=(20,10))
plt.title("Função Seno")
plt.plot(seno)
plt.plot(seno*-1)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
#Cores e estilo das linhas
plt.plot(seno,color='green',marker='o')
plt.plot(array*10,seno*-1,'r--')