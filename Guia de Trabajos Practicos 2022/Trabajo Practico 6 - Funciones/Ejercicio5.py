#Desarrollar la función signo(n), que reciba un número entero y devuelva 1, -1 o 
#0 según el valor recibido sea positivo, negativo o nulo.

def signo(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0
    
def main():
    num = int(input("Ingrese un numero: "))
    numSigno = signo(num)
    print("El signo del numero ", num, " es: ", numSigno)

main()
