#solução do eclipse solar...
HORA = input("qual a hora da chegada?")
ESTADO = input("qual é o estado(RJ/SP/MG/ES)?")
DIA = input("o dia está claro (S/N)?")

if HORA == "15:25h" and ESTADO  == "RJ" and DIA == "S":
    print(" eclipse total!")
elif HORA > "15:20h" and HORA > "13:30h":
    if ESTADO == "RJ" or ESTADO == "SP" or ESTADO == "MG" or ESTADO  == "ES":
        if DIA == "S" :
            print ("eclipse parcial!")
else:
    print ("não deu pra vê o eclipse...")