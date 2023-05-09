Algoritmo Ejercicio11
	Escribir 'Ingrese un numero binario de 4 cifras como un numero entero: '
	Leer NumeroBinario
	PrimerDigito <- trunc(NumeroBinario / 1000)
	NumeroBinario <- NumeroBinario MOD 1000
	SegundoDigito <- trunc(NumeroBinario / 100)
	NumeroBinario <- NumeroBinario MOD 100
	TercerDigito <- trunc(NumeroBinario / 10)
	NumeroBinario <- NumeroBinario MOD 10
	CuartoDigito <- trunc(NumeroBinario / 1)
	ValorDecimal = PrimerDigito * 2 ^ 3 + SegundoDigito * 2 ^ 2 + TercerDigito * 2 ^ 1 + CuartoDigito * 2 ^ 0
	Escribir "El numero en decimal es: ", ValorDecimal
FinAlgoritmo
