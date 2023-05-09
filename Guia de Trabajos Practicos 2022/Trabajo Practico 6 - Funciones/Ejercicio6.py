#Escribir la función comparar(a, b) que reciba como parámetros dos números enteros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si 
#el primero es menor que el segundo. En este ejercicio debe aprovecharse la función del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) 
#devuelve -1.

def comparar(numero1,numero2):
    if numero1 > numero2:
        return 1
    elif numero1 < numero2:
        return -1
    else:
        return 0


def main ():
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultadoComparacion = comparar(num,num2)
    print("El resultado de la comparacion es: ", resultadoComparacion)

main()
