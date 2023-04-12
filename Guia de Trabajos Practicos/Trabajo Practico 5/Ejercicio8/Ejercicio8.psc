Algoritmo Ejercicio8
	Escribir "Ingrese la cantidad de empleados: "
	Leer cantidadEmpleados
	gananMasDe200000 <- 0
	gananMenosDe50000C3 <- 0
	sueldoMasBajo <- 0
	promedioSueldos <- 0
	sueldoTotalCategoria1 <- 0
	sueldoTotalCategoria2 <- 0
	sueldoTotalCategoria3 <- 0
	sueldoTotal <- 0
	legajoMasGana <- 0
	
	Para i <- 1 Hasta cantidadEmpleados Con Paso 1 Hacer
		Escribir "Ingrese el legajo del empleado: "
		Leer legajo
		Escribir "Ingrese la categoria del empleado: "
		Leer categoria
		Escribir "Ingrese el salario del empleado: "
		Leer salario
		sueldoTotal <- sueldoTotal + salario
		
		Si salario > 200000 Entonces
			gananMasDe200000 <- gananMasDe200000 + 1
		Fin Si
		Si salario < 50000 y categoria = 3 Entonces
			gananMenosDe50000C3 <- gananMenosDe50000C3 + 1
		Fin Si
		Si i = 1 Entonces
			sueldoMasBajo <- salario
			legajoMasGana <- legajo
		Sino
			Si salario < sueldoMasBajo Entonces
				sueldoMasBajo <- salario
			Fin Si
			Si salario > sueldoMasBajo Entonces
				legajoMasGana <- legajo
			Fin Si
		Fin Si
		Si categoria = 1 Entonces
			sueldoTotalCategoria1 <- sueldoTotalCategoria1 + salario
		Fin Si
		Si categoria = 2 Entonces
			sueldoTotalCategoria2 <- sueldoTotalCategoria2 + salario
		Fin Si
		Si categoria = 3 Entonces
			sueldoTotalCategoria3 <- sueldoTotalCategoria3 + salario
		Fin Si
	Fin Para
	
	promedioSueldos <- sueldoTotal / cantidadEmpleados
	
	Escribir "El importe total de salarios pagados por la empresa es: ", sueldoTotal
	Escribir "La cantidad de empleados que ganan mas de $200000 es: ", gananMasDe200000
	Escribir "La cantidad de empleados que ganan menos de $50000 y cuya categoria es 3 es: ", gananMenosDe50000C3
	Escribir "El legajo del empleado que mas gana es: ", legajoMasGana
	Escribir "El sueldo mas bajo es: ", sueldoMasBajo
	Escribir "El importe total de sueldos por cada categoria es: "
	Escribir "Categoria 1: ", sueldoTotalCategoria1
	Escribir "Categoria 2: ", sueldoTotalCategoria2
	Escribir "Categoria 3: ", sueldoTotalCategoria3
	Escribir "El salario promedio es: ", promedioSueldos	
FinAlgoritmo
