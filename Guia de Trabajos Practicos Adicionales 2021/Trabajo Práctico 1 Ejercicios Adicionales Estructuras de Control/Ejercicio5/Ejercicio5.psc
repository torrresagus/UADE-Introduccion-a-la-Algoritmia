Algoritmo Ejericio5
	Escribir "Responder son si o no"
	Escribir "¿Es el cielo azul?"
	Leer respuesta1
	Si respuesta1 == "si" Entonces
		Escribir "¿Es el pasto verde?"
		Leer respuesta2
		Si respuesta2 == "si" Entonces
			Escribir "¿Es el agua transparente?"
			Leer respuesta3
			Si respuesta3 == "si" Entonces
				Escribir "Ganaste"
			SiNo
				Escribir "Perdiste"
			FinSi
		SiNo
			Escribir "Perdiste"
		FinSi
	SiNo
		Escribir "Perdiste"
	FinSi
FinAlgoritmo
