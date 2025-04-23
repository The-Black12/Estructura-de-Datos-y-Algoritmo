def determinar_signo():
  "Pide un número al usuario y determina si es positivo, negativo o cero."
  try:
    numero = float(input("Ingresa un número: "))
    if numero > 0:
      print("El número es positivo.")
    elif numero < 0:
      print("El número es negativo.")
    else:
      print("El número es cero.")
  except ValueError:
    print("Por favor, ingresa un valor numérico válido.")

if __name__ == "__main__":
  determinar_signo()