import random
import time
ht1 = []
ht2 = []
rodada = 0
plfinal = 0
plfinal1 = 0
pontot1 = 0
pontot2 = 0
t1l = 0
t2l = 0
print ("--------------------------------")
print ("Bem vindo ao SDJDVDS.C (SimuladordeJogodeVoleidaSilva.com)")
t1 = input("Nome do time 1: ").strip()
t2 = input("Nome do time 2: ").strip()
print ("--------------------------------")
l = [t1,t2]
while True:
    if pontot1 > 23 and pontot2 > 23:
        pro = random.choice(l)
        print ("Esperando algum time pontuar...")
        time.sleep(2)
        if pro == t1:
            print (f"O time '{t1}' pontuou!")
            pontot1 = pontot1 + 1
            print ("--------------------------------")
            print (f"Placar: {pontot1} x {pontot2}")
            if pontot1 == pontot2 + 2:
                plfinal = pontot1
                plfinal1 = pontot2
                print (f"O jogo acabou, {t1} ganhou!")
                print ("--------------------------------")
                print (f"Esse foi o histórico de pontos do {t1}: ")
                print (*ht1)
                print ("--------------------------------")
                print (f"E esse foi o histórico de pontos do {t2}: ")
                print (*ht2)
                print ("--------------------------------")
                print (f"O placar final foi de {plfinal} x {plfinal1}!")
                print ("--------------------------------")
                print (f"O {t1} liderou o placar {t1l} vezes!")
                print ("--------------------------------")
                print (f"Já o {t2} liderou o placar {t2l} vezes!")
                print ("--------------------------------")
                break
            rodada = rodada + 1
            ht1.append(f"rodada {rodada}")
        if pro == t2:
            print (f"O time '{t2}' pontuou!")
            pontot2 = pontot2 + 1
            print ("--------------------------------")
            print (f"Placar: {pontot1} x {pontot2}")
            if pontot2 == pontot1 + 2:
                plfinal = pontot1
                plfinal1 = pontot2
                print (f"O jogo acabou, {t2} ganhou!")
                print ("--------------------------------")
                print (f"Esse foi o histórico de pontos do {t1}: ")
                print (*ht1)
                print ("--------------------------------")
                print (f"E esse foi o histórico de pontos do {t2}: ")
                print (*ht2)
                print ("--------------------------------")
                print (f"O placar final foi de {plfinal} x {plfinal1}!")
                print ("--------------------------------")
                print (f"O {t1} liderou o placar {t1l} vezes!")
                print ("--------------------------------")
                print (f"Já o {t2} liderou o placar {t2l} vezes!")
                print ("--------------------------------")
            rodada = rodada + 1
            ht2.append(f"rodada {rodada}")
    elif pontot1 <= 25 and pontot2 <= 25:
        x = random.choice (l)
        print ("Esperando algum time pontuar...")
        time.sleep(2)
        if x == t1:
            print (f"O time '{t1}' pontuou!")
            pontot1 = pontot1 + 1
            print ("--------------------------------")
            print (f"Placar: {pontot1} x {pontot2}")
            if pontot1 > pontot2:
                t1l = t1l + 1
            if pontot1 >= 25 and pontot2 <= 23:
                plfinal = pontot1
                plfinal1 = pontot2
                print (f"O jogo acabou, {t1} ganhou!")
                print ("--------------------------------")
                print (f"Esse foi o histórico de pontos do {t1}: ")
                print (*ht1)
                print ("--------------------------------")
                print (f"E esse foi o histórico de pontos do {t2}: ")
                print (*ht2)
                print ("--------------------------------")
                print (f"O placar final foi de {plfinal} x {plfinal1}!")
                print ("--------------------------------")
                print (f"O {t1} liderou o placar {t1l} vezes!")
                print ("--------------------------------")
                print (f"Já o {t2} liderou o placar {t2l} vezes!")
                print ("--------------------------------")
                break
            rodada = rodada + 1
            ht1.append(f"rodada {rodada}")
        if x == t2:
            print (f"O time '{t2}' pontuou!")
            print ("--------------------------------")
            pontot2 = pontot2 + 1
            print (f"Placar: {pontot1} x {pontot2}")
            if pontot2 > pontot1:
                t2l = t2l + 1
            if pontot2 >= 25 and pontot1 <= 23:
                plfinal = pontot1
                plfinal1 = pontot2
                print (f"O jogo acabou, {t2} ganhou!")
                print ("--------------------------------")
                print (f"Esse foi o histórico de pontos do {t1}: ")
                print (*ht1)
                print ("--------------------------------")
                print (f"E esse foi o histórico de pontos do {t2}: ")
                print (*ht2)
                print ("--------------------------------")
                print (f"O placar final foi de {plfinal} x {plfinal1}!")
                print ("--------------------------------")
                print (f"O {t1} liderou o placar {t1l} vezes!")
                print ("--------------------------------")
                print (f"Já o {t2} liderou o placar {t2l} vezes!")
                print ("--------------------------------")
                break
            rodada = rodada + 1
            ht2.append(f"rodada {rodada}")