Algoritmo Ejercicio5
	Escribir "Ingrese la Inversion de la Persona 1: "
	Leer Inversion1
	Escribir "Ingrese la Inversion de la Persona 2: "
	Leer Inversion2
	Escribir "Ingrese la Inversion de la Persona 3: "
	Leer Inversion3
	Si Inversion1 > 0 Y Inversion2 > 0 Y Inversion3 > 0 Entonces
		TotalInversion = Inversion1 + Inversion2 + Inversion3
		Porcentaje1 = Inversion1 / TotalInversion * 100
		Porcentaje2 = Inversion2 / TotalInversion * 100
		Porcentaje3 = Inversion3 / TotalInversion * 100
		Escribir "El Porcentaje de la Persona1 es de: %", Porcentaje1
		Escribir "El Porcentaje de la Persona2 es de: %", Porcentaje2
		Escribir "El Porcentaje de la Persona3 es de: %", Porcentaje3
	SiNo
		Escribir "La Inversion no puede ser Igual o ‰enor que 0!"
	FinSi
FinAlgoritmo
