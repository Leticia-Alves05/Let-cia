"Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo"

import math

angulo = float(input("Digite o ângulo:"))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
s = math.sin(math.radians(angulo))

print(f"O cosseno é {c:.2f}, a tangente é {t:.2f} e o seno é {s:.2f}. ")