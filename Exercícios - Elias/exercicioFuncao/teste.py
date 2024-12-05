"""
O que é uma lista?

Listas são usadas para armazenar múltiplos, ordenados

Como identificar?
Utilizar o símbolo [] (colchetes) para as listas;
Armazenar a lista em uma VARIÁVEL;
Separa itens da lista pela vírgula;


Posição dos Itens da Lista
As listas são indexadas, o primeiro item tem index [0], o segundo item tem index [1] etc.
Exemplos:

Outro ponto interessante é que conseguimos utilizar as posições negativas dentro da lista para buscar os dados na ordem inversa!

A lista permite itens com nomes duplicados!

É possível também medir o cumprimento de um lista

Você pode mudar o valor de um elemento específico ou de um range
"""






frutas = ["maça", "banana", "cereja", "laranja", "cenoura"]

frutas[1:3] = ["casa", "cebola", "chocolate", "ameixa"]
print(frutas)

Métodos do Python para utilizar nas listas
Agora vamos analisar alguns métodos do Python como: append e insert (para inserir informações na lista); del, pop e remove (para remover itens da lista).

Para adicionar um item a lista:

.append(): adiciona o item ao final da lista;
.insert(): insere um item na lista na posição indicada
Para deletar um item da lista:

del: remove um item da lista baseado na posição indicada;
.remove(): remove um item baseado no seu valor e não na sua posição;
.pop(): remove da lista_compras o último item, mas não o exclui.
No exemplo abaixo tentamos incluir o item ‘carro’ a nossa lista_compras com o .append():

lista_compras.append('carro')
print(lista_compras)
['banana', 'laranja', 'maçã', 'carro']
Utilizando del para remover item com base na posição indicada:

del lista_compras[3]
print(lista_compras)
['banana', 'laranja', 'maçã']
Já no código abaixo, adicionamos ‘carro’ à lista na posição indicada, com .insert():

lista_compras.insert(1,'carro')
print(lista_compras)
['banana', ' carro', 'laranja', 'maçã']
Removendo um item com base no seu valor e não na sua posição, com o .remove() (ATENÇÃO! retira apenas a primeira ocorrência e não todas):

lista_compras.append('carro')
print(lista_compras)
['banana', 'carro', 'laranja', 'maçã', 'carro']

lista_compras.remove('carro')
print(lista_compras)
['banana', 'laranja', 'maçã', 'carro']
É comum que as listas se iniciem sem nenhum valor. Como se fosse um papel em branco que gradualmente você adiciona informações.

Para criarmos vamos usar novamente o colchetes, mas sem nenhum item:

lista_sonhos = []
Utilizando .pop(), iremos remover o último item da lista_compras, mas sem excluí-lo. Nesse caso, o valor carro será armazenado na variável item:

item = lista_compras.pop(-1)
print(item)
carro
Após retirar da lista_compras, adicionamos ‘carro’ na nossa lista_sonhos:

lista_sonhos.append(item)
print(lista_sonhos)
['carro']



def lista_de_mercado():
    print("Olá, seja bem-vindo ao My List!")
    print("Escolha o tema da sua lista:")
    print("1 - Lista de Frutas")
    print("2 - Lista de Carnes")
    print("3 - Lista de Higiene")
    
    frutas = ["Banana", "Limão", "Tangerina", "Melancia", "Uva"]
    carnes = ["Asa", "Peito", "Coxa", "Coração", "Alcatra", "Moela"]
    higiene = ["Desodorante", "Hidratante", "Sabonete", "Shampoo", "Pasta de dente"]

    try:
        opcao = int(input("Digite o número da lista que deseja visualizar (1/2/3): "))
        if opcao == 1:
            print("\nLista de Frutas:")
            for fruta in frutas:
                print(f"- {fruta}")
        elif opcao == 2:
            print("\nLista de Carnes:")
            for carne in carnes:y
                print(f"- {carne}")
        elif opcao == 3:
            print("\nLista de Higiene:")
            for item in higiene:
                print(f"- {item}")
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 3.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspondente ao menu.")


append(): Adiciona um elemento no final da lista

pop(): Remove o elemento na posição especificada

sort(): Classifica a lista

remove(): Remove o item com o valor especificado

index(): Retorna o índice do primeiro elemento com o valor especificado

lista_de_mercado()

