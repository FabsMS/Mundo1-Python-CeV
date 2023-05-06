frase = input("Digite a frase desejada: ")

qtdA = frase.lower().count('a')
primeiroA = frase.find('a')
ultimoA = frase.rfind('a')

print("Quantidade de aparições: {}". format(qtdA))
print("Index primeira aparição: {}". format(primeiroA))
print("Index última aparições: {}". format(ultimoA))