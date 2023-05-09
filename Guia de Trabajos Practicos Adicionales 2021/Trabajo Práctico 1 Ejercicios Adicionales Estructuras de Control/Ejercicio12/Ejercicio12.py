#ercicio 12: Escribir un algoritmo que solicite un nombre de usuario y una contraseña, y que no permita 
#seguir hasta que se introduzcan correctamente. Deberá repetirse hasta que el usuario sea 
#"admin" y la contraseña sea "1234", y en ese caso mostrar el mensaje “Login exitoso”. Tras 
#3 intentos sin acertar, se deberá mostrar un mensaje indicando que se agotaron esos 3 
#intentos y finaliza el programa.
#No se puede usar break ni continue.

#for de 0 a 2 de 1 en 1 
for range in (0,2,1):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "admin" and contraseña == "1234":
        print("Login exitoso")
        #break
        range = 3
    
if usuario != "admin" and contraseña != "1234":
    print("Se agotaron los 3 intentos")

