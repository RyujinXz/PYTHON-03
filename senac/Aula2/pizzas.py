'''
TESTE PARA VER SE DÁ PRA FAZER MENU DE PIZZAS
'''

i = 0
opcao = 0
total = 0
calabresa = 0
peperoni = 0
quatroQueijos = 0
muzzarela = 0
while (opcao != 5):
    print("-"*30)
    print("PIZZAS SENAC")
    print("-"*30)
    print()
    print()
    print("1. Pizza de Calebresa - R$ 49.50")
    print("2. Pizza de Peperoni - R$ 80.50")
    print("3. Pizza Quatro Queijos - R$ 59.50")
    print("4. Pizza de Muzzarela - R$ 84.99")
    print("5. Sair")
    print()
    print("~"*20)
    opcao = int(input("Diga a opção que gostaria de selecionar: "))
    if (opcao < 1) or (opcao > 5):
        print()
        print()
        print("!!!")
        print("Opção Inválida. Digite uma opção /válida/.")
    elif (opcao == 1):
        total += 49.5
        calabresa += 1
    elif (opcao == 2):
        total += 80.5
        peperoni += 1
    elif (opcao == 3):
        total += 59.5
        quatroQueijos += 1
    elif (opcao == 4):
        total += 84.99
        muzzarela += 1
print("-"*30)
print("RESUMO DO PEDIDO")
print("-"*30)
print(f"PIZZA'S CALABRESA: {calabresa}")
print(f"PIZZA'S PEPERONI: {peperoni}")
print(f"PIZZA'S QUATRO QUEIJOS: {quatroQueijos}")
print(f"PIZZA'S MUZZARELA: {muzzarela}")
print(f"TOTAL DE PIZZAS: {muzzarela+peperoni+quatroQueijos+muzzarela}")
print(f"VALOR: R$ {total}")