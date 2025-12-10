class Cliente:
    def __init__(self, nome, cpf, nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"