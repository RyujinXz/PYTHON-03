class Carrinho:
    def __init__(self):
        self.itens = []


    def adicionar_produto(self, nome, preco):
        self.itens.append({"nome": nome, "preco": preco})


    def exibir_itens(self):
        for item in self.itens:
            print(f"Produto: {item['nome']}, Preço: R${item['preco']:.2f}")


    def calcular_total(self):
        return sum(item['preco'] for item in self.itens)


# Exemplo de uso
carrinho = Carrinho()
carrinho.adicionar_produto("Camiseta", 29.90)
carrinho.adicionar_produto("Calça", 89.90)
carrinho.exibir_itens()
print(f"Total: R${carrinho.calcular_total():.2f}")
