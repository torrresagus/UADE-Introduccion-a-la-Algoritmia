Algoritmo Ejercicio9
	Escribir "Ingrese un Sueldo Basico: "
	Leer SueldoBasico
	Escribir "Ingrese Años de Antiguedad: "
	Leer Antiguedad
	Escribir "Ingrese Estado Civil:"
	Leer EstadoCivil
	SaldoBruto = 0
	SueldoNeto = 0
	Si EstadoCivil = 1 Entonces
		SueldoBruto = SueldoBasico * (0.05 * Antiguedad) + SueldoBasico
	SiNo
		Si EstadoCivil = 2 Entonces
			SueldoBruto = SueldoBasico * (0.07 * Antiguedad) + SueldoBasico
		SiNo
			Escribir "Ingreso un estado civil incorrecto"
		FinSi
	FinSi
	SueldoNeto = SueldoBruto - SueldoBruto * 0.17
	Escribir "El sueldo Basico es: ", SueldoBasico
	Escribir "Por tener ", Antiguedad, " Años de Antiguedad importe : +", SueldoBruto - SueldoBasico
	Escribir "Se desconto: "
	Escribir "Jubilacion: -", SueldoBruto * 0.11
	Escribir "Obra Social: -", SueldoBruto * 0.03
	Escribir "Sindicato: -", SueldoBruto * 0.03
	Escribir "El Sueldo Neto Final es :", SueldoNeto
FinAlgoritmo
