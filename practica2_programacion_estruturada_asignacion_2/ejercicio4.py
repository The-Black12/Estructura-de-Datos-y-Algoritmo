import operator

def calculadora_biblioteca():
  "Calculadora usando la biblioteca operator."
  operaciones = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
  }

  while True:
    print("\nSelecciona la operación (+, -, *, /) o 'salir':")
    operacion = input("> ")
    if operacion == 'salir':
      print("¡Gracias por usar la calculadora!")
      break
    elif operacion in operaciones:
      try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = operaciones[operacion](num1, num2)
        print("Resultado:", resultado)
      except ValueError:
        print("Entrada inválida. Por favor, ingresa números.")
      except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
      print("Operación inválida. Por favor, selecciona una operación válida (+, -, *, /) o 'salir'.")

if __name__ == "__main__":
  calculadora_biblioteca()