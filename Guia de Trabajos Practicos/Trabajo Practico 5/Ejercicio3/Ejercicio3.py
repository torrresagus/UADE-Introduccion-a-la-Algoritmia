#Ejercicio 3:Una empresa aplica el siguiente procedimiento en la comercialización de 
#sus pro-ductos:∑Aplica el precio base a la primera docena de unidades.
#Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
#El cálculo resultante sería:100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04
#Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor 
#total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada. 
#Al finalizar infor-mar: 
#Cantidad de ventas realizadas total.
#Cantidad de ventas en las que se aplicó un 10% de descuento.
#Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.

cantidad = 0
precioBase = 0
precioTotal = 0
precioPromedio = 0
cantVentas = 0
cantVentas10 = 0
cantVentas0 = 0
while cantidad != -1:
    cantidad = int(input("Ingrese una cantidad: "))
    if cantidad != -1:
        precioBase = int(input("Ingrese un precio base: "))
        if cantidad <= 12:
            precioTotal = precioBase * cantidad
            cantVentas0 += 1
        elif cantidad >= 13 and cantidad <= 100:
            precioTotal = precioBase * 12 + (precioBase * 0.9) * (cantidad - 12)
            cantVentas10 += 1
        else:
            precioTotal = precioBase * 12 + (precioBase * 0.9) * 88 + (precioBase * 0.75) * (cantidad - 100)
        cantVentas += 1
        precioPromedio = precioTotal / cantidad
        print("Precio total: ", precioTotal)
        print("Precio promedio: ", precioPromedio)

print("Cantidad de ventas realizadas total: ", cantVentas)
print("Cantidad de ventas en las que se aplicó un 10% de descuento: ", cantVentas10)
print("Cantidad de ventas en las que solo se aplicó el precio base, es decir que no se le realizaron descuentos: ", cantVentas0)
