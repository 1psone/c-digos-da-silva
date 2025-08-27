# PT-BR Ver.
# lista = lista dos livros em estoque
# la = livros-adicionados
# lv = livros-vendidos
# le = livros-em-estoque
# print ("----------------------") = divisor (apenas para a decoração)
import time
lista = []
la = 0
lv = 0
le = 0
print ("----------------------")
print ("Bem vindo ao EGESPP! - Estoque Gilleade Esdras da Silva Pereira Pinto")
print ("O que deseja fazer? Suas opções são:")
print ("Adicionar um Livro (A)")
print ("Vender um Livro (V)")
print ("Listar os Livros Atuais (L)")
print ("Sair do EGDSPP (S)")
print ("----------------------")
while True:
    oq = input("O que deseja fazer? (A | V | L | S): ").strip().lower()
    if oq == "a":
        al = input("Livro que deseja adicionar: ").strip()
        print (f"Livro '{al}' adicionado com sucesso!")
        lista.append(al)
        la = la + 1
        le = le + 1
        print ("----------------------")
    if oq == "v":
        vl = input("Livro que deseja vender: ").strip()
        lista.remove(vl)
        if ValueError == True:
            print ("Livro inválido... Tente novamente.")
            continue
        lv = lv + 1
        le = le - 1
        print ("----------------------")
    if oq == "l":
        print (f"Muito bem! seus livros atuais são:")
        print (lista)
        print ("----------------------")
    if oq == "s":
        print ("Dia bem produtivo, não? Carregando seus resultados...")
        time.sleep(1)
        print (f"Quantidade de livros adicionados: {la}")
        time.sleep(1)
        print (f"Quantidade de livros vendidos: {lv}")
        time.sleep(1)
        print (f"Quantidade de livros ainda no estoque: {le}")
        time.sleep(1)
        print ("----------------------")
        time.sleep(1)
        print ("Verificando se há livros restantes...")
        time.sleep(1)
        if le > 0:
            ctz = input("Tem certeza que quer fechar? Ainda tem livros restantes. (S/N): ").strip().lower()
            if ctz == "s":
                print ("Fechando Estoque...")
                print ("----------------------")
                time.sleep(2)
                print ("Estoque fechado!")
                break
            if ctz == "n":
                print ("Cancelando...")
                print ("----------------------")
                time.sleep(2)
                print ("Estoque aberto!")
                continue
        if le <= 0:
            print ("Fechando Estoque...")
            print ("----------------------")
            break

#ENG Ver.
# lista = list of books in stock
# la = books added
# lv = books sold
# le = books in stock
# print ("----------------------") = text divider (only for decoration)
import time
lista = []
la = 0
lv = 0
le = 0
print ("----------------------")
print ("Welcome to SGESPP! - Stock Gilleade Esdras da Silva Pereira Pinto")
print ("What do you want to do? Your options are:")
print ("Add a book (A)")
print ("Sell a book (S)")
print ("List the books in stock (L)")
print ("Leave EGDSPP (LE)")
print ("----------------------")
while True:
    oq = input("What do you want to do? (A | S | L | LE): ").strip().lower()
    if oq == "a":
        al = input("Book that you want to add: ").strip()
        print (f"Book '{al}' added sucessfully!")
        lista.append(al)
        la = la + 1
        le = le + 1
        print ("----------------------")
    if oq == "s":
        vl = input("Book that you want to sell: ").strip()
        lista.remove(vl)
        if ValueError == True:
            print ("Invalid book. Try again.")
            continue
        lv = lv + 1
        le = le - 1
        print ("----------------------")
    if oq == "l":
        print (f"Ok! The books in your stock right now are:")
        print (lista)
        print ("----------------------")
    if oq == "le":
        print ("Productive day, huh? Loading your results...")
        time.sleep(1)
        print (f"Quantity of books added: {la}")
        time.sleep(1)
        print (f"Quantity of books sold: {lv}")
        time.sleep(1)
        print (f"Quantity of books still in stock: {le}")
        time.sleep(1)
        print ("----------------------")
        time.sleep(1)
        print ("Verifying if you still have books in stock...")
        time.sleep(1)
        if le > 0:
            ctz = input("Are you sure you wanna leave? There are still books in stock. (Y/N): ").strip().lower()
            if ctz == "y":
                print ("Closing stock...")
                print ("----------------------")
                time.sleep(2)
                print ("Stock closed!")
                break
            if ctz == "n":
                print ("Cancelling...")
                print ("----------------------")
                time.sleep(2)
                print ("Stock re-opened!")
                continue
        if le <= 0:
            print ("Closing stock...")
            time.sleep(1)
            print ("----------------------")
            time.sleep(1)
            print ("Stock closed!")
            break