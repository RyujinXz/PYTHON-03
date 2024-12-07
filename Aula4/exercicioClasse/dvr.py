"""
Crie uma classe chamada Pessoa com os atributos nome e idade. Adicione um método chamado exibir_informacoes que exibe o nome e a idade da pessoa.
"""

class Pessoa():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def exibirInfo(self):
        print(
            "\n"
            "==========INFORMAÇÕES==========\n"
            f"🌟 Nome: {self.nome}\n"
            f"🎂 Idade: {self.idade}\n"
            "===============================\n"
    )

p1 = Pessoa("Samuel", 46)
p1.exibirInfo()