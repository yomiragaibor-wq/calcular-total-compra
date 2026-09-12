def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio = 10
    cantidad = 3
    resultado = calcularTotal(precio, cantidad)
    print("El total de la compra es:", resultado)