import time, random
#funciones Conecta_4, turno_jugador, turno_pc, Ganador
def Conecta_4():
    tablero = {
        "F": ["F0", "F1", "F2", "F3", "F4", "F5", "F6"],
        "E": ["E0", "E1", "E2", "E3", "E4", "E5", "E6"],
        "D": ["D0", "D1", "D2", "D3", "D4", "D5", "D6"],
        "C": ["C0", "C1", "C2", "C3", "C4", "C5", "C6"],
        "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6"],
        "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6"]
    }
    posiciones_user=[]
    posiciones_pc=[]
    casillas_vert = ["A0","A1","A2","A3","A4","A5","A6","B0","B1","B2","B3","B4","B5","B6","C0","C1","C2","C3","C4","C5","C6","D0","D1","D2","D3","D4","D5","D6","E0","E1","E2","E3","E4","E5","E6","F0","F1","F2","F3","F4","F5","F6"]
    letras = ["A","B","C","D","E","F"]
    numeros = ["0","1","2","3","4","5","6"]
    posiciones_dichas=[]
    for cont in range(1, 100):
        time.sleep(0.03)
        print("Cargando...", cont, "%")
    time.sleep(1)
    print("La Oca ha cargado exitosamente!")
    time.sleep(1)
    decision_normas = input("Desea repasar las normas rápidamente? (SI/NO):")
    if decision_normas == "SI" or decision_normas == "Si" or decision_normas == "si" or decision_normas == "sI" or decision_normas == "s" or decision_normas == "S":
        print("Ok! Te recordare las normas.")
        time.sleep(3)
        print("El juego consiste en introducir fichas en un tablero vertical con el objetivo de alinear cuatro fichas consecutivas.")
        time.sleep(5)
        print("El tablero tendrá unas dimensiones de 7x6, y será este:")
        time.sleep(4)
        for x in tablero:
            print(tablero[x])
            time.sleep(0.2)
        time.sleep(5)
        print("Jugarás contra el PC, y ganará el primero que consiga alinear cuatro fichas, ya sea verticalmente, horizontalmente o diagonalmente.")
        time.sleep(7)
        print("Eso es todo.")
    time.sleep(2)
    print("Buena suerte!")
    time.sleep(2)
    x = input("Dime que ficha deseas elegir X/Y:")
    if (x == "X" or x=="x" or x == "Y" or x=="y"):
        if (x == "X" or x=="x"):
            x = "XX"
            z = "X"
            ord = "YY"
            t = "Y"
        elif (x == "Y" or x=="y"):
            x = "YY"
            z = "Y"
            ord = "XX"
            t = "X"
        print("Has elegido como ficha la letra:", z)
        time.sleep(2)
        print("El PC sera:", t)
        turno_jugador(x,tablero,casillas_vert,letras,numeros,posiciones_dichas,ord,posiciones_user,posiciones_pc)
    else:
        print("Error!, vuelve a intentarlo")
        Conecta_4()


def turno_jugador(posicion,tablero,casillas_vert,letras,numeros,posiciones_dichas,ord,posiciones_user,posiciones_pc):
    for x in tablero:
        print(tablero[x])
        time.sleep(0.2)
    time.sleep(1)
    casilla = input("Elige una casilla:")
    if casilla not in casillas_vert:
        print("Error! Casilla incorrecta")
        turno_jugador(posicion,tablero,casillas_vert,letras,numeros,posiciones_dichas,ord,posiciones_user,posiciones_pc)
    else:
        for z in range(len(letras)):
            for y in range(len(numeros)):
                if (casilla == letras[z]+numeros[y]):
                    letra_res = letras[z-1]
                    if (letra_res+numeros[y] in posiciones_dichas or letras[z] == "A"):
                        print("Posicion asignada correctamente.")
                        posiciones_dichas.append(casilla)
                        posiciones_user.append(casilla)
                        tablero[letras[z]][int(numeros[y])] = posicion
                        #time.sleep(1)
                        print("Tablero:")
                        for x in tablero:
                            print(tablero[x])
                            time.sleep(0.1)
                        if (True):  # VERTICAL
                            try:
                                if (letras[z - 1] + numeros[y] in posiciones_user and letras[z - 2] + numeros[y] in posiciones_user and letras[z - 3] + numeros[y] in posiciones_user):
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                        if (True):  # HORIZONTAL
                            try:
                                if (letras[z] + numeros[y - 1] in posiciones_user and letras[z] + numeros[y - 2] in posiciones_user and letras[z] + numeros[y - 3] in posiciones_user):  # a3@#
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z] + numeros[y - 1] in posiciones_user and letras[z] + numeros[y - 2] in posiciones_user and letras[z] + numeros[y + 1] in posiciones_user):  # a2
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z] + numeros[y - 1] in posiciones_user and letras[z] + numeros[y + 1] in posiciones_user and letras[z] + numeros[y + 2] in posiciones_user):  # a1
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z] + numeros[y + 1] in posiciones_user and letras[z] + numeros[y + 2] in posiciones_user and letras[z] + numeros[y + 3] in posiciones_user):  # a0
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                        if (True):  # DIAGONAL
                            try:
                                if (letras[z + 1] + numeros[y - 1] in posiciones_user and letras[z + 2] + numeros[y - 2] in posiciones_user and letras[z + 3] + numeros[y - 3] in posiciones_user):  # a3
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z - 1] + numeros[y + 1] in posiciones_user and letras[z + 1] + numeros[y - 1] in posiciones_user and letras[z + 2] + numeros[y - 2] in posiciones_user):  # b2
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z + 1] + numeros[y - 1] in posiciones_user and letras[z - 1] + numeros[y + 1] in posiciones_user and letras[z - 2] + numeros[y + 2] in posiciones_user):  # c1
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z - 1] + numeros[y + 1] in posiciones_user and letras[z - 2] + numeros[y + 2] in posiciones_user and letras[z - 3] + numeros[y + 3] in posiciones_user):  # d0
                                    ganador = "User"
                                    Ganador(ganador)
                            except:
                                pass
                    else:
                        print("Incorrecto!, Vuelve a intentarlo.")
                        turno_jugador(posicion,tablero,casillas_vert,letras,numeros,posiciones_dichas,ord,posiciones_user,posiciones_pc)
    print("Es el turno de PC.")
    time.sleep(2)
    for x in tablero:
        print(tablero[x])
        time.sleep(0.1)
    turno_pc(ord, tablero, casillas_vert, posiciones_dichas, letras, numeros,posicion,posiciones_user,posiciones_pc)




def turno_pc(ord,tablero,casillas_vert,posiciones_dichas,letras,numeros,posicion,posiciones_user,posiciones_pc):
    casilla = random.choice(casillas_vert)
    if (casilla in posiciones_dichas):
        turno_pc(ord,tablero,casillas_vert,posiciones_dichas,letras,numeros,posicion,posiciones_user,posiciones_pc)
    else:
        for z in range(len(letras)):
            for y in range(len(numeros)):
                if (casilla == letras[z]+numeros[y]):
                    letra_res = letras[z-1]
                    if (letra_res + numeros[y] in posiciones_dichas or letras[z] == "A"):
                        posiciones_pc.append(casilla)
                        posiciones_dichas.append(casilla)
                        print("El PC ha escogido la casilla:", casilla)
                        time.sleep(2)
                        tablero[letras[z]][int(numeros[y])] = ord
                        time.sleep(1)
                        print("Tablero:")
                        for x in tablero:
                            print(tablero[x])
                            time.sleep(0.2)
                        if (True):  # VERTICAL
                            try:
                                if (letras[z - 1] + numeros[y] in posiciones_pc and letras[z - 2] + numeros[y] in posiciones_pc and letras[z - 3] + numeros[y] in posiciones_pc):
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                        if (True):  # HORIZONTAL
                            try:
                                if (letras[z] + numeros[y - 1] in posiciones_pc and letras[z] + numeros[y - 2] in posiciones_pc and letras[z] + numeros[y - 3] in posiciones_pc):  # a3@#
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z] + numeros[y - 1] in posiciones_pc and letras[z] + numeros[y - 2] in posiciones_pc and letras[z] + numeros[y + 1] in posiciones_pc):  # a2
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z] + numeros[y - 1] in posiciones_pc and letras[z] + numeros[y + 1] in posiciones_pc and letras[z] + numeros[y + 2] in posiciones_pc):  # a1
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z] + numeros[y + 1] in posiciones_pc and letras[z] + numeros[y + 2] in posiciones_pc and letras[z] + numeros[y + 3] in posiciones_pc):  # a0
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                        if (True):  # DIAGONAL
                            try:
                                if (letras[z + 1] + numeros[y - 1] in posiciones_pc and letras[z + 2] + numeros[y - 2] in posiciones_pc and letras[z + 3] + numeros[y - 3] in posiciones_pc):  # a3
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z - 1] + numeros[y + 1] in posiciones_pc and letras[z + 1] + numeros[y - 1] in posiciones_pc and letras[z + 2] + numeros[y - 2] in posiciones_pc):  # b2
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z + 1] + numeros[y - 1] in posiciones_pc and letras[z - 1] + numeros[y + 1] in posiciones_pc and letras[z - 2] + numeros[y + 2] in posiciones_pc):  # c1
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                            try:
                                if (letras[z - 1] + numeros[y + 1] in posiciones_pc and letras[z - 2] + numeros[y + 2] in posiciones_pc and letras[z - 3] + numeros[y + 3] in posiciones_pc):  # d0
                                    ganador = "PC"
                                    Ganador(ganador)
                            except:
                                pass
                    else:
                        turno_pc(ord,tablero,casillas_vert,posiciones_dichas,letras,numeros,posicion,posiciones_user,posiciones_pc)
    print("Es tu turno.")
    time.sleep(2)
    turno_jugador(posicion,tablero,casillas_vert,letras,numeros,posiciones_dichas,ord,posiciones_user,posiciones_pc)

def Ganador(x):
    time.sleep(4)
    if(x == "User"):
        print("Felicidades, has ganado la partida!")
    else:
        print("PC ha ganado la partida!")
    time.sleep(4)
    print("Volviendo al menu principal.")
    from MAIN_aka_Menu_principal import menu
    menu()



