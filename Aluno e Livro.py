alunos = []
plivros = []
print ("--------------------")
print ("Bem vindo a biblioteca")
print ("Adicione alunos na fila e atenda-os (MAX = 5)")
print ("Devolver livros e remova-os da pilha (MAX = 3)")
print ("--------------------")
print ("ED = Entrar na fila / Devolver um Livro | AP = Atender / Pegar um Livro da Pilha | S = Sair")
while True:
    opc = input("O que quer fazer? (ED/AP/S): ").lower().strip()
    if opc == "ed":
        x = input("Entrar ou Devolver? (E/D): ").lower().strip()
        if x == "e":
            opc = "e"
        elif x == "d":
            opc = "d"
    if opc == "ap":
        x = input("Atender ou Pegar um livro? (A/P): ").lower().strip()
        if x == "a":
            opc = "a"
        if x == "p":
            opc = "p"
    print ("--------------------")
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
    if opc == "e":
        if len(alunos) == 5:
            print ("Você já chegou no limite de alunos! Atenda ou saia!")
            continue
        adc = input("Nome do aluno que quer entrar na fila: ").strip()
        print (f"Muito bem! {adc} entrou na fila!")
        alunos.append(adc)
        print (f"Lista atual: {alunos}")
        print ("--------------------")
        continue
    elif opc == "a":
        if len(alunos) == 0:
            print ("Você não tem ninguém para atender! Adicione alguém e tente novamente!")
            continue
        print (f"Muito bem! {alunos[0]} foi atendido(a)!")
        alunos.pop(0)
        print (f"Lista atual: {alunos}")
        print ("--------------------")
        continue
    elif opc == "s":
        print ("Verificando se ainda tem alunos ou livros na fila...")
        if len(alunos) > 0 or len(plivros) > 0:
            ctz = input("Ainda tem alunos ou livros na fila!!! Tem certeza que quer sair? (S/N): ").strip().lower()
            print ("-------------------")
            if ctz == "s":
                print ("Fechando...")
                print ("-------------------")
                break
            if ctz == "n":
                print ("Cancelando...")
                print ("-------------------")
                continue
        if len(alunos) == 0:
            print ("Fechando...")
            print ("-------------------")
            break