import random

num_casa = random.randint(1, 10)
print("Estou pensando num número de 1 a 10, tente adivinhar qual é esse número")

num_player = int(input("Digite o seu número: "))

if num_player == num_casa:
    print(("Parabéns, você adivinhou, eu estava pensando no número {}".format(num_player)))
else:
    print("Infelizmente você errou... Eu estava pensando no número {}".format(num_casa))