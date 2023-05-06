num = 0
while True:
    num = int(input("Digite um número: "))
    if (num < 0) or (num > 9999):
        num = int(input("Digite um número: "))
    else:
        break

num = str(num)
numAdd = num[::-1]

for x in range(len(num)):
    if x == 0:
        print("unidade: {}".format(numAdd[x]))
    elif x == 1:
        print("dezena: {}".format(numAdd[x]))
    elif x == 2:
        print("centena: {}".format(numAdd[x]))
    elif x == 3:
        print("milhar: {}".format(numAdd[x]))