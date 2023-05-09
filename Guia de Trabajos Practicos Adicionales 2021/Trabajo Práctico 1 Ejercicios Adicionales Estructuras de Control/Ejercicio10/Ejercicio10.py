#Ejercicio 10: Una fábrica produce bicicletas de paseo y de montaña. Para construir una bicicleta de paseo 
#se necesita 1.5 kg de acero, y para construir una bicicleta de montaña se necesita 2kg de 
#acero. La fábrica vende las bicicletas de paseo a $16000 y las de montaña a $18000. Se pide: 
#ingresar las cantidades de bicicletas a producir (de paseo y montaña). Suponga que la fábrica 
#dispone de 80kg de acero para su producción. Informar si la cantidad de acero disponible en 
#la fábrica es suficiente para las cantidades de bicicletas ingresadas. Si no es suficiente, indicar 
#la cantidad faltante de acero necesaria para producirlas. Verificar que las cantidades 
#ingresadas sean valores mayores o iguales a 0 (cero).

# Ingreso de datos
bicicletas_paseo = int(input("Ingrese la cantidad de bicicletas de paseo a producir: "))
bicicletas_montania = int(input("Ingrese la cantidad de bicicletas de montaña a producir: "))
acero_disponible = 80

# Cálculo de la cantidad de acero requerida
acero_requerido = (bicicletas_paseo * 1.5) + (bicicletas_montania * 2)

# Salida de datos
if acero_requerido <= acero_disponible:
    print("La cantidad de acero disponible es suficiente para producir las bicicletas ingresadas")
else:
    print("La cantidad de acero disponible no es suficiente para producir las bicicletas ingresadas")
    print("La cantidad de acero faltante es:", acero_requerido - acero_disponible)
