def primo(rango):
    contador_primo = 0
    for i in range(1, rango+1):
        contador = 0
        if i == 1:
            continue
        for j in range(1, i+1):
            if j == 1 or j == i:
                continue
            if i % j == 0:
                contador += 1
        if contador == 0:
            contador_primo += 1
            print(i)
    return contador_primo


def run():
    rango = int(input(
        'Ingresa un limite para saber cuantos numeros primos hay en dicho limite: '))
    cantidad = primo(rango)
    print('Del 1 al '+str(rango)+' se encontraron ' +
          str(cantidad)+' numeros primos')


if __name__ == '__main__':
    run()
