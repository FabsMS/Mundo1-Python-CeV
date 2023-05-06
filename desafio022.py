nome = input("Digite o seu nome: ")

nomeMaisculo = nome.upper()
nomeMinusculo = nome.lower()
qtdLetras = nome.replace(" ", "")
qtdLetrasPrimeiroNome = nome.split()

print(nomeMaisculo)
print(nomeMinusculo)
print(len(qtdLetras))
print(len(qtdLetrasPrimeiroNome[0]))