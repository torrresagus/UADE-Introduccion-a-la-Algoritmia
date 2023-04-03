#Ejercicio 12:Escribir un programa para convertir un número binario de 4 cifras en un número decimal. 
#El número binario se ingresa como un solo número entero de cuatro dígitos.Procedimiento: 
#Para convertir un número binario a decimal es necesario multiplicar el valor de cada dígito por el número 2 
#elevado a un expo-nente. Este exponente se obtiene de la posición que ocupa el dígito dentro del número, 
#comenzando desde la derecha con la posición 0. To-dos estos resultados se suman para obtener el valor final. 
#Ejemplo: Con-vertir 1011 a decimal:13 02 11 10 = 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 11
NumeroBinario = int(input("Ingrese un numero binario de 4 cifras: "))
#Obtengo el primer digito
PrimerDigito = NumeroBinario // 1000
#Re asigno el valor de NumeroBinario para que no se acumule el resto de la division anterior
NumeroBinario = NumeroBinario % 1000
#Obtengo el segundo digito
SegundoDigito = NumeroBinario // 100
#Re asigno el valor de NumeroBinario para que no se acumule el resto de la division anterior
NumeroBinario = NumeroBinario % 100
#Obtengo el tercer digito
TercerDigito = NumeroBinario // 10
#Re asigno el valor de NumeroBinario para que no se acumule el resto de la division anterior
NumeroBinario = NumeroBinario % 10
#Obtengo el cuarto digito
CuartoDigito = NumeroBinario // 1
#Re asigno el valor de NumeroBinario para que no se acumule el resto de la division anterior
NumeroBinario = NumeroBinario % 1
#Calculo el valor decimal
ValorDecimal = PrimerDigito * 2 ** 3 + SegundoDigito * 2 ** 2 + TercerDigito * 2 ** 1 + CuartoDigito * 2 ** 0
print("El numero binario ingresado equivale a: ", ValorDecimal)
