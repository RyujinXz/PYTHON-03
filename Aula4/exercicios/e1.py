def parImpar(num):
    if num%2==0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")
num = float(input("Diga o número para saber ser par ou ímpar: "))
parImpar(num)