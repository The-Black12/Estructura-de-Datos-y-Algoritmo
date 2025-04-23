def saludar_usuario():
  "Pide al usuario su nombre y muestra un mensaje de bienvenida."
  nombre = input("Por favor, ingresa tu nombre: ")
  print(f"¡Hola, {nombre}! Bienvenido/a.")

if __name__ == "__main__":
  saludar_usuario()