from math import pow, sqrt

cateto1 = int(input("Digite o valor do cateto 1: "))
cateto2 = int(input("Digite o valor do cateto 2: "))

hipotenusa = sqrt((pow(cateto1, 2) + pow(cateto2, 2)))

print("Esse é o valor da hipotenusa: {}".format(hipotenusa))