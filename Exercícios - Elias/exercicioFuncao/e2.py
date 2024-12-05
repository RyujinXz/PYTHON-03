def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:  # Evita divisão por zero
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"


# Exemplos de uso:
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
op = input('Informe a operação(+,-,*,/): ')
print(calculadora(n1, n2, op))