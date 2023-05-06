"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
"""

ladoA = int(input("Digite o comprimento do primeiro lado: "))
ladoB = int(input("Digite o comprimento do segundo lado: "))
ladoC = int(input("Digite o comprimento do terceiro lado: "))

if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoC + ladoB > ladoA):
    print("É possível formar um triângulo com esses três segmentos de reta")
else:
    print("Não é possível formar um triângulo com esses três segmentos de reta")
