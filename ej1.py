estudiantes = [
    {"nombre": "Juan", "edad": 20},
    {"nombre": "María", "edad": 22},
    {"nombre": "Pedro", "edad": 18},
    {"nombre": "Sofía", "edad": 21},
    {"nombre": "Carlos", "edad": 19}
]


def estudiante_mayor_menor_edad(lista_estudiantes):
    estudiante_menor_edad = None
    edad_mayor = 0
    edad_menor = float("inf")

    for estudiante in lista_estudiantes:
        if estudiante["edad"] > edad_mayor:
            edad_mayor = estudiante["edad"]
            estudiante_mayor_edad = estudiante

        if estudiante["edad"] < edad_menor:
            edad_menor = estudiante["edad"]
            estudiante_menor_edad = estudiante

    return (estudiante_mayor_edad, estudiante_menor_edad)

mayor, menor = estudiante_mayor_menor_edad(estudiantes)
print("Estudiante con mayor edad:", mayor["nombre"], "con", mayor["edad"], "años")
print("Estudiante con menor edad:", menor["nombre"], "con", menor["edad"], "años")
