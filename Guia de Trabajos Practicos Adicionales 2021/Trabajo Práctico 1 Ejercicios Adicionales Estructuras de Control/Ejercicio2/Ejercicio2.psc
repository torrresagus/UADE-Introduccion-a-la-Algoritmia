Algoritmo Ejericio2
	Escribir "Ingrese la edad: "
	Leer edad
	Mientras edad <= 0 Hacer
		Escribir "Ingrese una edad valida: "
		Leer edad
	FinMientras
	Si edad >= 18 Entonces
		mayor = true
	SiNo
		mayor = falso
	FinSi
	Si mayor Entonces
		Escribir "Es mayor de edad"
	SiNo
		Escribir "Es menor de edad"
	FinSi
FinAlgoritmo
