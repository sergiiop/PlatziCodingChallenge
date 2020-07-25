def run(palabra, veces):
    LIMITE = 1
    if LIMITE <= veces:
        print(palabra)
        veces = veces - 1
        run(palabra, veces)


if __name__ == "__main__":
    palabra = input('Introduce una palabra: ')
    veces = int(input('¿Cuantas veces deseas repetir esta palabra?: '))
    run(palabra, veces)
