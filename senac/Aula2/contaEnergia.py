'''
Considere que o preço da tarifa de energia é R$ 0,50 por kWh. Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%.
'''

consumo = float(int("Diga o consumo de energia (em kWh): "))
total = (0.5*consumo)
if (consumo > 200):
    print(f"Total (Desconto de 10%): R$ {total-(total*0.1)}")
else:
    print(f"Total: R$ {total}")