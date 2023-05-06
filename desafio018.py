from math import cos, sin, tan

ang = int(input("Digite o ângulo desejado: "))

print("Esse é o seno de {}: {:.2f}".format(ang, sin(ang)))
print("Esse é o cosseno de {}: {:.2f}".format(ang, cos(ang)))
print("Esse é a tangente de {}: {:.2f}".format(ang, tan(ang)))