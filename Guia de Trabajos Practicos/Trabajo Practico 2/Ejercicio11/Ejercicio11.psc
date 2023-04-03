Algoritmo Ejercicio11
	Escribir 'Ingrese un Monto: '
	Leer Monto
	Billetes1000 <- trunc(Monto / 1000)
	Monto <- Monto MOD 1000
	Billetes500 <- trunc(Monto / 500)
	Monto <- Monto MOD 500
	Billetes100 <- trunc(Monto/100)
	Monto <- Monto MOD 100
	Billetes50 <- trunc(Monto/50)
	Monto <- Monto MOD 50
	Billetes10 <- trunc(Monto/10)
	Monto <- Monto MOD 10
	Billetes5 <- trunc(Monto/5)
	Monto <- Monto MOD 5
	Billetes1 <- trunc(Monto/1)
	Escribir 'El monto ingresado equivale a: ',Billetes1000,' Billetes de 1000, ',Billetes500,'Billetes de 500, ',Billetes100,'Billetes de 100, ',Billetes50,' Billetes de 50, ', Billetes10, " Billetes de 10 y ", Billetes1, "Billetes de 1"
FinAlgoritmo
