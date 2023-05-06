"""
Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR
"""
from sys import maxsize

MAIOR = 0
MENOR = maxsize

for i in range(3):
    num = float(input("Digite o número desejado: "))
    if num > MAIOR:
        MAIOR = num
    elif num < MENOR:
        MENOR = num

print("{} foi o maior número digitado, enquanto {} foi o menor".format(MAIOR, MENOR))