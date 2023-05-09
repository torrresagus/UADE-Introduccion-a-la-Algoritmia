#La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente 
#fórmula de Newton:
#donde a es una aproximación a n. Al aplicar repetidamente esta fórmula reemplazando a por la aproximación obtenida en el paso anterior, se obtiene cada vez 
#una aproximación mejor. Desarrollar un programa que calcule la raíz cuadrada 
#aproximada de un número entero positivo n utilizando como primera aproximación a n/2. Detener el proceso cuando la diferencia entre dos cálculos sucesivos 
#sea menor a 0,0001.

def raizCuadrada(numero):
    aproximacion = numero/2
    while True:
        aproximacion2 = (aproximacion + numero/aproximacion)/2
        if abs(aproximacion - aproximacion2) < 0.0001:
            break
        aproximacion = aproximacion2
    return aproximacion

def main():
    num = int(input("Ingrese un numero: "))
    resultado = raizCuadrada(num)
    print("La raiz cuadrada de ", num, " es: ", resultado)

main()
