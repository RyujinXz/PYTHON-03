'''
Crie um programa que calcule o valor total de uma compra feita em várias parcelas. 
Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.
'''
parcela = int(input("Digite quanta parcelas irá pagar: "))
valorParcela = float(input("Digite o valor de cada parcela: R$ "))
total = (parcela*valorParcela)
if (total > 1000):
    print(f"Total (5% de juros): R$ {total+total*0.05}")
else:
    print(f"Total: R$ {total:.2f}")