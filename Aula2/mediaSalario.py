salarioH = 0
salarioM = 0
mulher = 0
homem = 0
homens = []
mulheres = []
contador = 1
while True:
    salario = (float(input(f"Digite o salário do(a) {contador}º/ª funcionário(a): ")))
    gen = (input("Diga o gênero do(a) funcionário(a) (homem/mulher): "))
    if (gen.lower() == "mulher"):
        salarioM += salario
        mulher += 1
    elif (gen.lower() == "homem"):
        salarioH += salario
        homem += 1
    else:
        print("Genêro inválido! Tente Novamente.")
        continue
    while True:
        continuar = input("Deseja continuar? (sim/não): ")
        contador += 1
        if (continuar.lower() == "não"):
            break
        if (continuar.lower() == "sim"):
            continue
        else:
            print("Não Entendi.")
print("-"*30)
print("RESULTADOS")
print("-"*30)
print(f"MÉDIA DO SALÁRIO DOS HOMENS: {salarioH/homem}")
print(f"MÉDIA DO SALÁRIO DAS MULHERES: {salarioM/mulher}")