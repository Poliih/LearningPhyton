def encaixa(A, B):
    len_A = len(A)
    len_B = len(B)

    # Verifica se B é maior que A
    if len_B > len_A:
        return "nao encaixa"

    # Verifica se os últimos dígitos de A correspondem a B
    if A[-len_B:] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Leitura do número de casos de teste
N = int(input())

for _ in range(N):
    # Leitura dos valores A e B
    entrada = input().split()
    A = entrada[0]
    B = entrada[1]

    # Verificação se B encaixa em A
    resultado = encaixa(A, B)

    # Impressão do resultado
    print(resultado)
