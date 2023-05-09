# Escribir una función que reciba como parámetros un número de día, un número 
#de mes y un número de año y devuelva la cantidad de días que faltan hasta fin 
#de mes. Luego desarrollar tres programas para: 
#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir 
#la cantidad de días que faltan hasta fin de año.
#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir 
#la cantidad de días transcurridos en ese año hasta esa fecha.
#· Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuánto tiempo transcurrió entre ambas, expresando el resultado en 
#años, meses y días.
#Los tres programas deben realizar su trabajo a través de la función indicada al comienzo.

def esBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False
    
def cantidadDiasMes(mes,anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 12 or mes == 10:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and esBisiesto(anio):
        return 29
    else:
        return 28
    
def cantidadDiasFaltantes(dia,mes,anio):
    diasFaltantes = 0
    for i in range(mes,12):
        diasFaltantes += cantidadDiasMes(i,anio)
    diasFaltantes += cantidadDiasMes(mes,anio) - dia
    return diasFaltantes

def cantidadDiasTranscurridos(dia,mes,anio):
    diasTranscurridos = 0
    for i in range(1,mes):
        diasTranscurridos += cantidadDiasMes(i,anio)
    diasTranscurridos += dia
    return diasTranscurridos

def cantidadDiasEntreFechas(dia1,mes1,anio1,dia2,mes2,anio2):
    diasTranscurridos = 0
    diasTranscurridos += cantidadDiasFaltantes(dia1,mes1,anio1)
    diasTranscurridos += cantidadDiasTranscurridos(dia2,mes2,anio2)
    return diasTranscurridos

def main():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    diasFaltantes = cantidadDiasFaltantes(dia,mes,anio)
    print("La cantidad de dias faltantes hasta fin de año son: ", diasFaltantes)
    diasTranscurridos = cantidadDiasTranscurridos(dia,mes,anio)
    print("La cantidad de dias transcurridos hasta la fecha son: ", diasTranscurridos)
    dia2 = int(input("Ingrese el dia: "))
    mes2 = int(input("Ingrese el mes: "))
    anio2 = int(input("Ingrese el anio: "))
    diasEntreFechas = cantidadDiasEntreFechas(dia,mes,anio,dia2,mes2,anio2)
    print("La cantidad de dias entre las fechas son: ", diasEntreFechas)

main()

