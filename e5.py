par = 0
Pares = []
for i in range(1, 11):
    num = int(input(f"Digite o {i}º número: "))
    if (num % 2 == 0):
        par += 1
        Pares.append(num)
Pares.sort()
print(f"Foram {par} números pares.")
print(f"Sendo eles: {Pares}")