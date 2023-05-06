import random

listaAlunos = list()
seq = 1

for x in range(4):
    nome = input("Digite o nome do aluno: ")
    listaAlunos.append(nome)

for x in range(4):
    sorteado = random.choice(listaAlunos)
    print("O número {} na sequência de apresentação é o(a) aluno(a): {}".format(seq, sorteado))
    listaAlunos.remove(sorteado)
    seq += 1