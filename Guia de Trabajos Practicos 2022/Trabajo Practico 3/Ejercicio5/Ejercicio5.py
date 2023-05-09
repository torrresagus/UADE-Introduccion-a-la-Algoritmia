#Ejercicio 5:Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 
#El costo básico del libro es de $500, más $3,20 por página con encua-dernación rústica. 
#Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $200. 
#Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-cuadernación que 
#incrementa el costo en otros $336. 
#Desarrollar un programa que calcule el costo de un libro dado el número de páginas.
CostoFinal = 0
CostoBasico = 500
CostoPorPagina = 3.20
AgregadoTela = 200
AgregadoEspecial = 336
Paginas = int(input("Ingresar la Cantidad de Paginas: "))
CostoFinal = CostoBasico + (Paginas * CostoPorPagina)
if Paginas > 300:
    CostoFinal = CostoFinal + AgregadoTela
    if Paginas > 600:
        CostoFinal = CostoFinal + AgregadoEspecial
    else:
        print("El costo final del libro es de $", CostoFinal)
else:
    print("El costo final del libro es de $", CostoFinal)
    
        

