alunos = []
print ("--------------------")
print ("Bem vindo a biblioteca")
print ("Adicione alunos na fila e atenda-os (MAX = 5)")
print ("--------------------")
print ("E = Entrar na fila | A = Atender | S = Sair")
while True:
    opc = input("O que quer fazer? (E/A/S): ").lower().strip()
    print ("--------------------")
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
        print ("Verificando se ainda tem alunos na fila...")
        if len(alunos) > 0:
            ctz = input("Ainda tem alunos na fila!!! Tem certeza que quer sair? (S/N): ").strip().lower()
            if ctz == "s":
                print ("Fechando...")
                break
            if ctz == "n":
                print ("Cancelando...")
                continue
        if len(alunos) == 0:
            print ("Fechando...")
            break