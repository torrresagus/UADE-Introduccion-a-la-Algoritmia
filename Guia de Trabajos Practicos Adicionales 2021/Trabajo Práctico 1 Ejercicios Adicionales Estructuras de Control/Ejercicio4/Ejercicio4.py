#Ejercicio 4: Un albañil necesita contar con un sistema que le permita ingresar las medidas de un ambiente 
#rectangular, tamaño de una puerta y una ventana, y el tamaño de los dos lados de una 
#cerámica y le informe:
#a. Cantidad de cerámicas requeridas para colocar en las cuatro paredes del ambiente.
#b. Ingresando el costo por paquete y la cantidad de cerámicas por paquete, mostrar el 
#costo total en cerámicas.

# Ingreso de datos
largo = float(input("Ingrese el largo del ambiente: "))
ancho = float(input("Ingrese el ancho del ambiente: "))
alto = float(input("Ingrese el alto del ambiente: "))

alto_puerta = float(input("Ingrese el alto de la puerta: "))
ancho_puerta = float(input("Ingrese el ancho de la puerta: "))

alto_ventana = float(input("Ingrese el alto de la ventana: "))
ancho_ventana = float(input("Ingrese el ancho de la ventana: "))

alto_ceramica = float(input("Ingrese el alto de la cerámica: "))
ancho_ceramica = float(input("Ingrese el ancho de la cerámica: "))

precio_paquete = float(input("Ingrese el precio del paquete de cerámicas: "))
cantidad_paquete = int(input("Ingrese la cantidad de cerámicas por paquete: "))

# Cálculo de la cantidad de cerámicas requeridas
# Cálculo de la cantidad de cerámicas requeridas para el largo
ceramicas_largo = (largo - ancho_puerta - ancho_ventana) / ancho_ceramica
# Cálculo de la cantidad de cerámicas requeridas para el ancho
ceramicas_ancho = (ancho - alto_puerta - alto_ventana) / alto_ceramica
# Cálculo de la cantidad de cerámicas requeridas para las cuatro paredes
ceramicas = 2 * (ceramicas_largo + ceramicas_ancho)
# Cálculo del costo total en cerámicas
costo_total = (ceramicas / cantidad_paquete) * precio_paquete
# Salida de datos
print("La cantidad de cerámicas requeridas es: ", ceramicas)
print("El costo total en cerámicas es: ", costo_total)
