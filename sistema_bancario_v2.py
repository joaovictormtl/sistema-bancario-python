def menu():
    print("""
[1] Sacar
[2] Depositar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Contas          
[0] Sair
""")

def sacar(*, saldo, valor, extrato_hist, limite, saques_diarios):
    if saques_diarios < 3:
        if saldo >= valor:
            if valor <= limite:
                saldo -= valor
                saques_diarios += 1
                extrato_hist += f"Saque: R$ {valor:.2f}\n"
            else:
                print("Valor de saque superior ao limite.")
        else:
            print("Saldo Insuficiente.")
    else:
        print("Limite de saques diários alcançado.")
    return saldo, extrato_hist

def depositar(saldo, valor, extrato_hist, /):
    if valor <= 0:
        print("Depósito não pode ser inferior ou igual a 0.")
    else:
        saldo += valor
        extrato_hist += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato_hist

def extrato(saldo, /, *, extrato_hist):
    print("\n========== EXTRATO ===========")
    print("Não foram realizadas movimentações.\n" if not extrato_hist else extrato_hist)
    print(f"Saldo: {saldo:.2f}")

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return False

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com este CPF")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    endereco = input("Logradouro - nº - Bairro - Cidade/Sigla: ")
    
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("Usuário cadastrado com sucesso")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}\nN. Conta: {conta['numero_conta']}\nUsuário: {conta['usuario']['nome']}\n")

def main():
    saldo = 800
    saques_diarios = 0
    extrato_hist = ""
    LIMITE = 500
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        menu()
        opcao = int(input(": "))

        if opcao == 1:
            valor = float(input("\nValor de Saque: "))
            saldo, extrato_hist = sacar(saldo=saldo, valor=valor, extrato_hist=extrato_hist, saques_diarios=saques_diarios, limite=LIMITE)
        
        elif opcao == 2:
            valor = float(input("\nValor de depósito: "))
            saldo, extrato_hist = depositar(saldo, valor, extrato_hist)

        elif opcao == 3:
            extrato(saldo, extrato_hist=extrato_hist)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta +=1

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Digite uma opcao válida!")
main()
