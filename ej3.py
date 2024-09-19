def registrar_personas():
    personas = {}
    while True:
        nombre = input("Introduce el nombre de la persona (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            edad = int(input(f"Introduce la edad de {nombre}: "))
        except ValueError:
            print("La edad debe ser un número. Inténtalo de nuevo.")
            continue
        correo = input(f"Introduce el correo de {nombre}: ")
        
        personas[nombre] = {
            'edad': edad,
            'correo': correo
        }
    return personas

def filtrar_mayores(personas):
    mayores = {}
    for nombre, datos in personas.items():
        if datos['edad'] >= 18:
            mayores[nombre] = datos
    return mayores

def filtrar_menores(personas):
    menores = {}
    for nombre, datos in personas.items():
        if datos['edad'] < 18:
            menores[nombre] = datos
    return menores

personas_registradas = registrar_personas()

if personas_registradas:
    personas_mayores = filtrar_mayores(personas_registradas)
    print("\nPersonas mayores o iguales a 18 años:")
    if personas_mayores:
        for nombre, datos in personas_mayores.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Correo: {datos['correo']}")
    else:
        print("No hay personas mayores o iguales a 18 años registradas.")

    personas_menores = filtrar_menores(personas_registradas)
    print("\nPersonas menores de 18 años:")
    if personas_menores:
        for nombre, datos in personas_menores.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Correo: {datos['correo']}")
    else:
        print("No hay personas menores de 18 años registradas.")
else:
    print("No se ha registrado ninguna persona.")

