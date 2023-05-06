num = int(input("Digite o valor da tabuada desejada: "))

for x in range(1, 11):
    valor = num * x
    print("{:2} * {} = {}".format(x, num, valor))
