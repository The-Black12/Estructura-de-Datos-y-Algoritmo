def celsius_a_fahrenheit():
  "Convierte grados Celsius a Fahrenheit pidiendo la temperatura al usuario."
  try:
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
  except ValueError:
    print("Por favor, ingresa un valor numérico válido para la temperatura en Celsius.")

if __name__ == "__main__":
  celsius_a_fahrenheit()
