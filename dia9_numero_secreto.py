import random

def run():
    limite = int(input('Elige un limite para jugar: '))
    secreto = random.randint(1,limite)
    elegido = int(input('Ingresa un número entre 1 y ' +str(limite)+': '))
    contador = 0
    while elegido != secreto:
      if elegido > secreto:
          print('El número que buscas es menor')
      else:
          print('El número que buscas es mayor')
      elegido = int(input('Elige otro número: '))
      contador +=1
    print('El número es '+str(secreto) +
          ', Ganaste en el intento Nº: '+str(contador))



if __name__ == "__main__":
    run()
