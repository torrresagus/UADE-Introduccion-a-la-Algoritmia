#Ejercicio 6:Una remisería requiere un programa que calcule el precio de un viaje a partir de la cantidad de kilómetros 
#que desea recorrer el usuario. Para eso cuenta con la siguiente tarifa:
#Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no alcanza este mínimo.
#Si recorre entre 0 y 10 km: $30 por km
#Si recorre 10 km o más: $20 por km
CostoFinal = 0
CostoMinimo = 250
CostoHasta10Km = 30
CostoMas10km = 20
Kilometros = int(input("Ingresar la Cantidad de Kilometros: "))

if Kilometros > 0:
    if Kilometros > 10:
        CostoFinal = (Kilometros * CostoMas10km)
        print("El costo final del viaje es de $", CostoFinal)
    else:
        if (Kilometros * CostoHasta10Km) > CostoMinimo:
            CostoFinal = (Kilometros * CostoHasta10Km)
            print("El costo final del viaje es de $", CostoFinal)
        else:
            CostoFinal = CostoMinimo
            print("El costo final del viaje es de $", CostoFinal)
else:
    print("Ingreso un Numero Incorrecto!")

