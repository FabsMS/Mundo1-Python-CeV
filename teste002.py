n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div_int = n1//n2
resto = n1%n2
expo = n1**n2

print("A soma de {} com {}, resulta em {} e o produto entre eles é {}".format(n1, n2, soma, mult))
print("Já a divisão entre {} e {}, resulta em {:.2f}, e a sua divisão inteira, em {}".format(n1, n2, div, div_int))
print("O resto entre a divisão é {}, enquanto {} elevado à {}, é igual à {}".format(resto, n1, n2, expo))
