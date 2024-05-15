opcao = -1
saldo = 800
saques_diarios = 0
saques = 0
depositos = 0
limite = 500

while opcao != 0:
    print("""
[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair
""")
    opcao = int(input(": "))

    if opcao == 1:
        if saques_diarios < 3:
            valor = float(input("Valor de saque: "))

            if saldo >= valor:
                if valor <= limite:
                    saldo -= valor
                    saques += valor
                    saques_diarios += 1
                else:
                    print("Saque superior ao limite permitido")
            else:
                print("Saldo Insuficiente!")
        else:
            print("Limite de Saques diários alcançado.")
    elif opcao == 2:
        valor = float(input("Valor de depósito: "))

        if valor > 0:
            saldo += valor
            depositos += valor
        else:
            print("Deposite um valor válido!")
    elif opcao == 3:
        print(f"Saldo: {saldo:.2f}")
        print(f"Saques: {saques:.2f}")
        print(f"Depósitos: {depositos:.2f}")
else:
    print("Saindo...")
