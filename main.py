from banco import Banco

banco = Banco()

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo cliente
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """

print("Bem-vindo ao Banco B7!")

while True:
    opcao = input(menu).lower()

    if opcao == "nu":
        banco.cadastrar_cliente()
    elif opcao == "nc":
        banco.criar_conta()
    elif opcao == "lc":
        banco.listar_contas()
    elif opcao == "d":
        numero = int(input("Número da conta: "))
        conta = banco.buscar_conta(numero)
        if conta:
            valor = float(input("Valor do depósito: "))
            if conta.depositar(valor):
                print("Depósito realizado.")
            else:
                print("Valor inválido.")
        else:
            print("Conta não encontrada.")
    elif opcao == "s":
        numero = int(input("Número da conta: "))
        conta = banco.buscar_conta(numero)
        if conta:
            valor = float(input("Valor do saque: "))
            resultado = conta.sacar(valor)
            if resultado is True:
                print("Saque realizado.")
            else:
                print(resultado)
        else:
            print("Conta não encontrada.")
    elif opcao == "e":
        numero = int(input("Número da conta: "))
        conta = banco.buscar_conta(numero)
        if conta:
            conta.mostrar_extrato()
        else:
            print("Conta não encontrada.")
    elif opcao == "q":
        print("Obrigado por usar o Banco B7!")
        break
    else:
        print("Opção inválida.")