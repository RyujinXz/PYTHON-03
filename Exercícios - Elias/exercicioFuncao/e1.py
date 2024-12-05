def saud(nome: str, hora: int):
    if (6 <= hora <= 12):
        print(f"Bom dia, {nome}!")
    elif (hora <= 18):
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")
nome = input("Diga seu nome: ")
hora = int(input("Diga o horário (formato 24h): "))
saud(nome, hora)