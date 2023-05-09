#Calcular y devolver el Máximo Común Divisor de dos enteros no negativos, basándose en las siguientes fórmulas matemáticas:
#· MCD(X,X) = X
#· MCD(X,Y) = MCD(Y, X)
#· Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
#Ejemplo: MCD(40, 15) devuelve 5.

def mcd(numero1,numero2):
    if numero1 == numero2:
        return numero1
    elif numero1 > numero2:
        return mcd(numero1-numero2,numero2)
    else:
        return mcd(numero1,numero2-numero1)
    
def signo(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0

def main():
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    while signo(num) == -1 or signo(num2) == -1:
        print("Ingrese numeros positivos")
        num = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese otro numero: "))
        
    total = mcd(num,num2)
    print("El MCD de ", num, " y ", num2, " es: ", total)

main()