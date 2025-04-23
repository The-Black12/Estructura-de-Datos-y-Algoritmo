def mostrar_tercer_pais():
  "Crea una tupla de países y muestra el tercer elemento."
  paises = ("España", "Canadá", "Ucrania", "Brasil", "Argentina")
  tercer_pais = paises[2]  # Los índices en Python comienzan desde 0
  print(f"El tercer país en la tupla es: {tercer_pais}")

if __name__ == "__main__":
  mostrar_tercer_pais()