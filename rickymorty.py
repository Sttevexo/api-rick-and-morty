import requests

# # 1. Hacemos la petición a la API
url = "https://rickandmortyapi.com/api/character"
respuesta = requests.get(url)
datos = respuesta.json()

# # 2. Guardamos la lista de personajes (está dentro de la clave 'results')
personajes = datos['results']


# 🔽 AQUÍ EMPIEZA EL CAMBIO (Reemplaza desde la línea 11 antigua) 🔽

# Abrimos el archivo 'dados.txt' en modo escritura ('w')
with open("dados.txt", "w", encoding="utf-8") as archivo:
    
    # Printeamos el título en la terminal y lo escribimos en el archivo
    print("=== DATOS DE LOS PERSONAJES ENCONTRADOS ===")
    archivo.write("=== DATOS DE LOS PERSONAJES ENCONTRADOS ===\n")
    
    # # 3. Recorremos cada personaje con un bucle for
    for personaje in personajes:
        # Extraemos los datos básicos
        nombre = personaje['name']
        estado = personaje['status']   # Alive, Dead o unknown
        especie = personaje['species']  # Human, Alien, etc.
        origen = personaje['origin']['name']
        
        # Esto lo sigue mostrando en tu terminal de VS Code
        print(f"Personaje: {nombre}")
        print(f" - Estado: {estado}")
        print(f" - Especie: {especie}")
        print(f" - Origen: {origen}")
        print("-" * 30)
        
        # Esto lo escribe automáticamente dentro del archivo dados.txt
        archivo.write(f"Personaje: {nombre}\n")
        archivo.write(f" - Estado: {estado}\n")
        archivo.write(f" - Especie: {especie}\n")
        archivo.write(f" - Origen: {origen}\n")
        archivo.write("-" * 30 + "\n")

        