#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia) en
#una lista y muestre por pantalla el mensaje "Yo estudio «asignatura>", donde <asignatura> es cada una de las asignaturas
#de la lista. Ejemplo:
#Yo estudio Matemáticas
#Yo estudio Física
#Yo estudio Química
#Yo estudio Historia

#Nota: EI ingreso de las asignaturas debe ser por teclado y finaliza cuando se ingresa eI carácter • (asterisco). Se deben
#utilizar mínimo tres funciones, para el programa principal, para la carga de la lista y para visualizar los mensajes por
#pantalla.

def cargar_asignaturas():
    asignaturas = []
    asignatura = input("Ingrese una asignatura (o * para terminar): ")
    while asignatura != "*":
        asignaturas.append(asignatura)
        asignatura = input("Ingrese una asignatura (o * para terminar): ")
    return asignaturas

def mostrar_mensajes(asignaturas):
    for i in range(len(asignaturas)):
        print("Yo estudio", asignaturas[i])

def main():
    asignaturas = cargar_asignaturas()
    mostrar_mensajes(asignaturas)

main()
