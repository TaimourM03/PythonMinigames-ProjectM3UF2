import random,time
def Oca():
    tablero = {
        8: ["25", "24", "23", "22", "21", "20", "19", "18", "17", "16"],
        7: ["26", "51", "50", "49", "48", "47", "46", "45", "44", "15"],
        6: ["27", "52", "  ", "  ", "  ", "  ", "  ", "  ", "43", "14"],
        5: ["28", "53", "  ", "  ", "  ", "  ", "  ", "  ", "42", "13"],
        4: ["29", "54", "  ", "  ", "  ", "  ", "  ", "62", "41", "12"],
        3: ["30", "55", "56", "57", "58", "59", "60", "61", "40", "11"],
        2: ["31", "32", "33", "34", "35", "36", "37", "38", "39", "10"],
        1: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    }
    JU = 0
    PC = 0
    casillas_especiales = ["05", "09", "14", "18", "23", "27", "32", "36", "41", "45", "50", "54", "59", "63"]
    ganador = ""
    casillas_puente = ["06", "12"]
    while (ganador==""):
        turno_USER(tablero,casillas_especiales,PC,ganador,casillas_puente)
        if (ganador==""):
            turno_PC(tablero,casillas_especiales,JU,ganador,casillas_puente)


def turno_PC(tablero,casillas_especiales,JU,ganador,casillas_puente):
    PC = 0
    for x in range(1):
        time.sleep(1)
        print("Turno del PC")
        dp1 = random.randint(1, 6)
        dp2 = random.randint(1, 6)
        to = dp1 + dp2
        PC = int(PC) + to
        print("PC ha tirado los dados.")
        time.sleep(2)
        print("El primer dado salio:", dp1, ",El segundo dado salio:", dp2, ",La suma de los dados del PC es:", to,",El PC ha avanzado al puesto:", PC)
        time.sleep(2)
        for m in range(len(casillas_especiales)):
            if "0" + str(PC) == casillas_especiales[m]:
                PC = casillas_especiales[m + 1]
                time.sleep(2)
                print("Al PC le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                time.sleep(2)
                break
            elif str(PC) == casillas_especiales[m]:
                PC = casillas_especiales[m + 1]
                time.sleep(2)
                print("Al PC le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                time.sleep(2)
                break
        for y in tablero:
            for z in range(len(tablero[y])):
                if (JU == PC and PC != 0):  #PC DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                    if (JU < 10 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "J|P"
                    elif (tablero[y][z] == str(JU)):
                        tablero[y][z] = "J|P"
                if (int(PC) < 10 and tablero[1][z] == "0" + str(PC)):
                    tablero[1][z] = "PC"
                elif tablero[y][z] == str(PC):
                    tablero[y][z] = "PC"
            time.sleep(0.2)
            print(tablero[y])

        if PC == "06":  # CASILLAS PUENTES
            PC = casillas_puente[1]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[0], "salta a,",
                  casillas_puente[1])
            print("Vuelve a tirar")
            time.sleep(1)
            turno_USER(tablero, casillas_especiales, JU, ganador, casillas_puente, PC)
            time.sleep(2)
        if PC == "12":  # CASILLAS PUENTES
            PC = casillas_puente[0]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[1], "vuelve a,",
                  casillas_puente[0])
            time.sleep(1)
            print("Vuelve a tirar")
            turno_USER(tablero, casillas_especiales, JU, ganador, casillas_puente, PC)
            time.sleep(2)

def turno_USER(tablero,casillas_especiales,PC,ganador,casillas_puente):
    JU = 0
    for x in range(1):
        time.sleep(1)
        print("Tu turno")
        time.sleep(2)
        x = input("Tirar dado (SI/NO):")
        if (x=="si"):
            d1= random.randint(1,6)
            d2=random.randint(1,6)
            t = d1+d2
            JU = int(JU)+t
            time.sleep(2)
            print("El primer dado salio:",d1,",El segundo dado salio:",d2,",La suma de los dados es:",t,",Haz avanzado a la casilla :",JU)
            for m in range(len(casillas_especiales)):
                if "0"+str(JU) == casillas_especiales[m]:
                    JU = casillas_especiales[m + 1]
                    time.sleep(2)
                    print("Al Jugador le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                    time.sleep(2)
                    break
                elif str(JU) == casillas_especiales[m]:
                    JU = casillas_especiales[m + 1]
                    time.sleep(2)
                    print("Al Jugador le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                    time.sleep(2)
                    break
            for y in tablero:
                for z in range(len(tablero[y])):
                    if (JU == PC and JU != 0):  # JU DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                        if (JU < 10 and tablero[1][z] == "0" + str(JU)):
                            tablero[1][z] = "J|P"
                        elif (tablero[y][z] == str(JU)):
                            tablero[y][z] = "J|P"
                    if (int(JU) < 10 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "JU"
                    elif tablero[y][z] == str(JU):
                        tablero[y][z] = "JU"
                time.sleep(0.2)
                print(tablero[y])
        elif (x=="no"):
            print("Como que no mamaguevo")
            turno_USER(tablero,casillas_especiales,PC,ganador)
        else:
            print("Error! Vuelve a intentarlo.")
            turno_USER(tablero,casillas_especiales,PC,ganador)

        if JU == "06":  # CASILLAS PUENTES
            JU = casillas_puente[1]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[0], "salta a,",
                  casillas_puente[1])
            print("Vuelve a tirar")
            time.sleep(1)
            turno_USER(tablero, casillas_especiales, PC, ganador, casillas_puente, JU)
            time.sleep(2)
        if JU == "12":  # CASILLAS PUENTES
            JU = casillas_puente[0]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[1], "vuelve a,",
                  casillas_puente[0])
            time.sleep(1)
            print("Vuelve a tirar")
            turno_USER(tablero, casillas_especiales, PC, ganador, casillas_puente, JU)
            time.sleep(2)

Oca()















































#LO NUEVO 06/03/2022#
import random,time
def Oca():
    JU = 0
    PC = 0
    casillas_especiales = ["05", "09", "14", "18", "23", "27", "32", "36", "41", "45", "50", "54", "59", "63"]
    casillas_puente = ["06", "12"]
    turno_USER(casillas_especiales,PC,casillas_puente,JU)


def turno_PC(casillas_especiales,JU,casillas_puente,PC):
    vuelve_a_tirar = ""
    tablero = {
        8: ["25", "24", "23", "22", "21", "20", "19", "18", "17", "16"],
        7: ["26", "51", "50", "49", "48", "47", "46", "45", "44", "15"],
        6: ["27", "52", "  ", "  ", "  ", "  ", "  ", "  ", "43", "14"],
        5: ["28", "53", "  ", "  ", "  ", "  ", "  ", "  ", "42", "13"],
        4: ["29", "54", "  ", "  ", "  ", "  ", "  ", "62", "41", "12"],
        3: ["30", "55", "56", "57", "58", "59", "60", "61", "40", "11"],
        2: ["31", "32", "33", "34", "35", "36", "37", "38", "39", "10"],
        1: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    }
    for x in range(1):
        time.sleep(1)
        print("Turno del PC")
        dp1 = random.randint(1, 6)
        dp2 = random.randint(1, 6)
        to = dp1 + dp2
        PC = int(PC) + to
        print("PC ha tirado los dados.")
        time.sleep(2)
        print("El primer dado salio:", dp1, ",El segundo dado salio:", dp2, ",La suma de los dados del PC es:", to,",El PC ha avanzado al puesto:", PC)
        time.sleep(2)
        for m in range(len(casillas_especiales)): #EN CASO DE QUE LA POSICION EN LA QUE ESTE EL PC CAIGA EN OCA:
            if "0" + str(PC) == casillas_especiales[m]:
                PC = casillas_especiales[m + 1]
                time.sleep(2)
                print("Al PC le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                vuelve_a_tirar = "si"
                time.sleep(3)
                break
            elif str(PC) == casillas_especiales[m]:
                PC = casillas_especiales[m + 1]
                time.sleep(2)
                print("Al PC le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                vuelve_a_tirar = "si"
                time.sleep(3)
                break

        if str(PC) == "06":  # EN CASO DE QUE PC ESTE EN ALGUNA CASILLA PUENTE:
            PC = casillas_puente[1]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[0], "avanza a,",casillas_puente[1])
            time.sleep(3)
            vuelve_a_tirar = "si"
        if str(PC) == "12":  # CASILLAS PUENTES
            PC = casillas_puente[0]
            time.sleep(2)
            print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[1], "retrocede a,",casillas_puente[0])
            time.sleep(3)
            vuelve_a_tirar = "si"

        for y in tablero: #AQUI SE MOSTRARA EL TABLERO CON LAS POSICIONES EXACTAS EN LAS QUE SE ENCUENTRAN AMBOS
            for z in range(len(tablero[y])):
                if (JU == PC and JU != 0):  # JU DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                    if (JU < 10 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "J|P"
                    elif (tablero[y][z] == str(JU)):
                        tablero[y][z] = "J|P"
                if (int(JU) < 10 and tablero[1][z] == "0" + str(JU)):
                    tablero[1][z] = "JU"
                elif tablero[y][z] == str(JU):
                    tablero[y][z] = "JU"
                if (int(PC) < 10 and tablero[1][z] == "0" + str(PC)):
                    tablero[1][z] = "PC"
                elif tablero[y][z] == str(PC):
                    tablero[y][z] = "PC"
            time.sleep(0.2)
            print(tablero[y])

    if (vuelve_a_tirar == ""):  # SI NO LE HA TOCADO NINGUNA CASILLA ESPECIAL, POR ENDE NO TIENE QUE VOLVER A TIRAR:
        turno_USER(casillas_especiales, PC, casillas_puente, JU)# UNA VEZ HAYA TIRADO EL USER, LE TOCA TIRAR AL PC
    else:  # SI HA ENTRADO EN ALGUNA CASILLA ESPECIAL Y LE TOCA VOLVER A TIRAR:
        print("Le toca volver a tirar a PC.")
        time.sleep(2)
        turno_PC(casillas_especiales, JU, casillas_puente, PC)

def turno_USER(casillas_especiales,PC,casillas_puente,JU):
    vuelvo_a_tirar= ""
    tablero = {
        8: ["25", "24", "23", "22", "21", "20", "19", "18", "17", "16"],
        7: ["26", "51", "50", "49", "48", "47", "46", "45", "44", "15"],
        6: ["27", "52", "  ", "  ", "  ", "  ", "  ", "  ", "43", "14"],
        5: ["28", "53", "  ", "  ", "  ", "  ", "  ", "  ", "42", "13"],
        4: ["29", "54", "  ", "  ", "  ", "  ", "  ", "62", "41", "12"],
        3: ["30", "55", "56", "57", "58", "59", "60", "61", "40", "11"],
        2: ["31", "32", "33", "34", "35", "36", "37", "38", "39", "10"],
        1: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    }
    for x in range(1):
        time.sleep(1)
        print("Tu turno")
        time.sleep(2)
        x = input("Tirar dado (SI/NO):")
        if (x=="si" or x=="SI"):
            d1= random.randint(1,6)
            d2=random.randint(1,6)
            t = d1+d2
            JU = int(JU)+t
            time.sleep(2)
            print("El primer dado salio:",d1,",El segundo dado salio:",d2,",La suma de los dados es:",t,",Haz avanzado a la casilla :",JU)
            for m in range(len(casillas_especiales)):#EN CASO DE QUE LA POSICION EN LA QUE ESTE EL USER CAIGA EN OCA:
                if "0"+str(JU) == casillas_especiales[m]:
                    JU = casillas_especiales[m + 1]
                    time.sleep(2)
                    print("Al Jugador le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                    vuelvo_a_tirar = "si"
                    time.sleep(3)
                    break
                elif str(JU) == casillas_especiales[m]:
                    JU = casillas_especiales[m + 1]
                    time.sleep(2)
                    print("Al Jugador le ha tocado una casilla especial,", casillas_especiales[m], "salta a,",casillas_especiales[m + 1])
                    vuelvo_a_tirar = "si"
                    time.sleep(3)
                    break

            if str(JU) == "06":  # EN CASO DE QUE USER ESTE EN ALGUNA CASILLA PUENTE:
                JU = casillas_puente[1]
                time.sleep(2)
                print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[0], "avanzas a,",casillas_puente[1])
                vuelvo_a_tirar = "si"
                time.sleep(3)
            if str(JU) == "12":  # CASILLAS PUENTES
                JU = casillas_puente[0]
                time.sleep(2)
                print("De puente a puente y tiro porque me lleva la corriente", casillas_puente[1], "retrocedes a,",casillas_puente[0])
                vuelvo_a_tirar = "si"
                time.sleep(3)

            for y in tablero: #AQUI SE MOSTRARA EL TABLERO CON LAS POSICIONES EXACTAS EN LAS QUE SE ENCUENTRAN AMBOS
                for z in range(len(tablero[y])):
                    if (JU == PC and JU != 0):  # JU DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                        if (JU < 10 and tablero[1][z] == "0" + str(JU)):
                            tablero[1][z] = "J|P"
                        elif (tablero[y][z] == str(JU)):
                            tablero[y][z] = "J|P"
                    if (int(JU) < 10 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "JU"
                    elif tablero[y][z] == str(JU):
                        tablero[y][z] = "JU"
                    if (int(PC) < 10 and tablero[1][z] == "0" + str(PC)):
                        tablero[1][z] = "PC"
                    elif tablero[y][z] == str(PC):
                        tablero[y][z] = "PC"
                time.sleep(0.2)
                print(tablero[y])

        elif (x=="no" or x=="NO"):
            print("Como que no xD")
            turno_USER(casillas_especiales,PC,casillas_puente,JU)
        else:
            print("Error! Vuelve a intentarlo.")
            turno_USER(casillas_especiales,PC,casillas_puente,JU)

    if (vuelvo_a_tirar == ""):#SI NO LE HA TOCADO NINGUNA CASILLA ESPECIAL, POR ENDE NO TIENE QUE VOLVER A TIRAR:
        turno_PC(casillas_especiales,JU,casillas_puente,PC)# UNA VEZ HAYA TIRADO EL USER, LE TOCA TIRAR AL PC
    else:#SI HA ENTRADO EN ALGUNA CASILLA ESPECIAL Y LE TOCA VOLVER A TIRAR:
        print("Te toca volver a tirar.")
        time.sleep(2)
        turno_USER(casillas_especiales, PC, casillas_puente, JU)





Oca()

    
