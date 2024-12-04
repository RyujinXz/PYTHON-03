contador = 1
soma = 0
media = 0
while True:
    num = int(input(f"Diga o {contador}º número (digite 0 para sair): "))
    if (num < 0):
        print("-"*30)
        print("   ** ERRO: Apenas números positivos são válidos! **")
        print("-"*30 )

    elif (num == 0):
        break
    else: 
        soma += num
        media += 1
        contador += 1
somaMedia = (soma / media)
print("-"*12) 
print("RESULTADO") 
print("-"*12)
print(f"MÉDIA: {somaMedia:.2f}") 