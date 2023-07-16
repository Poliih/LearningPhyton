texto = input("Escreva seu texto: ")
limite_letras = int(input("Limite de quantas letras: "))

def quantidade_letras(texto, limite_letras):
    if len(texto) <= limite_letras:
        return "Verdadeiro"
    else:
        return "Falso"

resultado = quantidade_letras(texto, limite_letras)
print(resultado + " -> " + texto)
