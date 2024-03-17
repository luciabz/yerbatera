#Funcion que calcula el descuento segun el metodo de pago elegido
def recargoFormaDePago(formaDePago):
        if formaDePago == 1:
            return -0.05
        elif formaDePago == 2:
            return 0.10
        else:
            print("Su forma de pago no admite descuento")
            return 0
        
#Funcion que calcula el descuento para aplicar segun la cantidad pedida
def descuentoCantidad(cantidad, total):
        if cantidad > 5:
            print("tiene 35% de descuento por haber comprado mas de 5 toneladas")
            return (total * 0.35)
        elif cantidad > 2:
            print("tiene 20% de descuento por haber comprado mas de 2 toneladas")
            return  (total * 0.2) 
        elif cantidad > 1:
            print("tiene 10% de descuento por haber comprado mas de una tonelada")
            return (total * 0.1) 
        else:
            print("Su cantidad no admite descuento a realizar")
            return 0
        
#Funcion que calcula el recargo adicional segun la distancia
def envio(distancia):
        if distancia <= 50:
            print ("hasta 50 km -> $ 5.000 adicional")
            return 5000
        elif distancia < 100:   
            print("hasta 100 km -> $ 10.500 adicional")
            return 10500
        elif distancia <200:       
            print("hasta 200 km -> $ 25.000 adicional")
            return 25000
        elif distancia > 200:       
            print("mas de 200 km -> precio de 200 km + $ 550 x km adicional")
            return 25000 + 550 * (distancia - 200)
        
"""
Funcion principal 
Solicita al cliente que y va guardando sus eleciones en variables, y llama a diferentes funciones apartes para 
llevar a cabo los calculos correspondientes
Se realizan las operaciones segun el tipo de yerba elegido, y finalmnete se imprime un resumen final.
"""

def main():
    print("Bienvenido a nuestro sistema de compras de yerba mate.")
    print("Los precios por tonelada son: $36.830 para hoja verde y $139.954 para yerba mate canchada.")
    tipo = int(input("Ingrese el tipo de yerba (1 para hoja verde, 2 para yerba mate canchada):\n"))
    print("Dependiendo la cantida de toneladas puede contar con los siguientes descuentos:")
    print("Mas de una tonelada tiene un 10% ")
    print("Mas de dos toneladas tiene un 20%")
    print("Mas de cinco toneladas tiene un 35%\n")
    cantidad = float(input("Ingrese la cantidad de toneladas a comprar: \n"))
    print("¿Como desea pagar? Si decide pagar por efectivo tiene un 5% de descuento adicional y si decide tarjeta de credito cuenta con un recargo del 10%\n")
    formaDePago = int(input("Ingrese la forma de pago 1.efectivo, 2.tarjeta de crédito, 3.pagaré): \n"))
    envioRespuesta = input("¿Desea envío a su planta? (si/no): \n")
    distancia=0
    if envioRespuesta.lower()== "si":
        distancia = float(input("Genial! Ingrese la distancia en kilómetros al lugar de entrega: \n"))
    print ("Gracias por comprar con nosotros.")
  
    precioBase = 36830 if tipo == 1 else 133994
    subtotal = precioBase * cantidad
    descuento = descuentoCantidad(cantidad,subtotal)
    recargoFormaPago = (subtotal - descuento) * recargoFormaDePago(formaDePago)
    recargoEnvio = envio(distancia) if envioRespuesta.lower() == "si" else 0
    total= subtotal-descuento + recargoEnvio + recargoFormaPago
                
    print(f"\nHa elegido el producto: {'hoja verde' if tipo == 1 else 'yerba Mate Canchada'} con un total de {subtotal}")
    print(f"Ha realizado una compra de {cantidad} toneladas, por lo tanto ha recibido un beneficio de ${descuento}")
    print(f"El método de pago elegido es: {'efectivo' if formaDePago == 1 else 'tarjeta de crédito' if formaDePago == 2 else 'pagaré'}. El descuento aplicado es: ${round(recargoFormaPago, 2)}")
    if envioRespuesta.lower() == "si":
        print(f"recargo por envio: ${recargoEnvio} por una distancia de: {distancia} km")
    print(f"El importe total es ${total}")
   
main()