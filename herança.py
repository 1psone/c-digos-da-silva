#SuperClasse;
class Pessoa:
    #Método Construtor "class Pessoa";
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Método "class Pessoa:";
    def exibir_dados(self):
        print ("-----")
        print(f"Nome: {self.nome}")
        print (f"Idade: {self.idade}")

#ClasseFilha;
class Professor(Pessoa):
    pass
class Aluno(Pessoa):
    pass
class TAE(Pessoa):
    pass

#Instancias "class Pessoa";
p1 = Pessoa("Luana", 17)
p2 = Pessoa("Alice", 16)
p3 = Pessoa("Luis", 16)

#Instancias "class Professor";
prof1 = Professor("Sionise", 42)
prof2 = Professor("Josiel", 49)

#Instancias "class Aluno";
aluno1 = Aluno("Paulo Ruan", 17)
aluno2 = Aluno("Djalma", 17)

#Instancias "class TAE";
tae1 = TAE("Lucas", 31)
tae2 = TAE("Rosa", 934)

#Chamada Métodos (Pessoas);
p1.exibir_dados()
p2.exibir_dados()
p3.exibir_dados()

#Chamada Métodos (Professores);
prof1.exibir_dados()
prof2.exibir_dados()

#Chamada Métodos (Alunos);
aluno1.exibir_dados()

#Chamada Métodos (TAE's);
tae1.exibir_dados()
tae2.exibir_dados()