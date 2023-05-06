nome = input("Digite o nome desejado: ")

findSilva = nome.upper().find("SILVA")

if findSilva != -1:
    print("Esse nome tem 'Silva'")
else:
    print("Esse nome não tem 'Silva'")
