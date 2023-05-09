#Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.

def imprimirAsteriscos(numero):
    for i in range(numero):
        print("*")

def main():
    num = int(input("Ingrese un numero: "))
    imprimirAsteriscos(num)

main()
