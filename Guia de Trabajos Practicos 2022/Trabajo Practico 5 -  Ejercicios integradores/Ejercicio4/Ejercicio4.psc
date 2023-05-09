Algoritmo Ejercicio4
	descuento = 0
	multa = 0
	Escribir "Ingrese numero de Cliente: "
	Leer numeroCliente
	Escribir "Ingrese Total de la Factura: "
	Leer totalFactura
	Si (totalFactura * 0.02) < 200 Entonces
		descuento = 200
	SiNo
		descuento = totalFactura * 0.02
	FinSi
	Si (totalFactura * 0.1) < 350 Entonces
		multa = 350
	SiNo
		multa = totalFactura * 0.1
	FinSi
	Escribir "Numero de Cliente: ", numeroCliente
	Escribir "Precio a pagar en los primeros 10 dias del mes:", totalFactura - descuento
	Escribir "Precio a pagar en los siguientes 10 dias del mes:", totalFactura
	Escribir "Precio a pagar despues del dia 20 del mes:", totalFactura + multa
FinAlgoritmo
