city = input("Digite o nome da cidade desejada: ")

primNome = city.upper().split()

if primNome[0] == "SANTO":
    print("O primeiro nome dessa cidade é Santo")
else:
    print("O primeiro nome dessa cidade não é Santo")