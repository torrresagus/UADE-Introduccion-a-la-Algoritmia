Algoritmo Ejercicio3
	cantidad = 0
	precioBase = 0
	precioTotal = 0
	precioPromedio = 0
	cantVentas0 = 0
	cantVentas10 = 0
	cantVentas = 0
	Mientras cantidad <> -1 Hacer
		Escribir "Ingrese Cantidad: "
		Leer cantidad
		Si cantidad <> -1 Entonces
			Escribir "Ingrese Precio Base: "
			Leer precioBase
			Si cantidad <= 12 Entonces
				precioTotal = precioBase * cantidad
				cantVentas0 = cantVentas0 + 1
			SiNo
				Si cantidad >= 13 & cantidad <= 100 Entonces
					precioTotal = precioBase * 12 + (precioBase * 0.9) * (cantidad - 12)
					cantVentas10 = cantVentas + 1
				SiNo
					precioTotal = precioBase * 12 + (precioBase * 0.9) * 88 + (precioBase * 0.75) * (cantidad - 100)
				FinSi
			FinSi
			cantVentas = cantVentas + 1
			precioPromedio = precioTotal / cantidad
			Escribir "Precio Total: ", precioTotal
			Escribir "Precio Promedio: ", precioPromedio
		FinSi
	FinMientras
	Escribir "Cantidad de ventas Realizadas total: ", cantVentas
	Escribir "Cantidad de ventas en las que solo se aplico un 10% de Descuento: ", cantVentas10
	Escribir "Cantidad de ventas en las que solo se aplico el precio base: ", cantVentas0
FinAlgoritmo
