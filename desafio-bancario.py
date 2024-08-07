menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "q":
        break
    elif opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        else:
            print("Valor inválido")
    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor a sacar: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido")
            continue
        elif valor > saldo:
            print("Saldo insuficiente")
            continue
        elif valor > limite:
            print("Valor acima do limite")
            continue
        else:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
    elif opcao == "e":
        print("Extrato")
        print(f"Saldo: R$ {saldo:.2f}")
    else:
        print("Opção inválida")


