#registrar a classificação do campeonato
CLUBE = input ("digite o clube:")
POSIÇÃO = int(input("digite a posição:"))

if POSIÇÃO == 1:
    print("campeão")
elif POSIÇÃO > 1 and POSIÇÃO <= 6:
    print("libertadores!")
elif POSIÇÃO >= 7 and POSIÇÃO <= 12:
    print("sul-americana.")
elif POSIÇÃO >= 17:
    print("rebaixado...")
else:
    print("não se dizer...")
