i = 0
soma = 0
contador = 1
while i >= 0:
    i = int(input(f"Digite o {contador}° número: "))
    contador += 1
    if i >= 0:
        soma += i
    else: 
        break
print(f"A soma de todo os números positivos é: {soma}.")