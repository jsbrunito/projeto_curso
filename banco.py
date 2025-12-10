from cliente import Cliente
from conta import Conta

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self):
        while True:
         cpf = input("Digite seu CPF (somente números): ")
         
         if cpf.isdigit():
            print("CPF válido:", cpf)
            break
         else:
            print("Erro: digite apenas números.")
        if self.buscar_cliente(cpf):
            print("Cliente já cadastrado.")
            return
        nome = input("Nome: ")
        nascimento = input("Nascimento (dd-mm-aaaa): ")
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade_uf = input("Cidade/UF: ")
        endereco = f"{rua}, {numero} - {bairro} - {cidade_uf} "
        cliente = Cliente(nome, cpf, nascimento, endereco)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso.")

    def buscar_cliente(self, cpf):
        return next((c for c in self.clientes if c.cpf == cpf), None)

    def criar_conta(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return

        numero = len(self.contas) + 1
        conta = Conta(numero, cliente)
        self.contas.append(conta)
        print("Conta criada com sucesso.")

    def listar_contas(self):
        for conta in self.contas:
            print(f"""
Agência: {conta.agencia}
Número: {conta.numero}
Titular: {conta.cliente.nome}
CPF: {conta.cliente.cpf}
Saldo: R$ {conta.saldo:.2f}
""")

    def buscar_conta(self, numero):
        return next((c for c in self.contas if c.numero == numero), None)