num = []
for i in range(3):
    num.append(float(input(f"Digite o {i+1}° número: ")))
num.sort()
print(f"O maior número é: {num[2]}.")
