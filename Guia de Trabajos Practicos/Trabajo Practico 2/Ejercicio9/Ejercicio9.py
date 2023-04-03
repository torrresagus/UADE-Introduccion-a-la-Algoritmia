#vEjercicio 9:Una inmobiliaria paga a sus vendedores un salario de $50000, 
#más una comisión de $5000 por cada venta realizada, más el 5% del valor de las ventas. 
#Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. 
#Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas. 
NumeroVendedor = int(input("Ingrese el numero del vendedor: "))
Ventas = int(input("Ingrese la cantidad de ventas del Vendedor: "))
ValorVentasVendedor = int(input("Ingrese el valor total de las ventas del Vendedor: "))
Salario = 50000 + (5000 * Ventas) + (ValorVentasVendedor * 0.05)
print("El salario del vendedor numero", NumeroVendedor, " es: ", Salario)