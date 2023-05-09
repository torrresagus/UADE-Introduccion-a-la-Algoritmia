#Ejercicio 8:Leer una medida en metros e imprimir esta medida expresada en 
#centí-metros, pulgadas, pies y yardas. 
#Los factores de conversión son:
#1 pie = 12 pulgadas
#1 yarda = 3 pies
#1 pulgada = 2,54 cm.
#1 metro = 100 cm.

Metros = float(input("Ingresar una medida en metros: "))
if Metros > 0:
    
    #Una opcion es directamente convertir la medida en metros a las otras medidas
    #Centimetros = Metros * 100
    #Pulgadas = Metros * 100 / 2.54
    #Pies = Metros * 100 / 2.54 / 12
    #Yardas = Metros * 100 / 2.54 / 12 / 3

    #E imprimir los resultados
    #print("La medida", Metros, "m en centimetros es: ", round(Centimetros,2), "cm")
    #print("La medida", Metros, "m en pulgadas es: ", round(Pulgadas,2), "pulgadas")
    #print("La medida", Metros, "m en pies es: ", round(Pies,2), "pies")
    #print("La medida", Metros, "m en yardas es: ", round(Yardas,2), "yardas")


    #Otra opcion es convertir la medida en unidad de 1 metro y luego multiplicar por la medida deseada
    Centimetros = 100
    Pulgadas = Centimetros / 2.54
    Pies = Pulgadas / 12
    Yardas = Pies / 3
    
    
    print("La medida en centimetros es: ", round(Metros * Centimetros,2))
    print("La medida en pulgadas es: ", round(Metros * Pulgadas,2))
    print("La medida en pies es: ", round(Metros * Pies,2))
    print("La medida en yardas es: ", round(Metros * Yardas,2))
else:
    print("La medida no puede ser menor o igual a 0")
    


    