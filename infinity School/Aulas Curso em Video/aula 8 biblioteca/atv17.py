
c_oposto = float(input("Digite o comprimento do cateto oposto: "))
c_adjacente = float(input("Digite o comprimento do adjacente oposto: "))

comp_hipotenusa = (c_oposto ** 2 + c_adjacente ** 2) ** (1/2)

print(f" o comprimento da hipotenusa é {comp_hipotenusa:.2f}")

"--------------------------------------------------------------"
import math
c_oposto = float(input("Digite o comprimento do cateto oposto: "))
c_adjacente = float(input("Digite o comprimento do adjacente oposto: "))

comp_hipotenusa = math.hypot(c_oposto, c_adjacente)

print(f" o comprimento da hipotenusa é {comp_hipotenusa:.2f}")




"Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e  calcule e mostre o comprimento da hipotenusa"