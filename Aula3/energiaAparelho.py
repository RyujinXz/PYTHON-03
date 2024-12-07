'''
Crie um programa que calcule o consumo total de energia de vários aparelhos em uma casa. Pergunte o consumo de cada aparelho em kWh e a quantidade de horas que o aparelho fica ligado por dia. O programa deve somar o consumo diário de todos os aparelhos e calcular o custo total de energia no mês.
'''

while True:
    consumo = float(input(f"Diga o consumo do {contador}º aparelho em (kwH): "))
    hora = float(input(f"Diga quantas horas o {contador}º aparelho fica ligado (em Horas): "))
    resposta = input("Deseja adicionar mais um aparelho? [sim/não]: ")
    qtdConsumo += consumo
    qtdHora += hora
    if (resposta.lower() == "não"):
        break

print("-"*30)    
print(RESULTDOS)    
print("-"*30)    
print(f"Consumo Diário de Todos os Aparelhos: {qtdConsumo*24}")
print(f"Custo Total de Energia (Mensal): {(qtdConsumo/qtdHora)*30}")
