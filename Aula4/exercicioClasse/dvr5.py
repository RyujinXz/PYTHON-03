class ItemEstoque:
    def __init__(self, nome:str, qtd: int, precoUnitario: float):
        self.nome = nome
        self.qtd = qtd 
        self.preco = precoUnitario
    
    def adicionarEstoque(self, adicionando: int):
        if adicionando < 0:
            print(
                "\n"
                "❌ Não é possível adicionar uma quantidade negativa ao estoque!"
                "\n")
            return
        self.qtd += adicionando
        print(
            "\n"
            f"📥 Foi adicionado {adicionando} {self.nome}(s)\n"
            f"📦 Estoque atual: {self.qtd} {self.nome}(s)\n"
            "\n"
        )

    def removerEstoque(self, removendo: int):
        if removendo < 0:
            print("\n❌ Não é possível remover uma quantidade negativa do estoque!\n")
            return
        if (self.qtd > 0) and (removendo <= self.qtd):
            self.qtd -= removendo
            print(
                "\n"
                f"🛒 Foram removidos {removendo} {self.nome}(s)\n"
                f"📦 Resta no estoque: {self.qtd} {self.nome}(s)\n"
                "\n"
            )
        elif (self.qtd > 0) and (removendo > self.qtd):
            print(
                "\n"
                "⚠️ O pedido de remoção é maior que a do estoque.\n"
                f"✔️ Foram removidos {self.qtd} {self.nome}'s do estoque.\n"
                "\n"
                )
            self.qtd = 0
        else:
            print(
                "\n"
                "❌ Sem estoque deste produto!"
                "\n"
            )
    
    def calcularTotal(self):
        return self.qtd * self.preco
    
    def __str__(self):
        return (
            "\n"
            "========== INFORMAÇÕES DO ESTOQUE ==========\n"
            f"📦 Produto: {self.nome}\n"
            f"📊 Quantidade: {self.qtd}\n"
            f"💰 Preço Unitário: R$ {self.preco:.2f}\n"
            f"💵 Valor Total em Estoque: R$ {self.calcularTotal():.2f}\n"
            "===========================================\n"
        )
    
item = ItemEstoque("Adidas SuperStar", 5, 500)
print(item)
item.removerEstoque(3)