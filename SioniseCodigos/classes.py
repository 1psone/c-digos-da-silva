class Aluno:
    #Método Construtor
    def __init__ (self, nome_aluno, ano_letivo, turma, matricula, idade, sexo, cpf, rg, email, tel):
        #Atributos (caracteristicas da classe/objeto)
        self.nome = nome_aluno
        self.ano = ano_letivo
        self.turma = turma
        self.matricula = matricula
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.tel = tel

class Professor:
    #Método Construtor
    def __init__ (self, nome_prof, lattes, formacao, turno, idade, sexo, cpf, rg, email, tel):
        #Atributos (caracteristicas da classe/objeto)
        self.nome = nome_prof
        self.area = formacao
        self.lattes = lattes
        self.turno = turno
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.tel = tel

def visualizarboletim (self):
    pass

class Televisao:
    def __init__ (self, marca, polegadas, resolucao):
        self.marca = marca
        self.polegadas = polegadas
        self.resolucao = resolucao

class Carro:
    def __init__ (self, marca, tipo, km_rodado):
        self.marca = marca
        self.tipo = tipo
        self.km = km_rodado

class Filme:
    def __init__ (self, nome_filme, diretor, data_lancamento):
        self.nome = nome_filme
        self.diretor = diretor
        self.data = data_lancamento

class Usuario:
    def __init__ (self, cpf, email, idade):
        self.cpf = cpf
        self.email = email
        self.idade = idade

class Bicicleta:
    def __init__ (self, cor, modelo, estado):
        self.cor = cor
        self.modelo = modelo
        self.estado = estado

class ContaBancaria:
    def __init__ (self, banco, dinheiro, divida):
        self.banco = banco
        self.dinheiro = dinheiro
        self.divida = divida

class Livro:
    def __init__ (self, autor, genero, paginas):
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

class Tabu:
    def __init__ (self, sabor, preco, quantidade):
        self.sabor = sabor
        self.preco = preco
        self.quantidade = quantidade

class Jogo:
    def __init__ (self, nome_jogo, genero, empresa):
        self.nome = nome_jogo
        self.genero = genero
        self.empresa = empresa

class Pokemon:
    def __init__ (self, nome_pokemon, pokedex, tipagem):
        self.nome = nome_pokemon
        self.pokedex = pokedex
        self.tipo = tipagem