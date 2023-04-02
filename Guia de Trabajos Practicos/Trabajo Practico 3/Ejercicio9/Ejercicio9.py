#Ejercicio 9:Diseñar un programa que calcule y muestre el sueldo neto de un empleado en 
#base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo 
#en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa 
#el sueldo en 7% del bruto por cada año de antigüedad. También se le realizan los siguientes descuentos: 
#Jubilación: 11%, Obra Social: 3%, Sindicato: 3%
#Como datos de entrada se ingresa por teclado el sueldo básico, antigüe-dad y estado civil 
#(1 si es soltero o 2 si es casado).
SueldoBasico = float(input("Ingresar el Sueldo Basico: "))
Antiguedad = int(input("Ingresar la Antiguedad: "))
EstadoCivil = int(input("Ingresar el Estado Civil (1-Soltero, 2-Casado): "))
SueldoNeto = 0
SueldoBruto = 0
if EstadoCivil == 1:
    SueldoBruto = SueldoBasico + SueldoBasico * (0.05 * Antiguedad)
elif EstadoCivil == 2:
    SueldoBruto = SueldoBasico + SueldoBasico * (0.07 * Antiguedad)
else:
    print("El Estado Civil ingresado no es valido!")

SueldoNeto = SueldoBruto - SueldoBruto * (0.11 + 0.03 + 0.03)
print("El Sueldo Basico es de $" , SueldoBasico)
print("Por tener ", Antiguedad, "años de antiguedad, se le incrementa el sueldo + $", SueldoBruto - SueldoBasico)
print("Se desconto:")
print("Jubilacion: $", SueldoBruto * 0.11)
print("Obra Social: $", SueldoBruto * 0.03)
print("Sindicato: $", SueldoBruto * 0.03)
print("El Sueldo Neto es de $", SueldoNeto)

