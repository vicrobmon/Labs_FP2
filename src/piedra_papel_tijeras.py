import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar ():

    """
    Lleva a cabo una ronda del juego piedra, papel o tijeras.
    Devuelve:
        Un mensaje con el resultado de la ronda.
    """

    eleccion_bot = ordenador_decide_jugada()
    eleccion_jugador = usuario_decide_jugada()
    ganador = determina_ganador(eleccion_jugador,eleccion_bot)
    print(f"El ordenador eligio {eleccion_bot}, y el jugador {eleccion_jugador}. {ganador}.")

def jugar_torneo ():
    control = False
    puntos_bot = 0
    puntos_jugador = 0

    while control != True:

        eleccion_bot = ordenador_decide_jugada()
        eleccion_jugador = usuario_decide_jugada()
        ganador = determina_ganador(eleccion_jugador,eleccion_bot)
        if ganador == 'Ganaste':
            puntos_jugador += 1
        elif ganador == 'Perdiste':
            puntos_bot += 1
        print(f"El ordenador eligio {eleccion_bot}, y el jugador {eleccion_jugador}. {ganador}.")
        print(f"Puntos jugador: {puntos_jugador}")
        print(f"Puntos ordenador: {puntos_bot}")

        if puntos_jugador == 3:
            print('Gana el jugador.')
            control = True
        elif puntos_bot == 3:
            print('Gana el ordenador.')
            control = True


    

if __name__ == "__main__":
    jugar_torneo()