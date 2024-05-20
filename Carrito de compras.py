# Diccionario con productos y precios
productos = {
    1: ("Manzanas", 0.5),
    2: ("Plátanos", 0.25),
    3: ("Naranjas", 0.6),
    4: ("Leche", 1.2),
    5: ("Pan", 1.0),
    6: ("Carne", 4.5),
    7: ("Pollo", 3.0),
    8: ("Huevos", 2.0)
}

carrito = []
total = 0

print("Bienvenido al supermercado. Estos son los productos disponibles:")
for numero, (producto, precio) in productos.items():
    print(f"{numero}. {producto} - ${precio:.2f}")

mientras_compra = True
while mientras_compra:
    numero_producto = int(input("\nIngresa el número del producto que deseas comprar (o 0 para finalizar): "))
    if numero_producto == 0:
        mientras_compra = False
    elif numero_producto in productos:
        producto, precio = productos[numero_producto]
        cantidad = int(input(f"¿Cuántas {producto} deseas comprar? "))
        costo = precio * cantidad
        carrito.append((producto, cantidad, costo))
        total += costo
        print(f"{cantidad} {producto} han sido agregados al carrito por un costo de ${costo:.2f}.")
        
        # Mostrar el carrito actual
        print("\nCarrito actual:")
        for producto, cantidad, costo in carrito:
            print(f"{cantidad} {producto} - ${costo:.2f}")
    else:
        print(f"Disculpa, el número {numero_producto} no corresponde a ningún producto.")

print("\nResumen de tu compra:")
for producto, cantidad, costo in carrito:
    print(f"{cantidad} {producto} - ${costo:.2f}")
print(f"\nTotal a pagar: ${total:.2f}")