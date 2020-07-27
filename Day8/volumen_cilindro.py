import math

def calcular_volumen(radio_cilindro,altura_cilindro):
  PI = math.pi
  area_cilindro = PI * (radio_cilindro**2)
  area_cilindro = round(area_cilindro,1)
  print(area_cilindro)
  volumen_cilindro = area_cilindro * altura_cilindro
  volumen_cilindro = round(volumen_cilindro,1)
  print(volumen_cilindro)
  return volumen_cilindro, area_cilindro


def run():
  radio_cilindro = int(input('Ingrese el radio del cilindro en cm: '))
  altura_cilindro = int(input('Ingrese la altura del cilindro en cm: '))
  cilindro = calcular_volumen(radio_cilindro,altura_cilindro)
  print('El area del cilindro es: '+str(cilindro[1])+ ' Y el Volumen del Cilindro es: '+str(cilindro[0]))

if __name__ == '__main__':
    run()
