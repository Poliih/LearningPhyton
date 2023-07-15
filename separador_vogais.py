texto = input("Informe um Texto: ")
Vogais = "AEIOU"

for letras in texto:
    if letras.upper() in Vogais:
        print(letras, end="")

print()