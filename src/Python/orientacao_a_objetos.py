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