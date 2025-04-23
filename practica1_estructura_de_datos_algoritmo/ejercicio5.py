def verificar_mayor_edad():
  "Pide la edad al usuario y determina si es mayor de edad (18 o más)."
  try:
    edad = int(input("Por favor, ingresa tu edad: "))
    if edad >= 18:
      print("Eres mayor de edad.")
    else:
      print("Eres menor de edad.")
  except ValueError:
    print("Por favor, ingresa un número entero válido para tu edad.")

if __name__ == "__main__":
  verificar_mayor_edad()