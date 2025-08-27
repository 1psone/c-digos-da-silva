plivros = []
print ("-------------------")
print ("Local para devolver livros emprestados:")
print ("Aqui você pode:")
print ("D = Devolver um livro | P = Pegar um livro da pilha | S = Sair")
print ("Max Livros = 3")
print ("-------------------")
while True:
    opc = input("O que quer fazer: ").strip().lower()
    if opc == "d":
        if len(plivros) == 3:
            print ("Você já possuí o maximo de livros empilhados!")
            print ("-------------------")
            continue
        dlivro = input("Nome do livro que quer devolver: ")
        plivros.append(dlivro)
        print (f"Livros atuais: {plivros}")
        print ("-------------------")
    elif opc == "p":
        if len(plivros) == 0:
            print ("Você não tem livros para pegar!")
            print ("-------------------")
            continue
        livro = plivros.pop()
        print (f"Livro {livro} retirado!")
        print (f"Livros atuais: {plivros}")
        print ("-------------------")
    elif opc == "s":
        print ("Verificando se ainda há livros na pilha...")
        if len(plivros) > 0:
            ctz = input("Ainda há livros restantes! Deseja continuar ou sair? (S/C): ").strip().lower()
            print ("-------------------")
            if ctz == "s":
                print ("Saindo...")
                print ("-------------------")
                break
            if ctz == "c":
                print ("Continuando...")
                print ("-------------------")
                continue
        if len(plivros) == 0:
            print ("Saindo...")
            print ("-------------------")
            break