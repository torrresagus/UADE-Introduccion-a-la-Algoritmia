#Devolver True si el número entero recibido como primer parámetro es múltiplo 
#del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True 
#y esmultiplo(50, 3) devuelve False.

def esMultiplo(numero1,numero2):
    if numero1 % numero2 == 0:
        return True
    else:
        return False
    
def main():
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    total = esMultiplo(num,num2)
    if total:
        print("El numero ", num, " es multiplo de ", num2)
    else:
        print("El numero ", num, " no es multiplo de ", num2)
        

main()
