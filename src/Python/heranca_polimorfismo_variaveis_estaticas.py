'''
Variáveis estáticas
Até o momento, todos os atributos (variáveis) e métodos (funções) que vimos são do OBJETO, não da CLASSE. No exemplo da Comida, CADA COMIDA possuía um nome, um preço etc.

Em alguns casos é interessante ter uma variável ESTÁTICA - uma variável que é única para a classe inteira. Esse tipo de variável é útil para controle da classe. Por exemplo, contar quantos objetos foram instanciados, guardar uma lista dos objetos daquela classe, entre várias outras coisas.
'''

class Produto:
    lista = [] # lista é uma variável estática da classe Produto
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.lista.append(self.nome) # acrescentamos o nome dos objetos na lista
    def __repr__(self):
        return self.nome + ' vendeu ' + str(self.quantidade) + ' unidades.'

p1 = Produto('Caneta', 1.00, 2000)
p2 = Produto('Papel', 10.00, 5000)
p3 = Produto('Lápis', 0.50, 3000)

for p in Produto.lista:  #chamamos a variável estática usando Classe.variavelestatica
    print(p)

'''
Herança e polimorfismo
Uma classe pode ser herdeira de outra. Dizemos que a classe original é a classe pai, e a herdeira é a classe filha. Quando uma classe é herdeira de outra, ela automaticamente herda todos os atributos e métodos da classe original. Podemos implementar na classe nova novas versões dos métodos antigos. Quando isso ocorre, os objetos da classe filha utilizarão essas versões novas. Quando isso não ocorre, são usados os métodos da classe pai mesmo. Os métodos da classe pai - bem como qualquer função feita para trabalhar com a classe pai - conseguem, automaticamente, trabalhar também com as classes filhas como se elas fossem membros da classe pai. Isso chama-se POLIMORFISMO: se a classe Y é herdeira de X, um objeto da classe Y é reconhecido também como um objeto da classe X.
'''
class Produto:
    lista = [] # lista é uma variável estática da classe Produto
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        Produto.lista.append(self.nome) # acrescentamos o nome dos objetos na lista
    def __repr__(self):
        return self.nome + ' vendeu ' + str(self.quantidade) + ' unidades.'

# Livro herda de Produto
class Livro(Produto):
    def __init__(self, nome, preco, quantidade, paginas):
        super().__init__(nome, preco, quantidade) #chama a inicialização da classe pai
        self.paginas = paginas # inicializa o que tem de diferente em relação à classe pai
    def __repr__(self):
        return self.nome + ' vendeu ' + str(self.quantidade) + ' unidades e tem ' + str(self.paginas) + ' paginas.' # atualiza o método mágico __repr__ da classe pai

p1 = Produto('Caneta', 1.00, 2000)
p2 = Produto('Lápis', 0.5, 5000)
p3 = Livro('Harry Potter', 40, 1000, 300)

print(p1)
print(p2)
print(p3)

for p in Produto.lista: #chamamos a variável estática usando Classe.variavelestatica
    print(p)

