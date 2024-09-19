Jugadores = [
    {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 20, 'posicion': 'portero'},
    {'nombre': 'Marcelo', 'apellido': 'Gomez', 'edad': 30, 'posicion': 'defensa'},
    {'nombre': 'Claudio', 'apellido': 'Echeverri', 'edad': 10, 'posicion': 'Mediocampista'},
    {'nombre': 'Juan', 'apellido': 'Hurtado', 'edad': 7, 'posicion': 'Mediocampista'},
    {'nombre': 'Miguel', 'apellido': 'Borja', 'edad': 8, 'posicion': 'Delantero'},
    {'nombre': 'Franco', 'apellido': 'Armani', 'edad': 30, 'posicion': 'Arquero'},
    {'nombre': 'Marcelo', 'apellido': 'Gomez', 'edad': 30, 'posicion': 'defensa'}
]

for jugador in Jugadores:
    print(f"Nombre: {jugador.get('nombre')}, Apellido: {jugador.get('apellido')}, Edad: {jugador.get('edad')}, Posición: {jugador.get('posicion')}")
