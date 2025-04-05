NUM_LIMITE_SAQUES = 3
VL_TOTAL_SAQUE_DIA = 1500
VL_MAX_SAQUE = 500
extrato = ""
saldo = 2000

menu = """
Bem vindo ao terminal bancário. Digite a opção desejada:
D - Depositar
S - Sacar
E - Extrato
Q - Sair
==> """
print(menu)
opcao = input("Digite a opção desejada: ").upper()
while True:
    if opcao == "Q":
        print("Saindo do sistema. Até logo!")
        break
    elif opcao not in ["D", "S", "E"]:
        print("Opção inválida. Tente novamente.")
        opcao = input(menu).upper()
        continue
    # Verifica se o usuário deseja sair
    if opcao != "Q":
        if opcao == "D":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f">>> Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                print(f"Saldo atual R$ {saldo:.2f}")
            else:
                print("Valor inválido para depósito.")
        elif opcao == "S":
            if extrato.count("Saque") >= NUM_LIMITE_SAQUES:
                print("Número máximo de saques diários atingido.")
            else:
                valor = float(input("Informe o valor do saque: "))
                if 0 < valor <= VL_MAX_SAQUE and saldo >= valor:
                    saldo -= valor
                    extrato += f">>> Saque: R$ {valor:.2f}\n"
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                    print(f"Saldo atual R$ {saldo:.2f}")
                else:
                    print("Valor inválido para saque ou saldo insuficiente.")
        elif opcao == "E":
            print("Extrato:")
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Opção inválida. Tente novamente.")

        opcao = input(menu).upper()

