"""
Faça um programa que leia um ano e mostre se ele é BISSEXTO
"""

DIVISOR_BISSEXTO = 4

ano = int(input("Digite o ano desejado: "))

if ano%DIVISOR_BISSEXTO == 0:
    print("O ano {} é bissexto". format(ano))
else:
    print("O ano {} não é bissexto". format(ano))