class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    def __init__(self, numero, cliente):
        self.agencia = "0001"
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return True
        return False

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        elif valor > self.LIMITE_VALOR:
            return "Valor excede o limite por saque."
        elif self.saques >= self.LIMITE_SAQUES:
            return "Número máximo de saques atingido."
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.saques += 1
            return True
        return "Valor inválido."

    def mostrar_extrato(self):
        print("\n=== EXTRATO ===")
        print(self.extrato if self.extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")