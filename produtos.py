class Produtos():
    def __init__ (self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

#metodos da classe
    def vender(self):
        pass

    def exibir(self):
        print (f"Nome do Produto: {self.nome}")
        print (f"Preço: {self.preco}R$")
        print (f"Quantidade: {self.quantidade}")

#instanciar
produto1 = Produtos ("Dudu", 2.50, 10) #Produto criado
produto2 = Produtos ("Açaí", 13, 5)
produto3 = Produtos ("Picolé", 1.50, 100)

#atribuindo valores ao objeto
produto2.nome = "Dida"
produto2.preco = 17
produto2.exibir()