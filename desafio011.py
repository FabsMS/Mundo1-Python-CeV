largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede também em metros: "))

area = largura * altura
qtd_litros = area / 2

print("Para pintar toda a área de {}m² da parede, serão necessários {} litros de tinta".format(area, qtd_litros))
