#solução de programa de avaliação...
EXECUÇÃO = input("olá! o serviço foi executado (s/n)")

if EXECUÇÃO == "s" :
    print("digite a sua avaliação (1 a 5):")
    print("1. péssimo / 2.ruim / 3 razoável / 4.bom / 5. ótimo")
    NOTA = int(input())
elif EXECUÇÃO == "n" :
    
    AVALIAÇÃO = input("descreva o que aconteceu de errado:")
else:
    print("opção inválida!")
print("obrigo por avaliar os nossos serviços!")