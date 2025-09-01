# Restaurante Legalzinho da Alice Alves Pimentel
pedidos = []
valor = 0
cac = ("lasanha", "pizza", "coxinha", "hamburguer", "salgado", "cimento", "conta")
cab = ("refrigerante", "suco", "chá", "água", "acido nucleico", "conta")
lasanha = 12
pizza = 11
coxinha = 6
hamburguer = 8
salgado = 7
cimento = 82
refrigerante = 6
suco = 8
chá = 7
água = 2
acido_nucleico = 137
print ("Garçom: Boa tarde! Seja bem vindo ao Restaurante Legalzinho da Alice Alves Pimentel, OU RLAAP para abreviar.")
print ("Garçom: Aqui está o cardápio, quando decidir o que quer pedir, pode me chamar!")
print ("Cardápio Comidas: Lasanha, Pizza, Coxinha, Hamburguer, Salgado, Cimento.")
print ("Lasanha - 12,00 R$ | Pizza - 11,00 R$ | Coxinha - 6,00 R$ | Hamburguer - 8,00 R$ | Salgado - 7,00 R$ | Cimento - 82,00 R$")
print ("Cardápio Bebidas: Refrigerante, Suco, Chá, Água, Acido Nucleico.")
print ("Refrigerante - 6,00 R$ | Suco - 8,00 R$ | Chá - 7,00 R$ | Água - 2,00 R$ | Acido Nucleico - 137,00 R$")
print ("Garçom: Se quiser pedir a conta, escreva 'conta'!")
while True:
    ped = input("Deseja pedir qual comida? (Ou deseja pedir a conta?): ").strip().lower()
    if ped in cac:
        if ped != "conta":
            print ("Garçom: Muito bem, o que você quer pedir?")
            print (f"Você: Eu quero um(a) {ped}!")
            print (f"Garçom: Certo! {ped} quentinho(a) saindo!")
            pedidos.append(ped)
            if ped == "lasanha":
                valor = valor + lasanha
            elif ped == "pizza":
                valor = valor + pizza
            elif ped == "coxinha":
                valor = valor + coxinha
            elif ped == "hamburguer":
                valor = valor + hamburguer
            elif ped == "salgado":
                valor = valor + salgado
            elif ped == "cimento":
                valor = valor + cimento
    elif ped not in cac and ped is not "conta":
        print ("Garçom: Talvez você tenha pedido errado.. Tente novamente!")
        continue
    if ped == "conta":
        print ("Você: Ó garçom! me traz a conta!")
        print ("Garçom: JÁ VAI!!!!!!")
        print ("Garçom: Certo, senhor! aqui está a sua conta:")
        print (f"Pedidos feitos: {pedidos} | Valor Total da Compra: {valor:5.2f}R$")
        print ("Garçom: Credito ou Debito?!")
        print ("Você: Nada! otário! *Procede a fugir do restaurante sem pagar nada*")
        print ("Continua...")
        break
    pedb = input("Garçom: Certo, agora que pediu uma comida, qual bebida você deseja?: ").strip().lower()
    if pedb in cab:
        if pedb != "conta":
            print (f"Você: Eu quero um(a) {pedb}.")
            print (f"Garçom: Certo! aqui está: *Entrega-te a bebida*")
            pedidos.append(pedb)
            if pedb == "refrigerante":
                valor = valor + refrigerante
            elif pedb == "suco":
                valor = valor + suco
            elif pedb == "chá":
                valor = valor + chá
            elif pedb == "água":
                valor = valor + água
            elif pedb == "acido nucleico":
                valor = valor + acido_nucleico
    if pedb not in cab:
        print ("Garçom: Talvez você tenha pedido errado.. Tente novamente!")
        continue
    elif pedb == "conta":
        print ("Você: Ó garçom! me traz a conta!")
        print ("Garçom: JÁ VAI!!!!!!")
        print ("Garçom: Certo, senhor! aqui está a sua conta:")
        print (f"Pedidos feitos: {pedidos} | Valor Total da Compra: {valor:5.2f}R$")
        print ("Garçom: Credito ou Debito?!")
        print ("Você: Nada! otário! *Procede a fugir do restaurante sem pagar nada*")
        print ("Continua...")
        break