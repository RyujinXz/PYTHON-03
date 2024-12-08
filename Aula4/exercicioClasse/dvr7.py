class Tarefa:
    def __init__(self, descricao: str, status="Pendente"):
        self.desc = descricao
        self.stat = status
    
    def mudarStatus(self):
        self.stat = "Concluída"
    
    def __str__(self):
        return (
            "\n"
            "==========INFORMAÇÕES==========\n"
            f"📋 Tarefa: {self.desc}\n"
            f"🔄 Status: {self.stat}\n"
            "===============================\n"
    )

#Exemplo
tarefa = Tarefa("Estudar Python")
print(tarefa)
tarefa.mudarStatus()
print(tarefa)