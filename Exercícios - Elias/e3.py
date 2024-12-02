# A padaria Sópão vende diariamente uma certa quantidade de pães franceses e uma quantidade de broas. Cada pãozinho custa R$ 0,80 e a broa custa R$ 2,50. Do total arrecadado, 43% corresponde aos custos de fabricação. Do restante, Seu joão guarda 15% numa conta de poupança e 15% ele converte em Euros para sua viagem anual. Sabe-se que 1 Euro custa R$ 4,60. Com base nestes fatos, faça um programa para ler as quantidades de pães e de broas, calcular a venda total de pães e broas, o custo de fabricação, quanto irá guardar na poupança e quantos euros irá comprar. Ao final, exibir os dados calculados.


pao = int(input("Diga quantos pães serão fabricados: "))
broa = int(input("Diga quantas broas serão feitas: "))

valorBroa = broa*2.5
valorPao = pao*0.8 
total = valorBroa + valorPao

custoFabricacao = total*0.43
poupanca = (total-custoFabricacao)*0.15
euro = poupanca/4.6

print("-"*30)
print(f"Venda Total: R$ {total:.2f}")
print(f"Custo de Fabricação: R$ {custoFabricacao:.2f}")
print(f"Poupança: R$ {poupanca:.2f}")
print(f"Euro: € {euro:.2f}")
print("-"*30) 