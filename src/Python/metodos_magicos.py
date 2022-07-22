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