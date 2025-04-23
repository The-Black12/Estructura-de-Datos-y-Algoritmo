def realizar_operaciones():
  "Pide dos números al usuario y muestra su suma, resta, multiplicación y división."
  try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    if num2 != 0:
      division = num1 / num2
      print(f"La suma es: {suma}")
      print(f"La resta es: {resta}")
      print(f"La multiplicación es: {multiplicacion}")
      print(f"La división es: {division}")
    else:
      print("No se puede dividir por cero.")

  except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
  realizar_operaciones()