# Um determinado prêmio de loteria saiu para um bolão de três amigos. Uma lei garante que todo prêmio de loteria deva pagar um imposto de 7% para os cofres estaduais. Do total descontado o imposto, os amigos irão dividir o prêmio da seguinte maneira:

# O primeiro ganhador recebera 46%;
# O segundo recebera 32%;
# O terceiro recebera o restante; Faça um programa que leia o valor total do prêmio, calcule o desconto, o valor que cada um tem direito e imprima o total do prêmio, o premio descontado o imposto e a quantia recebida por cada um dos ganhadores.

premio = float(input("Declare o total do prêmeio da loteria: "))
p1 = input("Diga o primeiro ganhador: ")
p2 = input("Diga o segundo ganhador: ")
p3 = input("Diga o terceiro ganhador: ")
imposto = premio*0.07
novoPremio = premio-imposto
premioP1 =  novoPremio*0.46
premioP2 =  novoPremio*0.32
premioP3 = novoPremio-(premioP1+premioP2)

print("-"*30)
print(f"Prêmio: R$ {premio:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Prêmio Descontado: R$ {novoPremio:.2f}")
print(f"Pagamento de(a) {p1}: R$ {premioP1:.2f}")
print(f"Pagamento de(a) {p2}: R$ {premioP2:.2f}")
print(f"Pagamento de(a) {p3}: R$ {premioP3:.2f}")