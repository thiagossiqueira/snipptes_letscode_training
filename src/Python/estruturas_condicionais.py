#If
#O if testa uma condição:
#se ela for verdadeira, seu conteúdo é executado;
#caso contrário, seu conteúdo é ignorado.

idade = int(input('Digite sua idade:'))
if idade >= 12:
   print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
   print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

#Utilizamos um 'tab' antes de cada linha pertencente ao if. No exemplo acima, a linha 'obrigado por participar' sempre será exibida. Já a linha 'Você pode entrar na montanha russa.' só será exibida se a idade digitada for maior ou igual a 12 e a altura digitada for maior ou igual a 1.60.

#Else
#Em alguns casos, queremos que o programa escolha entre 2 casos mutuamente exclusivos. Para isso utilizamos o else. O else não possui condição para verificar. O else sempre vem imediatamente após um if e é executado se o if for ignorado.

idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
   print('Você pode entrar na montanha russa.')
else:
   print('Você não pode entrar na montanha russa.')
print('Obrigado por participar.')

#É possível "aninhar" diversos if's e else's. O programa abaixo só deixa a pessoa entrar no brinquedo se tiver idade e altura mínimas:

idade = int(input('Digite sua idade:'))
if idade >= 12:
   resposta = input('Você gostaria de entrar nesta montanha russa?')
   if (resposta == 'sim'):
       print('Por favor, entre!')
   else:
       print('Ok então')
else:
   print('Você não tem idade para esse brinquedo.')

#Elif
#Podemos testar diversos casos mutuamente exclusivos utilizando o 'elif'.

#elif é a contração de "else if" - ou seja, caso um if não seja executado, você pode propor uma nova condição para ser testada.

exercicios = int(input('Quantos exercícios de Python vc já fez?'))

if exercicios > 30:
   print('Já está ficando profissional!')
elif exercicios > 20:
   print('Tá indo bem, bora fazer mais alguns!')
elif exercicios > 10:
   print('Vamos tirar o atraso?')
else:
   print('Xiiii...')