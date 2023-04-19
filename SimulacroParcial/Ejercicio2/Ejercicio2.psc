Algoritmo SimulacroParcial2
	Escribir "Ingrese Caracter: "
	Leer caracter_
	Mientras caracter_ <> " " Hacer
		Si caracter_ == "A" O caracter_ == "a" O caracter_ == "E" O caracter_ == "e" O caracter_ == "I" O caracter_ == "i" O caracter_ == "O" O caracter_ == "o" O caracter_ == "U" O caracter_ == "u" Entonces
			Escribir "VOCAL"
		SiNo
			Escribir "NO VOCAL"
		FinSi
		Escribir "Ingrese Caracter: "
		Leer caracter_
	FinMientras
FinAlgoritmo
