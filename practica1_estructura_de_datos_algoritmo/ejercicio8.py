def determinar_par_impar():
  "Pide un número al usuario y determina si es par o impar."
  try:
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
      print(f"El número {numero} es par.")
    else:
      print(f"El número {numero} es impar.")
  except ValueError:
    print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
  determinar_par_impar()