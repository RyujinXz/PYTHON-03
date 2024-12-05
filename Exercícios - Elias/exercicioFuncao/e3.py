alunos = []
def addAlunos(aluno):
    alunos.append(aluno)
def remAlunos(aluno):
    alunos.pop(aluno)
def exi():
    print(alunos)
while True:
    pergunta = input("Quer adicionar um aluno (sim/não): ")
    if (pergunta[0].lower() == "n"):
        break
    elif (pergunta[0].lower() == "s"):
        alunos.append(input("Digite o nome do aluno: "))
while True:
    print("-"*30) 
    pergunta2 = input("Quer remover um aluno (sim/não): ")
    print("-"*30)
    if (pergunta2[0].lower() == "n"):
        break
    elif (pergunta2[0].lower() == "s"):
        alunos.remove
        (input("Digite o nome do aluno: "))
exi()
