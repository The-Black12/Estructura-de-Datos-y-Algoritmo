def calcular_area_rectangulo():
 "Calcula el área de un rectángulo pidiendo al usuario el largo y el ancho."
 try:
    largo = float(input("Ingresa el largo del rectángulo: "))
    ancho = float(input("Ingresa el ancho del rectángulo: "))
    area = largo * ancho
    print(f"El área del rectángulo es: {area}")
 except ValueError:
    print("Por favor, ingresa valores numéricos válidos para el largo y el ancho.")

if __name__ == "__main__":
  calcular_area_rectangulo()