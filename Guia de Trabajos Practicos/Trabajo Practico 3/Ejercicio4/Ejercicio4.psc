Algoritmo Ejercicio4
	Escribir "Ingresar Nota del Parcial 1:"
	Leer Nota1
	Si Nota1 > 0 Y Nota1 <= 10 Entonces
		Escribir "Ingresar Nota del Parcial 2:"
		Leer Nota2
		Si Nota2 > 0 Y Nota2 <= 10 Entonces
			Si Nota1 >= 7 Y Nota2 >= 7 Entonces
				Escribir "El Alumno Promocino"
			SiNo
				Si Nota1 >= 4 Y Nota2 >= 4  Entonces
					Escribir "El Alumno aprobo"
				SiNo
					Escribir "El Alumno no aprobo, debe recuperar"
				FinSi
			FinSi
		SiNo
			Escribir "La nota: ", Nota2, " del parcial 2 no es valida" 
		FinSi
	SiNo
		Escribir "La nota: ", Nota1, " del parciial 1 no es valida" 
	FinSi
FinAlgoritmo
