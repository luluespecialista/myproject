#demonstração de estrutura repetitiva...
CONTADOR = 0; senha = ""
while senha != "s3nh4" :
    print("digite a senha:")
    senha = input()
    if senha == "s3nh4":
        print("senha correta!")
        break
    else:
        print("senha errada...")
    CONTADOR += 1
    if CONTADOR == 3:
        print("3 tentativas excedidas")
        break