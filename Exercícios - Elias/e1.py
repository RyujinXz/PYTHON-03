
'''
Faça um programa para calcular a quantidade de latas de tintas para pintar uma parede. O programa deverá solicitar ao usuário, a altura (float) e o comprimento(float) da parede. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 3,6 litros, que custam R$ 107,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math #importação de biblioteca com funções 


altura = float(input("Altura da parede para se pintar: "))
comprimento = float(input("Comprimento da parede para se pintar: "))
area = altura*comprimento
litros = area/3
latas = litros/3.6
arredondado = math.ceil(latas)
valor = arredondado*107
print(f"Latas: {arredondado}")
print(f"Valor: {valor:.2f}")