import os

# Caminho para o diretório desejado
caminho_arquivo = r"C:\dados.txt"  # Usando raw string (r"") para evitar problemas com barras invertidas

# Garantir que o diretório exista
diretorio = os.path.dirname(caminho_arquivo)
if not os.path.exists(diretorio):
    os.makedirs(diretorio)  # Cria o diretório, se não existir

# Escrever no arquivo
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write("Curso: Programação em Python\n")
    arquivo.write("Aluno: Maria\n")
    arquivo.write("Progresso: 85%\n")

print(f"Arquivo salvo em: {caminho_arquivo}")