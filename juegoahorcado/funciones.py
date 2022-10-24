
import random




#función para escojer una palabra random
def selectpalabra():
  lineas = open("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra


#Función entrada del teclado
def entusuario():
  letra = input("introduzca una letra: ")
  return letra.lower()


#Función actualizar jugada
def actjugada(palabra, letra, jugada):
  n_letras = len(palabra)
  for i in range(0, n_letras):
    if palabra[i] == letra:
      jugada[i] = letra
  return jugada


#palabra = selectpalabra()
#letra = entusuario()
#jugada = ["_"] * len(palabra)
#jugada = actjugada(palabra, letra, jugada)


#Actualizar el alfabeto
def updatealphabet(letra, alfabeto):
  alfabeto = alfabeto.replace(letra, " ")
  return alfabeto


#alfabeto = updatealphabet(letra, alfabeto)


#imprimir resultado en pantalla
def impact(alfabeto, jugada):
  print(f"jugada:{jugada}")
  print(f"letras disponibles:{alfabeto}")


#impact(alfabeto, jugada)


#verificar jugada
def verjugada(suposicion, palabra):
  success = False
  if suposicion == palabra:
    success = True

  return success


#success = verjugada("tomate", palabra)
#print(success)
