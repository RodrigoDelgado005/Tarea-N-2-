# Diccionario con productos y precios
productos = {
    'manzana': 1.50,
    'banana': 0.80,
    'naranja': 0.90
}

# Función para calcular el total a pagar
def calcular_total(compra):
    total = 0
    for producto, cantidad in compra.items():
        if producto in productos:
            total += productos[producto] * cantidad
        else:
            print(f"El producto {producto} no está disponible.")
    return total

# Función para pedir productos y cantidades al usuario
def pedir_compra():
    compra = {}
    print("Productos disponibles: manzana, banana, naranja.")
    while True:
        producto = input("Introduce el nombre del producto (o 'Terminado' para terminar): ").lower()
        if producto == 'Terminado':
            break
        if producto in productos:
            cantidad = int(input(f"Introduce la cantidad de {producto} que quieres comprar: "))
            compra[producto] = cantidad
        else:
            print(f"El producto {producto} no está disponible.")
    return compra

# Ejecución
compra = pedir_compra()
if compra:
    total_a_pagar = calcular_total(compra)
    print(f"Total a pagar: ${total_a_pagar:.2f}")
else:
    print("No se ha comprado nada.")
