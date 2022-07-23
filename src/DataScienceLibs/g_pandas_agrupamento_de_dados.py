import pandas as pd

# Lendo arquivo
df = pd.read_csv('ads.csv', delimiter=';')
df.head()

# Agrupando por Gênero e analisando contagem de produtos comprados
df.groupby('Gender')['Purchased'].value_counts()

# Agrupando por Gênero e analisando média de salário
df.groupby('Gender')['EstimatedSalary'].mean()

# Agrupando por Idade e analisando total de produtos comprados
df.groupby('Age')['Purchased'].sum()

# Agrupando por Idade e analisando média de salário
df.groupby('Age')['EstimatedSalary'].mean()

# Agrupando por Gênero e analisando contagem de produtos comprados
df.groupby('Gender')['Purchased'].agg(['value_counts'])

# Agrupando por Gênero e analisando média, mediana e desvio padrão de salário
df.groupby('Gender')['EstimatedSalary'].agg(['mean', 'median', 'std'])

# Renomeando estatísticas
df.groupby('Gender')['EstimatedSalary'].agg(Media='mean', Mediana='median', Desvio='std')