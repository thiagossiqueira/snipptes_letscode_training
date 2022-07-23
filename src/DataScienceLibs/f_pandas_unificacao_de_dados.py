#Método concat
import pandas as pd
import numpy as np

# Declarando dataframes:
df1 = pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]},index=['w','x','y'])
df2 = pd.DataFrame({'B':[1,2,3],'C':[4,5,6],'D':[7,8,9]},index=['x','y','z'])


# .concat(): concatena ambos, preenchendo dados ausentes com np.nan
pd.concat([df1,df2])

# join='inner': exclui colunas que não estão presentes em ambos
pd.concat([df1,df2],join='inner')

# axis=1 "duplica" colunas que existem em ambos
pd.concat([df1,df2],axis=1)

# axis=0 "duplica" linhas que existem em ambos
pd.concat([df1, df2], axis=0)

# "duplicando" colunas que existem em ambos e excluindo linhas com NAN:
pd.concat([df1, df2], axis=1, join='inner')

# "duplicando" linhas que existem em ambos e excluindo colunas com NAN:
pd.concat([df1, df2], axis=0, join='inner')

#Método merge
import pandas as pd
import numpy as np

# Declarando dataframes:
df3 = pd.DataFrame({'Paises':['BR', 'PT', 'BO'], 'valor1':[6,7,8], 'valor2':[3,4,5]})

df4 = pd.DataFrame({'Paises':['BR', 'PT', 'BO'], 'valor3':[1,2,3], 'valor4':[3,4,5]})

# Unifica ambos:
pd.merge(df3, df4)

# Mantém coluna 'Paises' e "duplica" colunas com indices iguais
pd.merge(df3, df4, on='Paises')