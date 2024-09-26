# Solicita ao usuário que insira um número
try:
    numero = int(input("Digite um número para ver sua tabuada: "))

    # Exibe um cabeçalho
    print(f"\nTabuada do {numero}:\n")
    print("-" * 20)  # Linha de separação

    # Gera e exibe a tabuada
    for i in range(1, 11):  # De 1 a 10
        resultado = numero * i
        print(f"{numero:2} x {i:2} = {resultado:3}")

    print("-" * 20)  # Linha de separação

except ValueError:
    print("Por favor, insira um número inteiro válido.")