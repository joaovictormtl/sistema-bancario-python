saldo = 800
saques_diarios = 0
extrato = ""
limite = 500

while True:
    print("""
[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair
""")
    opcao = int(input(": "))

    if opcao == 1:
        if saques_diarios < 3:
            valor = float(input("\nValor de saque: "))

            if saldo >= valor:
                if valor <= limite:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    saques_diarios += 1
                else:
                    print("Saque superior ao limite permitido")
            else:
                print("Saldo Insuficiente!")
        else:
            print("Limite de Saques diários alcançado.")
    elif opcao == 2:
        valor = float(input("\nValor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Deposite um valor válido!")
    elif opcao == 3:
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Digite uma opcao válida!")