grupo = []
estoque = [{"Pacotinhos" : 50},
           {"AlbumM" : 15}, #Capa Mole
           {"AlbumD" : 22}, #Capa Dura
           {"AlbumPD" : 10}] #Premium Deluxe
album = 150
valor = 7.50

#Funções |
def comprar_figurinhas():
    while True:
        if estoque[0]["Pacotinhos"] > 0:
            print (f"Cada pacotinho custa: {valor}R$ | Contém 10 unidades.")
            qtd = int(input("Quantos pacotinhos você deseja? (Caso tenha mudado de ideia digite 0): "))
            if qtd > 0 and qtd <= estoque[0]["Pacotinhos"]:
                print (f"{qtd} Pacotinhos comprados.")
                estoque[0]["Pacotinhos"] = estoque[0]["Pacotinhos"] - qtd
                break
            elif qtd <= 0:
                print ("Compra cancelada. Caso tenha sido um erro de digitação tente novamente.")
                break
            elif qtd > 0 and qtd > estoque[0]["Pacotinhos"]:
                print ("Quantidade excede o estoque. Tente novamente.")
        elif estoque[0]["Pacotinhos"] == 0:
            print ("O estoque acabou! Avisaremos no grupo quando novos pacotinhos estiverem disponíveis.")
            break
def comprar_album():
    print ("comprar album")
def entrar_grupo():
    nome = input("Nome completo do usuário: ")
    numero = input("Numero do usuario: ")
    grupo.append({
        "Nome" : nome,
        "Numero" : numero
    })
    print ("Obrigado pelas informações! Você será adicionado ao grupo de figurinhas do whatsapp em breve.")
    for pessoa in grupo:
        if pessoa["Nome"] == nome:
            for nome,numero in pessoa.items():
                print (f"{nome}: {numero}")
    print (f"Já temos {len(grupo)} pessoa(s) no grupo!")

#Programa Principal |
while True:
        print ('''Bem vindo a loja de vendas de figurinhas da copa. Escolha uma das opções abaixo:
1 - Comprar pacotes de figurinhas
2 - Comprar álbum
3 - Entrar no grupo de troca de figurinhas
4 - Sair do programa''')
        opcao = int(input("Escolha uma opção: "))

#Estrutura de seleção: Match Case / If-Elif |
        match opcao:
            case 1:
                comprar_figurinhas()
            case 2:
                comprar_album()
            case 3:
                entrar_grupo()
            case 4:
                print("Obrigado pela compra! Até a próxima.")
                break
            case 5:
                estoque[0]["Pacotinhos"] = estoque[0]["Pacotinhos"] + 50
                print ("Pacotinhos adicionados ao estoque!")