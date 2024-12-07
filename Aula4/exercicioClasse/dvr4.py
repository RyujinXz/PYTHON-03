from typing import List

class Estudante:
    def __init__(self, nome: str, notas: List[float]):
        self.nome = nome
        self.notas = notas
    
    def calcularMedia(self):
        if not self.notas: 
            return 0
        return sum(self.notas) / len(self.notas)
    
    def statusAluno(self):
        media = self.calcularMedia()
        if media >= 6:
            status = "APROVADO"
        else:
            status = "REPROVADO"
        return media, status
    
    def exibirInformacoes(self):
        media, status = self.statusAluno()
        print(
             "\n"
            "========== INFORMAÇÕES ==========\n"
            f"📚 Aluno: {self.nome}\n"
            f"📊 Média: {media:.2f}\n"
            f"✅ Status: {status}\n"
            "=================================\n"
        )
    
e1 = Estudante("Matheus", [4.5, 5.5, 3.2])
e1.exibirInformacoes()