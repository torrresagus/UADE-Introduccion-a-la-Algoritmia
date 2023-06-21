#Escribir una función para ingresar desde el teclado una serie de números entre A 
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la función mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la 
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A 
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como 
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.

def ingresar_numeros_entre_a_y_b(a, b):
    numeros = []
    
    while True:
        try:
            numero = int(input(f"Ingrese un número entre {a} y {b} (ingrese -1 para finalizar): "))
            
            if numero == -1:
                break

            if a <= numero <= b:
                numeros.append(numero)
            else:
                print("Error: el número ingresado está fuera del rango permitido. Intente nuevamente.")
                
        except ValueError:
            print("Error: valor no numérico ingresado. Por favor, ingrese un número válido.")

    return numeros

def main():
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    numeros = ingresar_numeros_entre_a_y_b(a, b)
    print(f"La lista de números ingresados es: {numeros}")

main()

