PRECO_DIA = 60
PRECO_KM = 0.15

qtd_dias = int(input("Quantos dias o carro ficou alugado? "))
qtd_km = float(input("Quantos km foram percorridos? "))

preco_dias = qtd_dias * PRECO_DIA
preco_km = qtd_km * PRECO_KM

valor_total = preco_km + preco_dias

print("O valor total à pagar pelo carro alugado é de R${:.2f}".format(valor_total))
