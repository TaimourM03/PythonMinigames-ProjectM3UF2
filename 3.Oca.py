#VERSION FINAL 21/03/22
#funciones Oca, turno_PC, turno_USER, Ganador
import random,time
def Oca():
    tablero_normas = {
        8: ["22", "21", "20", "19", "18", "17", "16", "15"],
        7: ["23", "43", "42", "41", "40", "39", "38", "14"],
        6: ["24", "44", "57", "56", "55", "54", "37", "13"],
        5: ["25", "45", "58", "63", "62", "53", "36", "12"],
        4: ["26", "46", "59", "60", "61", "52", "35", "11"],
        3: ["27", "47", "48", "49", "50", "51", "34", "10"],
        2: ["28", "29", "30", "31", "32", "33", "34", "09"],
        1: ["01", "02", "03", "04", "05", "06", "07", "08"]
    }
    JU = 1
    PC = 1
    casillas_especiales = ["05", "09", "14", "18", "23", "27", "32", "36", "41", "45", "50", "54", "59", "63"]
    casillas_puente = ["06", "12"]
    posada_pc = ""
    posada_user = ""
    posada_user_3 = ""
    posada_pc_3 = ""
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
        print("El juego consiste en tirar un dado, y avanzar tu ficha de acuerdo al número obtenido.")
        time.sleep(4)
        print("Jugaras contra el PC, y ambos os iréis moviendo por un tablero de 63 casillas con forma de Caracol, como este:")
        time.sleep(5)
        for x in tablero_normas:
            print(tablero_normas[x])
            time.sleep(0.2)
        time.sleep(4)
        print("En este tablero, hay varias casillas con cualidades especiales, como por ejemplo volver a tirar.")
        time.sleep(4)
        print("Veamos las casillas especiales y sus cualidades:")
        time.sleep(4)
        #OCAS
        print("Las siguientes casillas son Ocas:", "[05, 09, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59, 63]")
        time.sleep(7)
        print("Si caes en una Oca, avanzaras hasta la siguiente Oca, y también volverás a tirar Dado.")
        time.sleep(5)
        #PUENTES
        print("También tenemos unas casillas llamadas Puentes, que están situadas en [6, 12]")
        time.sleep(6)
        print("Si caes en un el puente 6, avanzaras al 12, y volverás a tirar.")
        time.sleep(5)
        print("Sin embargo, si caes en el puente 12, retrocederás al puente 6, y volverás a tirar.")
        time.sleep(5)
        #POSADA
        print("Otra casilla especial, es la numero 19, llamada la Posada.")
        time.sleep(5)
        print("Si caes en dicha casilla, pierdes dos turnos.")
        time.sleep(5)
        #EL POZO
        print("Una casilla similar a la anterior, situada en la casilla 31, es el Pozo de Bronce.")
        time.sleep(5)
        print("En esta casilla, se pierden tres turnos.")
        time.sleep(5)
        #LABERINTO
        print("Otra casilla especial, es el Laberinto, situada en la 42.")
        time.sleep(5)
        print("En esta casilla, se retrocede a la casilla numero 30.")
        time.sleep(5)
        #LA CÁRCEL
        print("En la número 52, esta situada la Cárcel.")
        time.sleep(5)
        print("En esta casilla, perderás 3 turnos")
        time.sleep(5)
        #LA CALAVERA
        print("La Calavera, esta situada en la casilla número 58.")
        time.sleep(5)
        print("Si caes, en esta casilla, vuelves a la casilla de inicio (1).")
        time.sleep(5)
        print("Esas son todas las casillas especiales.")
        time.sleep(5)
        print("Ganara la partida el primero que consiga llegar a la última casilla (63).")
        time.sleep(5)
        print("En caso de que te pases de la casilla 63, retrocederás la cantidad que te sobre del dado.")
        time.sleep(5)
        print("Esas són todas las normas.")
    time.sleep(2)
    print("Buena suerte!")
    time.sleep(2)
    turno_USER(casillas_especiales,PC,casillas_puente,JU,posada_user,posada_pc,posada_user_3,posada_pc_3)

def turno_PC(casillas_especiales,JU,casillas_puente,PC,posada_pc,posada_user,posada_user_3,posada_pc_3):
    vuelve_a_tirar = ""
    tablero = {
        8: ["22", "21", "20", "19", "18", "17", "16", "15"],
        7: ["23", "43", "42", "41", "40", "39", "38", "14"],
        6: ["24", "44", "57", "56", "55", "54", "37", "13"],
        5: ["25", "45", "58", "63", "62", "53", "36", "12"],
        4: ["26", "46", "59", "60", "61", "52", "35", "11"],
        3: ["27", "47", "48", "49", "50", "51", "34", "10"],
        2: ["28", "29", "30", "31", "32", "33", "34", "09"],
        1: ["01", "02", "03", "04", "05", "06", "07", "08"]
    }
    for x in range(1):
        time.sleep(1)
        print("Turno del PC")
        dp1 = random.randint(1, 6)
        PC = int(PC) + dp1
        if PC>63:
            PC = PC - dp1
            for x in range(dp1):
                if (PC<63):
                    PC = PC + 1
                elif (PC==63):
                    for z in range(dp1-x):
                        PC = PC - 1
                    break

        print("PC ha tirado el dado.")
        time.sleep(2)
        print("El dado salio:", dp1,",El PC esta en la casilla:", PC)
        time.sleep(1)
        for m in range(len(casillas_especiales)): #EN CASO DE QUE LA POSICIÓN EN LA QUE ESTE EL PC CAIGA EN OCA:
            if "0" + str(PC) == casillas_especiales[m]:
                PC = casillas_especiales[m + 1]
                time.sleep(3)
                print("De oca en oca y tiro porque me toca")
                time.sleep(2)
                print("Al PC le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                vuelve_a_tirar = "si"
                time.sleep(3)
                break
            elif str(PC) == casillas_especiales[m] and PC < 63:
                PC = casillas_especiales[m + 1]
                time.sleep(2)
                print("Al PC le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                vuelve_a_tirar = "si"
                time.sleep(3)
                break

        if PC == 6:  # EN CASO DE QUE PC ESTE EN ALGUNA CASILLA PUENTE:
            PC = casillas_puente[1]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[0], "avanza a,", casillas_puente[1])
            time.sleep(3)
            vuelve_a_tirar = "si"
        elif PC == 12:  # CASILLAS PUENTES
            PC = casillas_puente[0]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[1], "retrocede a,", casillas_puente[0])
            time.sleep(3)
            vuelve_a_tirar = "si"

        if PC == 19:   #casilla la posada
            time.sleep(2)
            print("El PC ha caído en la posada, pierde dos turnos.")
            time.sleep(2)
            posada_pc = "si"
            turno_USER(casillas_especiales, PC, casillas_puente, JU,posada_user,posada_pc,posada_user_3,posada_pc_3)

        if PC == 31:  # pozo de bronce
            time.sleep(2)
            print("El PC ha caído en el Pozo de Bronce, pierde tres turnos.")
            time.sleep(2)
            posada_pc_3 = "si"
            turno_USER(casillas_especiales, PC, casillas_puente, JU,posada_user,posada_pc,posada_user_3,posada_pc_3)

        if PC == 42:     # LABERINTO, SE RETROCEDE A 30
            time.sleep(1)
            print("Del laberinto al 30")
            time.sleep(2)
            print("El PC retrocede a la casilla 30")
            time.sleep(2)
            PC = 30

        if PC == 52:  # Cárcel, pierdes tres turnos
            time.sleep(2)
            print("PC ha caído en la casilla Cárcel, pierde tres turnos.")
            time.sleep(2)
            posada_pc_3 = "si"
            turno_USER(casillas_especiales, PC, casillas_puente, JU, posada_user, posada_pc,posada_user_3,posada_pc_3)

        if PC == 58:  # Calavera
            time.sleep(2)
            print("PC ha caído en la casilla Calavera, vuelve a la casilla de inicio.")
            time.sleep(2)
            PC = 1

        if (str(PC) == "63"):  # en caso de que PC este en la casilla 63, gana.
            ganador = "PC"
            Ganador(ganador)

        for y in tablero: #AQUI SE MOSTRARA EL TABLERO CON LAS POSICIONES EXACTAS EN LAS QUE SE ENCUENTRAN AMBOS
            for z in range(len(tablero[y])):
                if (JU == PC and JU != 1):  # JU DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                    if (JU < 9 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "J|P"
                    elif (tablero[y][z] == str(JU)):
                        tablero[y][z] = "J|P"
                if (int(JU) < 9 and tablero[1][z] == "0" + str(JU)):
                    tablero[1][z] = "JU"
                elif tablero[y][z] == str(JU):
                    tablero[y][z] = "JU"
                if (int(PC) < 9 and tablero[1][z] == "0" + str(PC)):
                    tablero[1][z] = "PC"
                elif tablero[y][z] == str(PC):
                    tablero[y][z] = "PC"
            time.sleep(0.2)
            print(tablero[y])

    if (vuelve_a_tirar == "si"):#SI HA ENTRADO EN ALGUNA CASILLA ESPECIAL Y LE TOCA VOLVER A TIRAR:
        time.sleep(1)
        print("Le toca volver a tirar a PC.")
        time.sleep(1)
        turno_PC(casillas_especiales, JU, casillas_puente, PC,posada_pc,posada_user,posada_user_3,posada_pc_3)

    if (posada_user == "si"): #si hay posada de user, vuelve a tirar PC.
        posada_user = ""
        time.sleep(1)
        print("Segunda tirada de PC.")
        time.sleep(1)
        turno_PC(casillas_especiales, JU, casillas_puente, PC, posada_pc, posada_user,posada_user_3,posada_pc_3)

    if (posada_user_3 == "si" or posada_user_3 == "s"): #si hay Carcel o Pozo de Bronce de User, tirara 3 veces en total PC.
        if (posada_user_3 == "si"):
            posada_user_3 = "s"
            print("Segunda tirada de PC.")
            time.sleep(1)
            turno_PC(casillas_especiales, JU, casillas_puente, PC, posada_pc, posada_user, posada_user_3, posada_pc_3)
        if (posada_user_3 == "s"):
            posada_user_3 = ""
            print("Tercera tirada de PC.")
            time.sleep(1)
            turno_PC(casillas_especiales, JU, casillas_puente, PC, posada_pc, posada_user, posada_user_3, posada_pc_3)

    if (posada_user == "" and posada_user_3 == "" and vuelve_a_tirar == ""):
        turno_USER(casillas_especiales, PC, casillas_puente, JU, posada_user, posada_pc,posada_user_3,posada_pc_3)

def turno_USER(casillas_especiales,PC,casillas_puente,JU,posada_user,posada_pc,posada_user_3,posada_pc_3):
    vuelvo_a_tirar= ""
    tablero = {
        8: ["22", "21", "20", "19", "18", "17", "16", "15"],
        7: ["23", "43", "42", "41", "40", "39", "38", "14"],
        6: ["24", "44", "57", "56", "55", "54", "37", "13"],
        5: ["25", "45", "58", "63", "62", "53", "36", "12"],
        4: ["26", "46", "59", "60", "61", "52", "35", "11"],
        3: ["27", "47", "48", "49", "50", "51", "34", "10"],
        2: ["28", "29", "30", "31", "32", "33", "34", "09"],
        1: ["01", "02", "03", "04", "05", "06", "07", "08"]
    }
    for x in range(1):
        time.sleep(1)
        print("Tu turno")
        time.sleep(1)
        x = input("Tirar dado (SI/NO):")
        if (x=="si" or x=="SI" or x=="Si" or x=="sI" or x=="S" or x=="s"):
            d1= random.randint(1,6)
            JU = int(JU)+d1
            if (JU > 63):
                JU = JU - d1
                for x in range(d1):
                    if (JU < 63):
                        JU = JU + 1
                    elif (JU == 63):
                        for z in range(d1 - x):
                            JU = JU - 1
                        break
            time.sleep(1)
            print("El dado salio:",d1,",Estas en la casilla :",JU)
            for m in range(len(casillas_especiales)):#EN CASO DE QUE LA POSICION EN LA QUE ESTE EL USER CAIGA EN OCA:
                if "0"+str(JU) == casillas_especiales[m]:
                    JU = casillas_especiales[m + 1]
                    time.sleep(3)
                    print("De oca en oca y tiro porque me toca")
                    time.sleep(2)
                    print("Te ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                    vuelvo_a_tirar = "si"
                    time.sleep(2)
                    break
                elif (str(JU) == casillas_especiales[m] and JU < 63):
                    JU = casillas_especiales[m + 1]
                    time.sleep(2)
                    print("Te ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                    vuelvo_a_tirar = "si"
                    time.sleep(2)
                    break

            if JU == 6:  # EN CASO DE QUE USER ESTE EN ALGUNA CASILLA PUENTE:
                JU = casillas_puente[1]
                time.sleep(2)
                print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[0], "avanzas a,",casillas_puente[1])
                vuelvo_a_tirar = "si"
                time.sleep(3)
            elif JU == 12:  # CASILLAS PUENTES
                JU = casillas_puente[0]
                time.sleep(2)
                print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[1], "retrocedes a,",casillas_puente[0])
                vuelvo_a_tirar = "si"
                time.sleep(3)

            if JU == 19:#casilla la posada
                time.sleep(2)
                print("Has caído en la Posada, pierdes dos turnos.")
                time.sleep(2)
                posada_user="si"
                turno_PC(casillas_especiales, JU, casillas_puente, PC,posada_pc,posada_user,posada_user_3,posada_pc_3)

            if JU == 31: #pozo de bronce
                time.sleep(2)
                print("Has caído en la casilla Pozo de Bronce, pierdes tres turnos.")
                time.sleep(2)
                posada_user_3 = "si"
                turno_PC(casillas_especiales, JU, casillas_puente, PC, posada_pc, posada_user,posada_user_3,posada_pc_3)

            if JU == 42: #LABERINTO, SE RETROCEDE A 30
                time.sleep(2)
                print("Del laberinto al 30")
                time.sleep(2)
                print("Retrocedes a la casilla 30")
                JU = 30

            if JU == 52:  # Cárcel, pierdes tres turnos
                time.sleep(2)
                print("Has caído en la Cárcel, pierdes tres turnos.")
                time.sleep(2)
                posada_user_3 = "si"
                turno_PC(casillas_especiales, JU, casillas_puente, PC,posada_pc,posada_user,posada_user_3,posada_pc_3)

            if JU == 58:   #Calavera
                time.sleep(2)
                print("Has caído en la Calavera, vuelves a la casilla de inicio.")
                time.sleep(2)
                JU = 1

            if (str(JU) == "63"):
                ganador = "User"
                Ganador(ganador)

            for y in tablero: #AQUI SE MOSTRARA EL TABLERO CON LAS POSICIONES EXACTAS EN LAS QUE SE ENCUENTRAN AMBOS
                for z in range(len(tablero[y])):
                    if (JU == PC and JU != 0):  # JU DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                        if (JU < 9 and tablero[1][z] == "0" + str(JU)):
                            tablero[1][z] = "J|P"
                        elif (tablero[y][z] == str(JU)):
                            tablero[y][z] = "J|P"
                    if (int(JU) < 9 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "JU"
                    elif tablero[y][z] == str(JU):
                        tablero[y][z] = "JU"
                    if (int(PC) < 9 and tablero[1][z] == "0" + str(PC)):
                        tablero[1][z] = "PC"
                    elif tablero[y][z] == str(PC):
                        tablero[y][z] = "PC"
                time.sleep(0.2)
                print(tablero[y])

        elif (x=="no" or x=="NO" or x=="No" or x=="nO" or x=="N" or x=="n"):
            print("Como que no xD")
            turno_USER(casillas_especiales,PC,casillas_puente,JU,posada_user,posada_pc,posada_user_3,posada_pc_3)
        else:
            print("Error! Vuelve a intentarlo.")
            turno_USER(casillas_especiales,PC,casillas_puente,JU,posada_user,posada_pc,posada_user_3,posada_pc_3)

    if (vuelvo_a_tirar == "si"):#SI HA ENTRADO EN ALGUNA CASILLA ESPECIAL Y LE TOCA VOLVER A TIRAR:
        print("Te toca volver a tirar.")
        time.sleep(2)
        turno_USER(casillas_especiales, PC, casillas_puente, JU,posada_user,posada_pc,posada_user_3,posada_pc_3)

    if (posada_pc == "si"):
        posada_pc = ""
        turno_USER(casillas_especiales, PC, casillas_puente, JU, posada_user, posada_pc,posada_user_3,posada_pc_3)

    if (posada_pc_3 == "si" or posada_pc_3 == "s"): #si hay Carcel o Pozo de Bronce de User, tirara 3 veces en total PC.
        if (posada_pc_3 == "si"):
            posada_pc_3 = "s"
            print("Tu Segunda tirada.")
            time.sleep(1)
            turno_USER(casillas_especiales, PC, casillas_puente, JU, posada_user, posada_pc,posada_user_3,posada_pc_3)
        if (posada_pc_3 == "s"):
            posada_pc_3 = ""
            print("Tu Tercera tirada.")
            time.sleep(1)
            turno_USER(casillas_especiales, PC, casillas_puente, JU, posada_user, posada_pc,posada_user_3,posada_pc_3)

    if (posada_pc == "" and posada_pc_3 == "" and vuelvo_a_tirar == ""):
        turno_PC(casillas_especiales, JU, casillas_puente, PC,posada_pc,posada_user,posada_user_3,posada_pc_3)

def Ganador(x):
    time.sleep(3)
    if (x=="User"):
        print("Felicidades! Has ganado")
    else:
        print("Mala suerte, ha ganado pc!")
    time.sleep(6)
    print("Volviendo al menu principal...")
    time.sleep(3)
    from pruebas import menu
    menu()
