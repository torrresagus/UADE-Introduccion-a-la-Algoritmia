Algoritmo Ejercicio1
	sumaMenores = 0
	sumaMayores = 0
	cantMenores = 0
	cantMayores = 0
	edad = 0
	Mientras edad <> -1 Hacer
		Escribir "Ingrese una edad: "
		Leer edad
		Si edad >= 0 & edad <= 100 Entonces
			Si edad < 18 Entonces
				sumaMenores = sumaMenores + edad
				cantMenores = cantMenores + 1
			SiNo
				sumaMayores = sumaMayores + edad
				cantMayores = cantMayores + 1
			FinSi
		SiNo
			Escribir "Ingreso una edad invalida!"
		FinSi
	FinMientras
	promedioMenores = sumaMenores/ cantMenores
	promedioMayores = sumaMayores / cantMayores
	Escribir "Cantidad de menores de 18 años: ", cantMenores
	Escribir "Cantidad de mayores de 18 años: ", cantMayores
	Escribir "Promedio Mayores: ", promedioMayores
	Escribir "Promedio Menores: ", promedioMenores
FinAlgoritmo
