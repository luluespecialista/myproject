#resgitrar o conteudo e a sua nota...
CONTEUDO = input("Qual o filme ou série preferido? ")
AVALIAÇÃO = int(input ("atribuir uma nota de 1 a 5:"))

#realizar  avaliação ...
match AVALIAÇÃO:
    case 1:
        print("péssimo!")
        PORQUE = input("descreva porque a avliação foi baixa: ")
    case 2:
        print("ruim!")
        PORQUE = input("descreva porque a avaliação foi baixa: ")
    case 3:
        print("razoável")
    case 4:
        print("bom")
    case 5:
        print("ótimo")
    
    case _:
        print("Opção não reconhecida!")

   
