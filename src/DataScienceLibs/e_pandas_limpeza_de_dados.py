#É muito comum termos dados faltando na nossa series ou dataframe. O Pandas identifica os dados ausentes com o uso do np.nan, e são chamados de NA (Not Available). Vamos estudar alguns métodos interessantes quando tratando desses casos:

import pandas as pd
import numpy as np

ss = pd.Series([7, 5, np.nan, -888, -999, None,  9])
#.dropna(): Remove NA de uma Series ou DataFrame.

ss.dropna()
#.fillna(): Substitui NA por algum valor (diversos métodos disponíveis).

ss.fillna(1000)
#.isnull(): Retorna booleanos informando quais valores estão ausentes.

ss.isnull()
#.notnull(): Inverso de isnull.

ss.notnull()
#"Flags" são comuns quando trabalhando com dados que estão faltando:

ss.replace(-999, np.nan)
ss.replace([-999, -888], np.nan)
ss.replace([-999, -888], [0, np.nan])
ss.replace({-999: 0, -888: np.nan})

#Vamos ver agora como nos livrarmos dos nans:

ss2 = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
ss2.head()
#Dropa >linhas< que têm valores nan:

ss2.dropna()
#Para dropar >colunas<, utilizar 'axis=1':

ss2.dropna(axis=1)
#Preenchendo valores nan:

ss2.fillna('Isso não é um número')
#Verificando número de valores nan para cada coluna:

ss2.isnull().sum()