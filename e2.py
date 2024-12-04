contador = 1
soma = 0
while True:
    num = float(input(f"Diga o {contador}º número (ou um negativo para sair): "))
    if (num < 0):
        break
    soma += num
    contador += 1
print(f"A soma dos números positivos é: {soma}")