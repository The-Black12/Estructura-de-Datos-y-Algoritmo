def mostrar_edad_persona():
  "Crea un diccionario con información de una persona y muestra su edad."
  persona = {
      "nombre": "Felipe Pérez",
      "edad": 22,
      "ciudad": "El Seibo"
  }
  edad_persona = persona["edad"]
  print(f"La edad de la persona es: {edad_persona} años.")

if __name__ == "__main__":
  mostrar_edad_persona()