LIMITE = 80
VALOR_KM = 7

velocidade = int(input("Digite a velocidade do carro: "))

if velocidade <= LIMITE:
    print("Velocidade permitida!!")
else:
    print("Velocidade acima da permitida! Multa à pagar no valor de R$ {:.2f}".format(VALOR_KM*(velocidade-LIMITE)))