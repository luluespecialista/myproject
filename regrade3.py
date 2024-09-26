# programas com três valores...
x = int(input("digite o valor de x:"))
y = int(input("digite o valor de y:"))
z = int(input("digite o valor de z:"))

if x < y and y < z:
    print("em ordem crescente!")
elif x > y and y > z:
     print("em ordem decrescente!")
else:
    print("todos misturados!")
    