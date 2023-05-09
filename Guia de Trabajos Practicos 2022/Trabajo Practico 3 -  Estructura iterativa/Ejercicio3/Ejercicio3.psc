Algoritmo Ejercicio3
	Escribir "Ingresar el Numero del Mes:"
	Leer NumeroMes
	Si NumeroMes > 0 & NumeroMes <= 12 Entonces
		Si NumeroMes == 1 Entonces
			Escribir NumeroMes, " corresponde al mes de Enero"
		SiNo
			Si NumeroMes == 2 Entonces
				Escribir NumeroMes, " corresponde al mes de Febrero"
			SiNo
				Si NumeroMes == 3 Entonces
					Escribir NumeroMes, " corresponde al mes de Marzo"
				SiNo
					Si NumeroMes == 4 Entonces
						Escribir NumeroMes, " corresponde al mes de Abril"
					SiNo
						Si NumeroMes == 5 Entonces
							Escribir NumeroMes, " corresponde al mes de Mayo"
						SiNo
							Si NumeroMes == 6 Entonces
								Escribir NumeroMes, " corresponde al mes de Junio"
							SiNo
								Si NumeroMes == 7 Entonces
									Escribir NumeroMes, " corresponde al mes de Julio"
								SiNo
									Si NumeroMes == 8 Entonces
										Escribir NumeroMes, " corresponde al mes de Agosto"
									SiNo
										Si NumeroMes == 9 Entonces
											Escribir NumeroMes, " corresponde al mes de Septiembre"
										SiNo
											Si NumeroMes == 10 Entonces
												Escribir NumeroMes, " corresponde al mes de Octubre"
											SiNo
												Si NumeroMes == 11 Entonces
													Escribir NumeroMes, " corresponde al mes de Noviembre"
												SiNo
													Si NumeroMes == 12 Entonces
														Escribir NumeroMes, " corresponde al mes de Dicembre"
													FinSi
												FinSi
											FinSi
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "El numero ingresado no corresponde a un mes del año"
	FinSi
FinAlgoritmo
