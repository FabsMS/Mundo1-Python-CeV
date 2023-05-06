import random

listaAlunos = list()

for x in range(4):
    nome = input("Digite o nome do aluno: ")
    listaAlunos.append(nome)

print("Aluno(a) sorteado(a) para apagar o quadro: {}".format(random.choice(listaAlunos)))