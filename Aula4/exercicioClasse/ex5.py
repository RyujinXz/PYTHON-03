class Conta:
    def __init__(self, titular: str, numero: int, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo


    def exibir_saldo(self):
        print(f"-"*15)
        print(f"DADOS CONTA")
        print(f"-"*15)
        print(f"Titular: {self.titular}")
        print(f"Conta: {self.numero}")
        print(f"Saldo: R${self.saldo:.2f}")

    def depositar(self, deposito: float):
        if deposito > 0:
            self.saldo += deposito
            print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")


    def sacar(self, saque):
        if saque > 0 and saque <= self.saldo:
            self.saldo -= saque
            print(f"Saque de R${saque:.2f} realizado com sucesso!")
        elif saque > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")


    def transferir(self, transferencia: float, contaDestino):
        if transferencia > 0 and transferencia <= self.saldo:
            self.saldo -= transferencia
            contaDestino.saldo += transferencia
            print(f"Transferência de R${transferencia:.2f} realizada com sucesso para {contaDestino.titular}.")
        elif transferencia > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor da transferência deve ser positivo.")


# Criando contas para testes
conta1 = Conta("João", 12345, 1000)
conta2 = Conta("Maria", 67890, 500)


# Testando operações
conta1.exibir_saldo()
conta2.exibir_saldo()
print()
print()
conta1.transferir(200, conta2)
print()
print()
conta1.exibir_saldo()
conta2.exibir_saldo()