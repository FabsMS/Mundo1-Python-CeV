"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250.00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
"""

SALARIO_LIMITE = 1250

salario = float(input("Digite o valor do salário do funcionário em questão: "))

if salario > SALARIO_LIMITE:
    novo_salario = salario * 1.1
    print("O novo salário desse funcionário será de {:.2f}".format(novo_salario))
else:
    novo_salario = salario * 1.15
    print("O novo salário desse funcionário será de {:.2f}".format(novo_salario))