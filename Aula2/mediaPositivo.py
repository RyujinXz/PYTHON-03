
contador = 1
somaMedia = 0
while (i != 0):
    num = float(int(input(f"Digite o {contador}º contador")))
    contador += 1
    if (num%2==0):
        somaMedia += num
        par += 1
print(f"A média da soma dos números pares é {somaMedia/par}.")