# ordem de precedencia
# 1 ()
# 2 **
# 3 * / // %
# 4 + -"
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro numero: "))
s = n1 + n2 # soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #divi. inteira 
e = n1 ** n2 #expoente
mo = n1 % n2 #modulo
print(f"a soma vale {s}, a multiplicação vale {m} a divisão vale {d:.3f}, a divi. inteira vale {di}, o expoente vale {e}, e o modulo vale {mo}.  ")

