#Até o momento, vimos alguns jeitos diferentes de agrupar dados: - listas: é uma estrutura mutável, onde utilizamos índices para buscar dados - tuplas: outra estrutura indexada, mas imutável - dicionários: uma coleção de pares chave-valor
#Essas estruturas podem ser um pouco limitadas quando queremos agregar uma grande quantidade de informações sobre um mesmo "tema", e muitas vezes fizemos "gambiarras" trabalhando com múltiplas listas, criamos funções para tratar esses dados espalhados etc.

#Podemos agregar todos os dados sobre uma certa entidade em um OBJETO. Para criarmos objetos, devemos definir uma CLASSE, que é a "receita" para construir um objeto.

#Todos os objetos de uma mesma classe possuirão as mesmas variáveis internas (atributos) e funções internas (métodos).

#Toda classe deve possui um método construtor, que irá "ensinar" o Python como montar o seu objeto. É uma boa prática inicializar os atributos no construtor. Em Python, o construtor sempre se chamará init

class Comida:
   # para que uma função possa atuar sobre o objeto que a chamou,
   # é necessário passar "self" como parâmetro
   # self se refere a esse objeto
   def __init__(self, nome, preco, ingredientes):
       self.nome = nome
       self.preco = preco
       self.ingredientes = ingredientes
       # o objeto que está sendo criado recebeu em seus atributos os
       # valores passados como parâmetro
   def apresentacao(self):
       print ("Receita de", self.nome + ": " + ', '.join(self.ingredientes))
       print("O seu preço é R$" + str(self.preco))
   def promocao(self, desconto):
       self.preco -= desconto
       return self.preco


# Para criarmos objetos de uma classe, usamos uma atribuição "chamando"
# a classe como se fosse uma função. Isso irá chamar o método construtor.
hamburguer = Comida("Hamburguer", 20, ["Pão", "Carne"])
pizza = Comida("Pizza", 40, ["Massa", "Molho de tomate", "Queijo"])

# Utilizamos o ponto (.) para acessar métodos ou atributos do objeto:
print(hamburguer.nome, hamburguer.preco, hamburguer.ingredientes)

# Métodos são acessados colocando parênteses após seus respectivos nomes:
hamburguer.promocao(5)
pizza.promocao(10)
hamburguer.apresentacao()
pizza.apresentacao()