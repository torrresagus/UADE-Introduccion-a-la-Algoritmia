#Obtener el dígito central de un número entero pasado como parámetro, sólo si la 
#cantidad de dígitos es impar. Si la longitud fuera par devolver -1. Ejemplo: 
#digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1

def paridad(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
def digitocentral(numero):
    num_original = numero
    if numero < 0:
        numero = numero * -1
    contador = 0
    while numero > 0:
        contador += 1
        numero = numero // 10
    if paridad(contador):
        return -1
    else:
        if num_original < 0:
            num_original = num_original * -1
        for i in range(contador//2 + 1):
            digito = num_original % 10
            num_original = num_original // 10
        return digito
    
def main():
    num = int(input("Ingrese un numero: "))
    digito = digitocentral(num)
    print("El digito central es: ", digito)

main()
