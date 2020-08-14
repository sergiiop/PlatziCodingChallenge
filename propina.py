def calcular_propina(cantidad_platos, propina):
    valor_total = 0
    porcentaje = propina / 100
    for i in range(cantidad_platos):
        valor = int(input("Ingrese el valor del plato: "))
        valor_total += valor
    valor_propina = valor_total * porcentaje
    print("El valor total sin propina es: "+str(valor_total))
    print("El valor total de la propina es: "+str(valor_propina))
    valor_total += valor_propina
    print("El gran total a pagar es: "+str(valor_total))


def run():
    cantidad_platos = int(input("Ingrese la cantidad de platos: "))
    propina = float(
        input("Ingrese el porcentaje de propina que desea pagar por el pedido: "))
    calcular_propina(cantidad_platos, propina)


if __name__ == '__main__':
    run()
