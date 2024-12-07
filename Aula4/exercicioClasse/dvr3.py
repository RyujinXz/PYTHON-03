class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor 
    
    def __str__(self):
        return (
            "\n"
            "==========INFORMAÇÕES==========\n"
            f"📖 Título da Obra: {self.titulo}\n"
            f"✍️  Autor: {self.autor}\n"
            "===============================\n"
            "\n"
        )
    
l1 = Livro("Sherlock Holmes", "Arthur Conan Doyle")
print(l1)