# PT-BR Ver.
# lista = Guarda os resultados de todas as suas operações
# print ("----------------------") = divisor (apenas para a decoração)
#Calculadora
print ("Essa é uma calculadora das 4 operações básicas.")
print ("Som, Sub, Div, Mult")
print ("----------------------")
lista = []
while True:
    x = input("Qual operação você deseja realizar: ").lower()
    print ("----------------------")
    if x == "som":
        som = float(input("Escolha o primeiro número da soma: "))
        som1 = float(input("Escolha o segundo número da soma: "))
        print ("----------------------")
        resul = som + som1
        print (f"O resultado da sua soma é: {resul}")
        print ("----------------------")
        lista.append(resul)
    if x == "sub":
        sub = float(input("Escolha o primeiro número da subtração: "))
        sub1 = float(input("Escolha o segundo número da subtração: "))
        print ("----------------------")
        resul1 = sub - sub1
        print (f"O resultado da sua subtração é: {resul1}")
        print ("----------------------")
        lista.append(resul1)
    if x == "div":
        div = float(input("Escolha o primeiro número da divisão: "))
        if div == 0:
            print ("Não se divide por 0, deixe de ser burro!")
            continue
        div1 = float(input("Escolha o segundo número da divisão: "))
        if div1 == 0:
            print ("Não se divide por 0, deixe de ser burro!")
            continue
        print ("----------------------")
        resul2 = div/div1
        print(f"O resultado da sua divisão: {resul2}")
        print ("----------------------")
        lista.append(resul2)
    if x == "mult":
        mult = float(input("Escolha o primeiro número da multiplicação: "))
        mult1 = float(input("Escolha o segundo número da multiplicação:"))
        print ("----------------------")
        resul3 = mult * mult1
        print (f"O resultado da sua multiplicação é: {resul3}")
        print ("----------------------")
        lista.append(resul3)
    cont = input("Deseja continuar? Digite (S/N): ").lower().strip()
    print ("----------------------")
    if cont == "s":
        continue
    if cont == "n":
        print (f"O(s) resultado(s) total(is) é/são: {lista}")
        break

# ENG Ver.
# lista = Keeps all the results of your operations
# print ("----------------------") = divider (only for decoration)
#Calculator
print ("----------------------")
print ("This is a calculator that contemplates all the 4 basic operations")
print ("Sum, Sub, Div, Mult")
print ("----------------------")
lista = []
while True:
    x = input("Operation you want to execute: ").lower()
    print ("----------------------")
    if x == "som":
        som = float(input("Choose the first number of the sum: "))
        som1 = float(input("Choose the second number of the sum: "))
        print ("----------------------")
        resul = som + som1
        print (f"The result of the sum is: {resul}")
        print ("----------------------")
        lista.append(resul)
    if x == "sub":
        sub = float(input("Choose the first number of the subtraction: "))
        sub1 = float(input("Choose the second number of the subtraction: "))
        print ("----------------------")
        resul1 = sub - sub1
        print (f"The result of the subtraction is: {resul1}")
        print ("----------------------")
        lista.append(resul1)
    if x == "div":
        div = float(input("Choose the second number of the division: "))
        if div == 0:
            print ("You cant divide by 0!")
            continue
        div1 = float(input("Choose the second number of the division: "))
        if div1 == 0:
            print ("You cant divide by 0!")
            continue
        print ("----------------------")
        resul2 = div/div1
        print(f"The result of your divison is: {resul2}")
        print ("----------------------")
        lista.append(resul2)
    if x == "mult":
        mult = float(input("Choose the first number of the multiplication: "))
        mult1 = float(input("Choose the second number of the multiplication: "))
        print ("----------------------")
        resul3 = mult * mult1
        print (f"The result of your multiplication: {resul3}")
        print ("----------------------")
        lista.append(resul3)
    cont = input("Do you wish to continue? Digit (Y/N): ").lower().strip()
    print ("----------------------")
    if cont == "y":
        continue
    if cont == "n":
        print (f"The total result(s) is(are): {lista}")
        break