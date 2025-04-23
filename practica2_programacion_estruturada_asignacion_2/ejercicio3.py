def sumar(num1, num2):
  "Suma dos números."
  return num1 + num2

def restar(num1, num2):
  "Resta dos números."
  return num1 - num2

def multiplicar(num1, num2):
  "Multiplica dos números."
  return num1 * num2

def dividir(num1, num2):
  "Divide dos números."
  if num2 == 0:
    return "Error: No se puede dividir por cero."
  return num1 / num2

def calculadora_funciones():
  "Interfaz de la calculadora usando funciones."
  while True:
    print("\nSelecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación: ")

    if opcion in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
          print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
          print("Resultado:", restar(num1, num2))
        elif opcion == '3':
          print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
          print("Resultado:", dividir(num1, num2))
      except ValueError:
        print("Entrada inválida. Por favor, ingresa números.")
    elif opcion == '5':
      print("¡Gracias por usar la calculadora!")
      break
    else:
      print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
  calculadora_funciones()