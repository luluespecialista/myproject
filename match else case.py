#Demonstração do uso da condicional match/case...

print("digite número referente ao estado da moeda:")
print("1. flor de cunho")
print("2. soberba")
print("3. muito bem conservada")
print("4. bem conservada")
print("5. Outros estados")
ESTADO = int(input())

match ESTADO:
    case 1:
        print("perfeita! vou pagar R$ 1.000.000,00!")
    case 2:
        print("Quase perfeita! Ofereço R$ 250.000,00!")
    case 3:
        print("Que ótimo! posso dar uns R$ 100.000,00!")
    case 4:
        print("Que bom! aceitaria  R$ 30.000,00?")
    case 5:
        print("Desculpe, não aceito neste estado.")
    case _:
        print("Opção não reconhecida!")



    

        



