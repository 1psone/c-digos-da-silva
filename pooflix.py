#netflix de pobre:

#classe dos filmes
class Filmes():
    def __init__ (self, nome, anolancamento, diretor, genero, duracao):
        self.nome = nome
        self.anolancamento = anolancamento
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao

    #metodos "class Filmes()"
    def ExibirFilme(self):
        print (f'''-------FILME: {self.nome}-------
            Data de Lançamento: {self.anolancamento}
            Diretor/Criador: {self.diretor}
            Genero: {self.genero}
            Duração: {self.duracao}
            -----------------------------------
            ''')

#classe das series
class Series():
    def __init__(self, nome, anolancamento, diretor, genero, temporadas, quantiaepisodios):
        self.nome = nome
        self.anolancamento = anolancamento
        self.diretor = diretor
        self.genero = genero
        self.temporadas = temporadas
        self.quantiaepisodios = quantiaepisodios

#metodos "class Series()"
    def ExibirSerie(self):
        print (f'''-------SERIE: {self.nome}-------
Data de Lançamento: {self.anolancamento}
Diretor/Criador: {self.diretor}
Genero: {self.genero}
Temporadas: {self.temporadas}
Quantidade de Episódios: {self.quantiaepisodios}
-----------------------------------
''')

class Usuario():
    def __init__(self, usuario, nome, idade, email, senha, local):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha
        self.local = local

#metodos "class Usuario()"
    def Login(self):
        mail = "..."
        while mail != self.email:
            mail = input("Insira seu email: ")
            if mail != self.email:
                print ("Email incorreto. (Talvez você tenha digitado errado?)")
            else:
                print ("Email correto!")
        password = "..."
        while password != self.senha:
            password = input("Digite sua senha: ")
            if password != self.senha:
                print ("Senha incorreta. (Talvez você tenha digitado errado?)")
            else:
                print ("Senha correta!")
        print ("Bem vindo de volta.")

#instanciando
#Filmes (3):
filme1 = Filmes("Exterminador do Futuro", 1984, "James Cameron", "Ficção Cientifica", 1.47)
filme2 = Filmes("Obsession", 2025, "Curry Barker", "Terror", 1.49)
filme3 = Filmes("O Espetacular Homem-Aranha 2", 2014,"Marc Webb", "Ação", 2.22)

#Series (3):
serie1 = Series("Tengen Toppa Gurren Lagann", 2007, "Kazuki Nakashima", "Anime", 1, 27)
serie2 = Series("Cowboy Bebop", 2001, "Shin'ichirō Watanabe", "Anime", 1, 26)
serie3 = Series("Cyberpunk: Edgerunners", 2022, "Rafal Jaki", "Anime", 1, 10)

#Usuarios (3):
usuario1 = Usuario("Alice", "alicita", 16, "alicealvespimentel@gmail.com", "Alicezitita123", "Palmares")
usuario2 = Usuario("Luana", "luanita", 17, "luanagabrielapereira@gmail.com", "Luanitita123", "Palmares")
usuario3 = Usuario("Luis", "luisito", 16, "luispedromedeiros@gmail.com", "Luisitito123", "Ribeirão")

#atribuição de valores
filme1.ExibirFilme()
serie3.ExibirSerie()