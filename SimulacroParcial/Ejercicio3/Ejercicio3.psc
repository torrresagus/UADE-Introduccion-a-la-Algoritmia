Algoritmo Ejercicio3
	Escribir "Ingrese el Numero de Documento: "
	Leer Documento
	cont = 0
	contMayores = 0
	Mientras Documento <> -1 Hacer
		Escribir "Ingrese la Edad: "
		Leer Edad
		Si cont == 0 Entonces
			primero =  Documento
		FinSi
		cont = cont + 1
		Si edad > 60 Entonces
			contMayores = contMayores + 1
		FinSi
		ultimo = Documento
		Escribir "Ingrese el Numero de Documento: "
		Leer Documento
	FinMientras
	Si cont >= 1 Entonces
		Escribir "El primer cliente atendido fue: " , primero
		Escribir "Cantidad de clientes atendidos en el dia: " , cont
		Escribir "Cantidad de clientes mayores a 60 años: " , contMayores
		Escribir "El ultimo cliente atendido en el dia fue: " , ultimo
	SiNo
		Escribir "No hubo clientes en el dia."
	FinSi
FinAlgoritmo
