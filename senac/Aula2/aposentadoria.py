idade = int(input("Diga a idade: "))
contribuicao = int(input("Diga quantos anos contribuição: "))
if (idade >= 60) or (contribuicao >= 35):
    print("Já pode aposentar-se!")
else:
    aposentarI = 60-idade
    aposentarC = 35-contribuicao
print(f"Por Idade: {aposentarI} anos restantes")
print(f"Por Contrubuição: {aposentarC} anos restantes")
