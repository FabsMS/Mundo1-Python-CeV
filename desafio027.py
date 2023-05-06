nome = input("Digite o seu nome: ")

nomeSeparado = nome.split()

primeiroNome = nomeSeparado[0]
ultimoNome = nomeSeparado[-1]

print("Primeiro nome = {}".format(primeiroNome))
print("Último nome = {}".format(ultimoNome))