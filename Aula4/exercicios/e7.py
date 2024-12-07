contador = 1
machos = femeas = totalM = totalF = mediaM = mediaF = 0
while True:
    genero = input(f"Diga o gênero do funcionário {contador} (H/M): ").strip()
    if (genero[0].upper() == "H"):
        salarioM = float(input("Diga o salário do funcionário: "))
        machos += 1
        totalM += salarioM
        contador += 1
    elif (genero[0].upper() == "M"):
        salarioF = float(input("Diga o salário da funcionária: "))
        femeas += 1
        totalF += salarioF
        contador += 1
    else:
        print("Gênero inválido! Por favor, digite 'H' para homem ou 'M' para mulher.")
        continue
    while True:
        continuar = input("Deseja continuar (sim/não): ")
        if (continuar[0].lower() == "s"):
            break
        elif (continuar[0].lower() == "n"):
            break
        else:
            print("Resposta inválida! Por favor, digite 's' para sim ou 'n' para não.")
    if (continuar[0].lower() == "n"):
        break

if (mediaM == 0):
    mediaF = (totalF / femeas)
    print("-"*30)
    print("DADOS DAS FUNCIONÁRIAS")
    print("-"*30)
    print(f"MÉDIA SALARIAL: R$ {mediaF:.2f}")
elif (mediaF == 0):
    mediaM = (totalM / machos)
    print("-"*30)
    print("DADOS DOS FUNCIONÁRIOS")
    print("-"*30)
    print(f"MÉDIA SALARIAL: R$ {mediaM:.2f}")
else:
    mediaM = (totalM / machos)
    mediaF = (totalF / femeas)
    print("-"*30)
    print("DADOS DOS FUNCIONÁRIOS")
    print("-"*30)
    print(f"MÉDIA FEMININA: R$ {mediaF:.2f}")
    print(f"MÉDIA MASCULINA: R$ {mediaM:.2f}")