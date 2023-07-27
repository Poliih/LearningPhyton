menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Depósito: +R$ {deposito:.2f}")
        else:
            print("Não é possível depositar esse valor")

    elif opcao == "s":
        saque = float(input("Valor do saque: "))
        if numero_saques < LIMITE_SAQUES and saque <= 500:
            if saque <= saldo:
                saldo = saldo - saque
                extrato.append(f"Saque: -R$ {saque:.2f}")
                numero_saques += 1
            else:
                print("Você não possui saldo suficiente.")
        else:
            if numero_saques >= LIMITE_SAQUES:
                print("Você excedeu o limite de saques no dia.")
            else:
                print("Você não pode sacar mais de R$ 500,00 por vez")

    elif opcao == "e":
        print("\nExtrato:")
        for item in extrato:
            print(item)
        print("Saldo Atual: R$ {:.2f}\n".format(saldo))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
