def sumar_numeros_hasta_cero():
  "Suma números ingresados por el usuario hasta que ingrese 0."
  suma = 0
  while True:
    try:
      numero = float(input("Ingresa un número (ingresa 0 para terminar): "))
      if numero == 0:
        break  # Sale del bucle si el usuario ingresa 0
      suma += numero
    except ValueError:
      print("Por favor, ingresa un valor numérico válido.")
  print(f"La suma de los números ingresados es: {suma}")

if __name__ == "__main__":
  sumar_numeros_hasta_cero()