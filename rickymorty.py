import requests

# 1. Hacemos la petición a la API
url = "https://rickandmortyapi.com/api/character"
respuesta = requests.get(url)
datos = respuesta.json()

# 2. Guardamos la lista de personajes (está dentro de la clave 'results')
personajes = datos['results']

print("=== DATOS DE LOS PERSONAJES ENCONTRADOS ===")

# 3. Recorremos cada personaje con un bucle for y hacemos print de sus datos
for personaje in personajes:
    # Extraemos los datos básicos
    nombre = personaje['name']
    estado = personaje['status']    # Alive, Dead o unknown
    especie = personaje['species']  # Human, Alien, etc.
    
    # El origen es un diccionario, así que entramos a su clave 'name'
    origen = personaje['origin']['name'] 
    
    # Mostramos los datos en la terminal
    print(f"Personaje: {nombre}")
    print(f" - Estado: {estado}")
    print(f" - Especie: {especie}")
    print(f" - Origen: {origen}")
    print("-" * 30) # Esto coloca una línea de guiones para separar cada personaje