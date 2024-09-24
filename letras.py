#Demonstração do uso da condicional match/case...
print("digite número referente ao estado da moeda:")
print("A. flor de cunho")
print("B. soberba")
print("C. muito bem conservada")
print("D. bem conservada")
print("E. Outros estados")
ESTADO = input()

match ESTADO:
    case "A":
        print("perfeita! vou pagar R$ 1.000.000,00!")
    case "B":
        print("Quase perfeita! Ofereço R$ 250.000,00!")
    case "C":
        print("Que ótimo! posso dar uns R$ 100.000,00!")
    case "D":
        print("Que bom! aceitaria  R$ 30.000,00?")
    case "E":
        print("Desculpe, não aceito neste estado.")
    case _:
        print("Opção não reconhecida!")

