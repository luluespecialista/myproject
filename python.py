# demonstração de operadores lógicos em condicionais...
print("o que você vai fazer amanhã de manhã?")
print("dormi/ estudar/Planejar")
MANHA = input()
print("o que você vai fazer amanhã de tarde")
print("jogar/treinar/trabalhar")
TARDE = input ()

if not MANHA or not TARDE == "jogar":
    print("você precisa dizer o que vai fazer !")
else:
    if MANHA == "dormi" or TARDE == "jogar":
        print("você está desperdiçando o seu dia!")
    elif  MANHA == "estudar" or TARDE == "treinar":
        print("que bom você irá se aperfeiçoar!")
    elif MANHA == "planejar" and TARDE == "trabalhar" :
        print("para trabalhar melhor devo planejar!")
    else:
        print("não combinamos essas ações...")

        print("tenha um  bom dia!")


     