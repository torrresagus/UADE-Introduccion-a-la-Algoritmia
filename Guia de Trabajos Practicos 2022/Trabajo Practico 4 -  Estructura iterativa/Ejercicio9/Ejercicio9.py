#Ejercicio 9:Se desea analizar cuántos autos circulan con patente con numeración par y 
#cuántos con numeración impar en un día. Escribir un programa que permita in-gresar 
#la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe cuántos vehículos
#pasaron con numeración par y cuántos con numeración impar.

par = 0
impar = 0
patente = 0
while patente != -1:
    patente = int(input("Ingrese la terminacion de la patente: "))
    if patente > 9 or patente < -1:
        print("La patente ingresada es invalida")
    elif patente != -1:
        if patente % 2 == 0:
            par += 1
        else:
            impar += 1

print("La cantidad de patentes pares es: ", par)
print("La cantidad de patentes impares es: ", impar)
