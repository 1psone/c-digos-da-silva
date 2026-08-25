#Programa que leia três números e, em seguida deixe o usuário escolher entre:
#1 - Somar os números
#2 - Ordem crescente
#3 - Verificar pares e impares
#4 - Dobro e metade dos números
dobro = []
metade = []
impar = []
par = []
num = []

#soma
def somar():
    soma = num[0] + num[1] + num[2]
    print (f"A soma dos números é igual a: {soma}")

#crescente
def crescente():
    num.sort()
    print (num)

#par e impar
def par_impar():
    x = 0
    while len(par) + len(impar) < 3:
        if num[x] % 2 == 0:
            par.append(num[x])
        else:
            impar.append(num[x])
        x = x + 1
    print (f"Números pares: {par} | Números impares: {impar}")

#dobro e metade
def dobro_metade():
    x = 0
    while len(dobro) < 3 and len(metade) < 3:
        dobrado = num[x] * 2
        meio = num[x] / 2
        dobro.append(dobrado)
        metade.append(meio)
        x = x + 1
    print (f"Números dobrados: {dobro} | Números meiados: {metade}")


#Estrutura de repetição: Escolha dos números
while len(num) < 3:
    escolha = int(input("Escolha um número inteiro: "))
    num.append(escolha)

#Programa Principal |
while True:
        print ('''Com os três números escolhidos, terá as seguintes opções:
1 - Somar os 3 números
2 - Colocar os 3 números em ordem crescente
3 - Verificar quais são pares e quais são impares
4 - Ver o dobro dos números e a metade dos números
5 - Sair''')
        opc = int(input("Agora que escolheu os números, o que quer fazer? [1/2/3/4/5]: "))
    #Estrutura de seleção: Match Case / If-Elif |
        match opc:
            case 1:
                somar()
            case 2:
                crescente()
            case 3:
                par_impar()
            case 4:
                dobro_metade()
            case 5:
                print ("Ok! Até mais.")
                break