#Ejercicio 5: Hora de jugar: Se requiere desarrollar un juego de preguntas, en que se puede responder 
#"si" o "no". Gana quien responde correctamente 3 preguntas. Si se responde mal alguna, no 
#se formula la siguiente y termina el juego (las preguntas son libres, las piensa Ud.)

# Ingreso de datos
pregunta1 = input("¿Es el cielo azul?: ")
if pregunta1 == "si":
    pregunta2 = input("¿Es el pasto verde?: ")
    if pregunta2 == "si":
        pregunta3 = input("¿Es el agua transparente?: ")
        if pregunta3 == "si":
            print("Ganaste")
        else:
            print("Perdiste")
    else:
        print("Perdiste")
else:
    print("Perdiste")
    