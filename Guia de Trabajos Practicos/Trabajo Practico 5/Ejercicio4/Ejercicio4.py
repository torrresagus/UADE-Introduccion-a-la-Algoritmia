#Ejercicio 4:Una empresa factura a sus clientes el último día de cada mes. 
#Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, 
#tiene un descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
#Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura, mientras 
#que si paga después del día 20 deberá abonar una multa de $350 o del 10% de su factura, lo que resulte mayor. 
#Escribir un programa que lea el número del cliente y el total de la factura, y emita un informe donde cons-te el 
#número del cliente y los tres importes que podría abonar según la fecha de pago.

numeroCliente = int(input("Ingrese un número de cliente: "))
totalFactura = int(input("Ingrese el total de la factura: "))
descuento = 0
multa = 0

print("Número de cliente: ", numeroCliente)

if ( totalFactura * 0.02 ) < 200:
    descuento = 200
else:
    descuento = totalFactura * 0.02
if (totalFactura * 0.1) < 350:
    multa = 350
else:
    multa = totalFactura * 0.1

print("Precio a pagar en los primeros 10 días del mes siguiente: ", totalFactura - descuento)
print("Precio a pagar en los siguientes 10 días del mes siguiente: ", totalFactura)
print("Precio a pagar después del día 20 del mes siguiente: ", totalFactura + multa)


