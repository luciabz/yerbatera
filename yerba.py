
def calcular_descuento(cantidad):
    if cantidad > 5:
        return 0.35
    elif cantidad > 2:
        return 0.20
    elif cantidad > 1:
        return 0.10
    else:
        return 0

def calcular_recargo_forma_pago(forma_pago):
    if forma_pago == 1:
        return -0.05
    elif forma_pago == 2:
        return 0.10
    else:
        return 0

def calcular_recargo_envio(distancia):
    if distancia > 200:
        return 25000 + 550 * (distancia - 200)
    elif distancia > 100:
        return 25000
    elif distancia > 50:
        return 10500
    else:
        return 5000

def main():
    print("Bienvenido a nuestro sistema de compras de yerba mate.")
    tipo = int(input("Ingrese el tipo de yerba (1 para hoja verde, 2 para yerba mate canchada): "))
    cantidad = float(input("Ingrese la cantidad de toneladas a comprar: "))
    forma_pago = int(input("Ingrese la forma de pago (1 para efectivo, 2 para tarjeta de crédito, 3 para pagaré): "))
    envio = input("¿Desea envío a su planta? (s/n): ")
    distancia = 0
    if envio.lower() == 's':
        distancia = float(input("Ingrese la distancia en km hasta su planta de procesamiento: "))

    precio_base = 36830 if tipo == 1 else 139954
    subtotal = precio_base * cantidad
    descuento = subtotal * calcular_descuento(cantidad)
    recargo_forma_pago = (subtotal - descuento) * calcular_recargo_forma_pago(forma_pago)
    recargo_envio = calcular_recargo_envio(distancia) if envio.lower() == 's' else 0
    total = subtotal - descuento + recargo_forma_pago + recargo_envio

    print(f"\nProducto: {'hoja verde' if tipo == 1 else 'yerba mate canchada'}")
    print(f"Total a comprar: {cantidad} toneladas")
    print(f"Beneficio por cantidad comprada: ${descuento}")
    print(f"Subtotal a pagar: ${subtotal}")
    print(f"Bonificación o recargo por forma de pago: ${recargo_forma_pago}")
    if envio.lower() == 's':
        print(f"Recargo por envío: ${recargo_envio} (distancia: {distancia} km)")
    print(f"Importe total: ${total}")

if __name__ == "__main__":
    main()
