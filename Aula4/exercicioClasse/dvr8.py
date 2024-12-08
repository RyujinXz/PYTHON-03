from typing import List, Dict

class Carrinho:
    def __init__(self):
        self.produtos: List[Dict[str, float]] = []

    def adicionarProduto(self, nome: str, preco: float):
        produto = {"nome": nome, "preco": preco}
        self.produtos.append(produto)

    def exibirItens(self):
        
        print(
            "\n"
            "========== ITENS NO CARRINHO ==========\n")
        for produto in self.produtos:
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}\n")
        print("=======================================\n")

    def calcularTotal(self):
        return sum(produto['preco'] for produto in self.produtos)

#Testando Carrinho
tenis = Carrinho()
tenis.adicionarProduto("Adidas SuperStar", 500)
tenis.adicionarProduto("Nike Air Force One", 900)

tenis.exibirItens()
print(f"Total: R$ {tenis.calcularTotal():.2f}"
      "\n")