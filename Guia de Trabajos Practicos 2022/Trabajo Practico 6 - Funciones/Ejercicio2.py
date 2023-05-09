#Dados dos parámetros enteros A y B, obtener AB
#(A elevado a la B) mediante 
#multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar. 
#Por ejemplo 43= 4 * 4 * 4.

def multiplicacion(numero1,numero2):
    resultado = 0
    for i in range(numero2):
        resultado += numero1
    return resultado

def potencia(numero1,numero2):
    resultado = 1
    for i in range(numero2):
        resultado = multiplicacion(resultado,numero1)
    return resultado

def main ():
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    total = potencia(num,num2)
    print("El resultado de la potencia es: ", total)
    
main()

