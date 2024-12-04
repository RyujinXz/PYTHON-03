Numeros = []
for i in range(1, 4):
    numero = int(input(f"Diga o {i}º número: "))
    Numeros.append(numero)
Numeros.sort()
print(f"O maior número é: {Numeros[2]}")