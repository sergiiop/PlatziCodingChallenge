def operacion(valor1, operador, valor2):
    if operador == '+':
        suma = valor1 + valor2
        print('La suma entre '+str(valor1)+' y ' +
              str(valor2)+' da como resultado '+str(suma))
    elif operador == '-':
        resta = valor1 - valor2
        print('La resta entre '+str(valor1)+' y ' +
              str(valor2)+' da como resultado '+str(resta))
    elif operador == '*':
        multiplicacion = valor1 * valor2
        print('La multiplicación entre '+str(valor1)+' y ' +
              str(valor2)+' da como resultado '+str(multiplicacion))
    elif operador == '/':
        division = valor1 / valor2
        print('La división entre '+str(valor1)+' y ' +
              str(valor2)+' da como resultado '+str(division))
    else:
        print('Operación invalida')


def run():
    menu = """
    Que operacion deseas realizar?

    Suma => Escribe +
    Resta => Escribe -
    Multiplicacion => Escribe *
    Division => Escribe /
    Elige: """
    valor1 = int(input('Ingresa el primer valor: '))
    operador = str(input(menu))
    valor2 = int(input('Ingresa el segundo valor: '))
    operacion(valor1, operador, valor2)


if __name__ == "__main__":
    run()
