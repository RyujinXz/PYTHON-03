class Animal:
    def __init__(self, nome: str, faz: str):
        self.nome = nome
        self.faz = faz


class Cachorro(Animal):
    def som(self):
        return "Au au!"


class Gato(Animal):
    def som(self):
        return "Miau!"


dog = Cachorro("Rex", "faz")
cat = Gato("Felix", "faz")
print(dog.nome, dog.faz, dog.som())  # Saída: Rex faz Au au!
print(cat.nome, cat.faz, cat.som())  # Saída: Felix faz Miau!