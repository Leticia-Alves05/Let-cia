def multiplicar(n1, n2):
    return n1 * n2


def main():
    num1 = float(input("Digite o 1 numero: "))
    num2 = float(input("Digite o 2 numero: "))

    resultado = multiplicar(num1, num2)

    print(f"{num1} x {num2} = {resultado}")

main()

