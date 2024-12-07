class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque 
    
    def vender(self, qtd: int):
        if (self.estoque > 0) and (qtd <= self.estoque):
            self.estoque -= qtd
            print(
                "\n"
                f"🛒 Foi comprado {qtd} {self.nome}'s\n"
                f"📦 Resta no estoque: {self.estoque} {self.nome}'s\n"
                "\n"
            )
        elif (self.estoque > 0) and (qtd > self.estoque):
            print(
                "\n"
                "⚠️ O pedido de itens é maior que a do estoque.\n"
                f"✔️ Foram vendidos {self.estoque} do estoque.\n"
                "\n"
                )
            self.estoque = 0
        else:
            print(
                "\n"
                "❌ Sem estoque deste produto!"
                "\n"
            )

    def repor(self, qtd:int):
        self.estoque += qtd
        print(
            "\n"
            f"📥 Foi reposto {qtd} {self.nome}'s\n"
            f"📦 Estoque atual: {self.estoque} {self.nome}'s \n"
            "\n"
        )
    def __str__(self):
        return (
            "\n"
            "==========INFORMAÇÕES==========\n"
            "🏷️ " f" Produto: {self.nome}\n"
            "💲 " f"Valor: R$ {self.preco}\n"
            "📦 " f"Estoque: R$ {self.estoque}\n"
            "===============================\n"
            )
    
p1 = Produto("Nike", 300, 5)
print(p1)
p1.vender(3)
p1.repor(3)
p1.vender(5)
p1.vender(1)
p1.repor(3)
p1.vender(4)
print(p1)