def traducir(texto):
    vocales = ('a', 'e', 'i', 'o', 'u')
    for vocal in vocales:
        if texto[0] == vocal:
            texto = texto + 'way'
            return texto
        elif texto[0] != vocal:
            word = texto[0]
            texto = texto[1:]
            texto = texto + word + 'ay'
            return texto


def run():
    texto = str(input('Escriba el texto a traducir: '))
    texto = texto.lower()
    traduccion = traducir(texto)
    print('La traduccion de '+texto+' es: '+traduccion)


if __name__ == "__main__":
    run()
