def menu():
    print("""
[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair
""")

def saque(*, saldo, valor, extrato_hist, limite, saques_diarios):
    if saques_diarios < 3:
        if saldo >= valor:
            if valor <= limite:
                saldo -= valor
                extrato_hist += f"Saque: R$ {valor:.2f}"
                return f"\n{extrato_hist}\nSaldo: {saldo:.2f}"
            else:
                print("Valor de saque superior ao limite.")
        else:
            print("Saldo Insuficiente.")
    else:
        print("Limite de saques diários alcançado.")

def deposito(saldo, valor, extrato_hist, /):
    if valor <= 0:
        print("Depósito não pode ser inferior ou igual a 0.")
    else:
        saldo += valor
        return f"\n{extrato_hist}\nSaldo: {saldo:.2f}"

def extrato(saldo, /, *, extrato_hist):
    print("\n========== EXTRATO ===========")
    print("Não foram realizadas movimentações.\n" if not extrato_hist else extrato_hist)
    print(f"Saldo: {saldo:.2f}")

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
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

saldo = 800
saques_diarios = 0
extrato_hist = ""
limite = 500
usuarios = []
contas = []

while True:
    menu()
    opcao = int(input(": "))

    if opcao == 1:
        valor = float(input("\nValor de Saque: "))
        print(saque(saldo=saldo, valor=valor, extrato_hist=extrato_hist, saques_diarios=saques_diarios, limite=limite))
       
    elif opcao == 2:
        valor = float(input("\nValor de depósito: "))
        print(deposito(saldo, valor, extrato_hist))
        
    elif opcao == 3:
        extrato(saldo, extrato_hist=extrato_hist)
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Digite uma opcao válida!")
