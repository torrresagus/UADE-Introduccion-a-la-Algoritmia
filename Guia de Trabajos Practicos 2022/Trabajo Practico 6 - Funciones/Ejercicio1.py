#Escribir una función que reciba como parámetros dos números enteros. Calcular 
#y devolver el resultado de la multiplicación de ambos valores utilizando solamenete sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 .

def multiplicacion(numero1,numero2):
    resultado = 0
    for i in range(numero2):
        resultado += numero1
    return resultado

def main ():
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    total = multiplicacion(num,num2)
    print("El resultado de la multiplicacion es: ", total)
    
main()
