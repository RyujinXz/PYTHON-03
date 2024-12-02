idades = []
i = 0
while i < 3:
    N = (int(input(f"Diga a idade da {i+1}ª irmã: ")))
    if (5 <= N <= 100):
        idades.append(N)
        i += 1
    else:  
        
        print()
        print()
        print()
        print("-"*30)
        print("Insira um idade válida! (Entre 5 à 100 anos)")
        print("-"*30)
        print()
        print()
        print()
idades.sort()
print(f"A idade de Camila é {idades[1]} anos.")