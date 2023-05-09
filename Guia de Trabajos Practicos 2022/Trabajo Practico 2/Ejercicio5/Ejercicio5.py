#Ejercicio 5:Tres personas invierten dinero para fundar una empresa (no necesaria-mente en partes iguales). 
#Calcular qué porcentaje invirtió cada una.
Inversion1 = float(input("Ingresar la Inversion de la Persona 1: "))
Inversion2 = float(input("Ingresar la Inversion de la Persona 2: "))
Inversion3 = float(input("Ingresar la Inversion de la Persona 3: "))
if Inversion1 > 0 and Inversion2 > 0 and Inversion3 > 0:
    TotalInversion = Inversion1 + Inversion2 + Inversion3
    Porcentaje1 = Inversion1 / TotalInversion * 100
    Porcentaje2 = Inversion2 / TotalInversion * 100
    Porcentaje3 = Inversion3 / TotalInversion * 100
    print("El porcentaje de la Persona 1 es: %", round(Porcentaje1,2))
    print("El porcentaje de la Persona 2 es: %", round(Porcentaje2,2))
    print("El porcentaje de la Persona 3 es: %", round(Porcentaje3,2))
else:
    print("La inversion no puede ser menor o igual a 0!")
