Algoritmo Ejericio3
	Escribir "Ingrese el nombre del primer visitante"
	Leer nombre
	Escribir "Ingrese la edad del primer visitante"
	Leer edad
	Escribir "Ingrese la altura del primer visitante"
	Leer altura
	Escribir "Ingrese el nombre del segundo visitante"
	Leer nombre2
	Escribir "Ingrese la edad del segundo visitante"
	Leer edad2
	Escribir "Ingrese la altura del segundo visitante"
	Leer altura2
	Si edad >= 15 		y altura > 1.5 Entonces
		Si edad2 >= 15 y altura2 > 1.5 Entonces
			Escribir nombre, " y ", nombre2 , " pueden acceder a la montaña ruda"
		SiNo
			Escribir nombre, " puede acceder a la montaña ruda"
		FinSi
	SiNo
		Si edad2 >= 15 y altura2 > 1.5 Entonces
			Escribir nombre2, " puede acceder a la montaña ruda"
		SiNo
			Escribir "Ninguno puede acceder a la montaña rusa"
		FinSi
	FinSi
FinAlgoritmo
