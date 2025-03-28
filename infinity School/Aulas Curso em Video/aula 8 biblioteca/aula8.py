
"math"
"ceil -arredonda pra cima"
"floor - arredonda pra baixo"
"trunc - elimina da virgula pra frente"
"pow - potencia"
"sqrt - raiz quadrada "
"factorial - fatorial"


import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"a raiz de {num} é {math.ceil(raiz)}")

print(f"a raiz de {num} é {raiz:.2f}")

"------------------------------------------------------------"

from math import sqrt
num = int(input("Digite um número: "))
raiz = sqrt(num)

print(f"a raiz de {num} é {raiz}")