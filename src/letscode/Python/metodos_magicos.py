#É intuitivo deduzir o que acontece quando fazemos int + int, ou quando mandamos imprimir um float. Mas observe que certos dados em Python possuem comportamentos "surpreendentes" e úteis. Por exemplo, ao darmos print em uma lista, ela aparece representada com colchetes e vírgulas separando os dados. Quando somamos 2 strings, elas são concatenadas.

#Chamamos de SOBRECARGA DE OPERADORES o ato de ensinarmos ao nosso programa como ele deve aplicar um certo operador sobre os objetos de uma certa classe. Para sobrecarregarmos operadores em Python, utilizamos os "métodos mágicos": funções padrão que o Python irá ligar a certos operadores. Vejamos alguns dos mais comuns:

#_add_: soma

#_sub_: subtração

#_mul_: multiplicação

#_truediv_: divisão

#_mod_: resto da divisão

#_pow_: expoente

#_lt_: "less than" <

#_le_: "less or equal" <=

#_gt_: "greater than" >

#_ge_: "greater or equal" >=

#_eq_: "equal" ==

#_ne_: "not equal" !=

#_repr_: a string retornada por esse método é utilizada pelo print

#Vejamos um exemplo com uma grandeza vetorial de 2 dimensões, representada por 2 coordenadas i e j ex: 2i + 4j Vamos criar uma classe e usar alguns métodos mágicos pra decidir como somar e subtrair 2 vetores, comparar se são iguais ou diferentes e imprimir na forma bonitinha acima.

class Vetor2Dimensoes:
   def __init__(self, i, j):
       self.i = i
       self.j = j
   def __add__(self, other):
       resultadoi = self.i + other.i
       resultadoj = self.j + other.j
       resultado = Vetor2Dimensoes(resultadoi, resultadoj)
       return resultado
   def __sub__(self, other):
       resultadoi = self.i - other.i
       resultadoj = self.j - other.j
       resultado = Vetor2Dimensoes(resultadoi, resultadoj)
       return resultado
   def __eq__(self, other):
       if self.i == other.i and self.j == other.j:
           return True
       else:
           return False
   def __ne__(self, other):
       if self.i != other.i or self.j != other.j:
           return True
       else:
           return False
   def __repr__(self):
       impressao = str(self.i) + 'i+' + str(self.j) + 'j'
       return impressao
   def __mul__(self, other):
       resultado = self.i*other.i + self.j*other.j
       return resultado

v1 = Vetor2Dimensoes(2,4)
v2 = Vetor2Dimensoes(3,5)

if v1 == v2:
   print(v1, "igual a", v2)
else:
   print(v1, "diferente de", v2)

vt = v1 + v2
print(v1, '+', v2, '=', vt)