num = 0
par = []
pare = 0

for i in range(10):
    num = float(input(f"Digite o {i+1}° número: "))
    if (num%2 == 0):
        par.append(num)
        pare += 1
print(f"Teve {pare} números pares.")
print(f"Foram eles: {par}")
