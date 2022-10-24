from funciones import *


def main():

  palabra = selectpalabra()
  alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x z"
  jugada = ["_"] * len(palabra)
  for turno in range(5):
    print(f"\nturno:{turno+1}")
    print("-" * 20)
    # imprimir alfabeto
    impact(alfabeto, jugada)
    #Entrada Usuario
    letra = entusuario()

    #Actualizar alfabeto
    jugada = actjugada(palabra, letra, jugada)
    alfabeto = updatealphabet(letra, alfabeto)

    #Imprimir actualización
    impact(alfabeto, jugada)

    #Preguntar si el usuario desea o no adivinar la palabra
    check = input("Desea adivinar la palabra? (s/n):")
    if check.lower() == "s":
      suposicion = input("Introduzca su respuesta: ").lower()
      success = verjugada(suposicion, palabra)
      if success:
        print("+" * 20)
        print("siuuu ganoo")
        print("+" * 28)
        break
      else:
        print("+" * 20)
        print("Nouu es correcto :V")
        print("+" * 28)

    if turno == 4:
      print("-" * 20)
      print("Se ahorcooo XD HAHAHA")
      print("-" * 28)


if __name__ == "__main__":
  main()
  #selecionar  palabra e inicializar el alfabeto y jugada

# 5 turnos
