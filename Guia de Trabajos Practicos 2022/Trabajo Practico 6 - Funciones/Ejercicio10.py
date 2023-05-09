#Extraer un dígito de un número. La función recibe como parámetros dos números 
#enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea 
#obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si 
#no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o 
#negativo. Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) 
#devuelve -1.
#sin usar str ni listas

def extraerDigito(numero, cifra):
    if numero < 0:
        numero = numero * -1
    if cifra < 0:
        cifra = cifra * -1
    if cifra > numero:
        return -1
    else:
        for i in range(cifra):
            digito = numero % 10
            numero = numero // 10
        return digito
    
def main():
    num = int(input("Ingrese un numero: "))
    cifra = int(input("Ingrese la cifra que desea obtener: "))
    digito = extraerDigito(num,cifra)
    print("El digito es: ", digito)

main()
