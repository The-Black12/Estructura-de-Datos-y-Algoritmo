def sumar_complejos(complejo1, complejo2):
  "Suma dos números complejos y devuelve el resultado."
  suma = complejo1 + complejo2
  return suma

if __name__ == "__main__":
  # Define los dos números complejos
  numero_complejo1 = 3 + 2j
  numero_complejo2 = 1 - 4j

  # Calcula la suma
  resultado_suma = sumar_complejos(numero_complejo1, numero_complejo2)

  # Muestra el resultado
  print(f"La suma de {numero_complejo1} y {numero_complejo2} es: {resultado_suma}")