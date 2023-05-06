"""
Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0.50 por KM
para viagens de até 200KM, e R$0.45 para viagens mais longas
"""

LIMITE_KM = 200
PRECO_200KM = 0.50
PRECO_KM_MAIOR = 0.45

quilometragem = float(input("Digite a distância, em KM, da viagem que deseja fazer: "))

if quilometragem <= LIMITE_KM:
    print("Considerando a quilometragem da sua viagem, o valor cobrado para ela seria de R${:.2f}".format(PRECO_200KM*quilometragem))
else:
    print("Considerando a quilometragem da sua viagem, o valor cobrado para ela seria de R${:.2f}".format(PRECO_KM_MAIOR*quilometragem))