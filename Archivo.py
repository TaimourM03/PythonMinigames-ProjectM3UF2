

def menu():
    juegos = ["1: Hundir la flota","2: Oca","3: Escaleras y Serpientes","4: Quién es quién","5: Conecta 4","6: Apagar"]
    for x in range(len(juegos)):
        print(juegos[x])
    opcion = int(input("Escoge un juego:"))
    if (opcion == 1):
        Hundir_la_flota()
    elif (opcion == 2):
        Oca()
    elif (opcion == 3):
        Escaleras_y_Serpientes()
    elif (opcion == 4):
        Quien_es_quien()
    elif (opcion == 5):
        Conecta_4()
    elif (opcion == 6):
        pass
    else:
        print("Error!")
        menu()

def Hundir_la_flota():
    tablero = {
        0: [" J1 ", " J2 ", " J3 ", " J4 ", " J5 ", " J6 ", " J7 ", " J8 ", " J9 ", " J10 "],
        1: [" I1 ", " I2 ", " I3 ", " I4 ", " I5 ", " I6 ", " I7 ", " I8 ", " I9 ", " I10 "],
        2: [" H1 ", " H2 ", " H3 ", " H4 ", " H5 ", " H6 ", " H7 ", " H8 ", " H9 ", " H10 "],
        3: [" G1 ", " G2 ", " G3 ", " G4 ", " G5 ", " G6 ", " G7 ", " G8 ", " G9 ", " G10 "],
        4: [" F1 ", " F2 ", " F3 ", " F4 ", " F5 ", " F6 ", " F7 ", " F8 ", " F9 ", " F10 "],
        5: [" E1 ", " E2 ", " E3 ", " E4 ", " E5 ", " E6 ", " E7 ", " E8 ", " E9 ", " E10 "],
        6: [" D1 ", " D2 ", " D3 ", " D4 ", " D5 ", " D6 ", " D7 ", " D8 ", " D9 ", " D10 "],
        7: [" C1 ", " C2 ", " C3 ", " C4 ", " C5 ", " C6 ", " C7 ", " C8 ", " C9 ", " C10 "],
        8: [" B1 ", " B2 ", " B3 ", " B4 ", " B5 ", " B6 ", " B7 ", " B8 ", " B9 ", " B10 "],
        9: [" A1 ", " A2 ", " A3 ", " A4 ", " A5 ", " A6 ", " A7 ", " A8 ", " A9 ", " A10 "],
    }
    tablero_ordenador = {
        0: [" J1 ", " J2 ", " J3 ", " J4 ", " J5 ", " J6 ", " J7 ", " J8 ", " J9 ", " J10 "],
        1: [" I1 ", " I2 ", " I3 ", " I4 ", " I5 ", " I6 ", " I7 ", " I8 ", " I9 ", " I10 "],
        2: [" H1 ", " H2 ", " H3 ", " H4 ", " H5 ", " H6 ", " H7 ", " H8 ", " H9 ", " H10 "],
        3: [" G1 ", " G2 ", " G3 ", " G4 ", " G5 ", " G6 ", " G7 ", " G8 ", " G9 ", " G10 "],
        4: [" F1 ", " F2 ", " F3 ", " F4 ", " F5 ", " F6 ", " F7 ", " F8 ", " F9 ", " F10 "],
        5: [" E1 ", " E2 ", " E3 ", " E4 ", " E5 ", " E6 ", " E7 ", " E8 ", " E9 ", " E10 "],
        6: [" D1 ", " D2 ", " D3 ", " D4 ", " D5 ", " D6 ", " D7 ", " D8 ", " D9 ", " D10 "],
        7: [" C1 ", " C2 ", " C3 ", " C4 ", " C5 ", " C6 ", " C7 ", " C8 ", " C9 ", " C10 "],
        8: [" B1 ", " B2 ", " B3 ", " B4 ", " B5 ", " B6 ", " B7 ", " B8 ", " B9 ", " B10 "],
        9: [" A1 ", " A2 ", " A3 ", " A4 ", " A5 ", " A6 ", " A7 ", " A8 ", " A9 ", " A10 "],
    }

    opciones_finales = [] #2 sera vertical, 1 horizontal, posibilidades primera casilla: (1-7) o (A-G)
    numeros_posibles = [1,2,3,4,5,6,7]
    letras_posibles = ["A","B","C","D","E","F","G"]
    posiciones = []
    for x in range(10):
        barco = random.randint(1,2)
        opciones_finales.append(barco)
        for x in range(1): #barco de 4 casillas (solo hay uno)
            if (barco == 1):
                pri_num= random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                if (pri_letra == "A"):#FALTA ADIVINAR EL NUMERO QUE HAY EN LA POSICION
                    if(pri_num == 1):#LA POSICION ES A1
                        posiciones.append(" A1 ")
                        posiciones.append(" A2 ")
                        posiciones.append(" A3 ")
                        posiciones.append(" A4 ")
                    elif(pri_num == 2):#LA POSICION ES A2
                        posiciones.append(" A2 ")
                        posiciones.append(" A3 ")
                        posiciones.append(" A4 ")
                        posiciones.append(" A5 ")
                    elif(pri_num == 3):#LA POSICION ES A3
                        posiciones.append(" A3 ")
                        posiciones.append(" A4 ")
                        posiciones.append(" A5 ")
                        posiciones.append(" A6 ")
                    elif(pri_num == 4):#LA POSICION ES A4
                        posiciones.append(" A4 ")
                        posiciones.append(" A5 ")
                        posiciones.append(" A6 ")
                        posiciones.append(" A7 ")
                    elif(pri_num == 5):#LA POSICION ES A5
                        posiciones.append(" A5 ")
                        posiciones.append(" A6 ")
                        posiciones.append(" A7 ")
                        posiciones.append(" A8 ")
                    elif(pri_num == 6):#LA POSICION ES A6
                        posiciones.append(" A6 ")
                        posiciones.append(" A7 ")
                        posiciones.append(" A8 ")
                        posiciones.append(" A9 ")
                    elif(pri_num == 7):#LA POSICION ES A7
                        posiciones.append(" A7 ")
                        posiciones.append(" A8 ")
                        posiciones.append(" A9 ")
                        posiciones.append(" A10 ")

                elif (pri_letra == "B"):
                    if(pri_num == 1):#LA POSICION ES B1
                        posiciones.append(" B1 ")
                        posiciones.append(" B2 ")
                        posiciones.append(" B3 ")
                        posiciones.append(" B4 ")
                    elif(pri_num == 2):#LA POSICION ES B2
                        posiciones.append(" B2 ")
                        posiciones.append(" B3 ")
                        posiciones.append(" B4 ")
                        posiciones.append(" B5 ")
                    elif(pri_num == 3):#LA POSICION ES B3
                        posiciones.append(" B3 ")
                        posiciones.append(" B4 ")
                        posiciones.append(" B5 ")
                        posiciones.append(" B6 ")
                    elif(pri_num == 4):#LA POSICION ES B4
                        posiciones.append(" B4 ")
                        posiciones.append(" B5 ")
                        posiciones.append(" B6 ")
                        posiciones.append(" B7 ")
                    elif(pri_num == 5):#LA POSICION ES B5
                        posiciones.append(" B5 ")
                        posiciones.append(" B6 ")
                        posiciones.append(" B7 ")
                        posiciones.append(" B8 ")
                    elif(pri_num == 6):#LA POSICION ES B6
                        posiciones.append(" B6 ")
                        posiciones.append(" B7 ")
                        posiciones.append(" B8 ")
                        posiciones.append(" B9 ")
                    elif(pri_num == 7):#LA POSICION ES B7
                        posiciones.append(" B7 ")
                        posiciones.append(" B8 ")
                        posiciones.append(" B9 ")
                        posiciones.append(" B10 ")

                elif (pri_letra == "C"):
                    if(pri_num == 1):#LA POSICION ES C1
                        posiciones.append(" C1 ")
                        posiciones.append(" C2 ")
                        posiciones.append(" C3 ")
                        posiciones.append(" C4 ")
                    elif(pri_num == 2):#LA POSICION ES C2
                        posiciones.append(" C2 ")
                        posiciones.append(" C3 ")
                        posiciones.append(" C4 ")
                        posiciones.append(" C5 ")
                    elif(pri_num == 3):#LA POSICION ES C3
                        posiciones.append(" C3 ")
                        posiciones.append(" C4 ")
                        posiciones.append(" C5 ")
                        posiciones.append(" C6 ")
                    elif(pri_num == 4):#LA POSICION ES C4
                        posiciones.append(" C4 ")
                        posiciones.append(" C5 ")
                        posiciones.append(" C6 ")
                        posiciones.append(" C7 ")
                    elif(pri_num == 5):#LA POSICION ES C5
                        posiciones.append(" C5 ")
                        posiciones.append(" C6 ")
                        posiciones.append(" C7 ")
                        posiciones.append(" C8 ")
                    elif(pri_num == 6):#LA POSICION ES C6
                        posiciones.append(" C6 ")
                        posiciones.append(" C7 ")
                        posiciones.append(" C8 ")
                        posiciones.append(" C9 ")
                    elif(pri_num == 7):#LA POSICION ES C7
                        posiciones.append(" C7 ")
                        posiciones.append(" C8 ")
                        posiciones.append(" C9 ")
                        posiciones.append(" C10 ")

                elif (pri_letra == "D"):
                    if(pri_num == 1):#LA POSICION ES D1
                        posiciones.append(" D1 ")
                        posiciones.append(" D2 ")
                        posiciones.append(" D3 ")
                        posiciones.append(" D4 ")
                    elif(pri_num == 2):#LA POSICION ES D2
                        posiciones.append(" D2 ")
                        posiciones.append(" D3 ")
                        posiciones.append(" D4 ")
                        posiciones.append(" D5 ")
                    elif(pri_num == 3):#LA POSICION ES D3
                        posiciones.append(" D3 ")
                        posiciones.append(" D4 ")
                        posiciones.append(" D5 ")
                        posiciones.append(" D6 ")
                    elif(pri_num == 4):#LA POSICION ES D4
                        posiciones.append(" D4 ")
                        posiciones.append(" D5 ")
                        posiciones.append(" D6 ")
                        posiciones.append(" D7 ")
                    elif(pri_num == 5):#LA POSICION ES D5
                        posiciones.append(" D5 ")
                        posiciones.append(" D6 ")
                        posiciones.append(" D7 ")
                        posiciones.append(" D8 ")
                    elif(pri_num == 6):#LA POSICION ES D6
                        posiciones.append(" D6 ")
                        posiciones.append(" D7 ")
                        posiciones.append(" D8 ")
                        posiciones.append(" D9 ")
                    elif(pri_num == 7):#LA POSICION ES D7
                        posiciones.append(" D7 ")
                        posiciones.append(" D8 ")
                        posiciones.append(" D9 ")
                        posiciones.append(" D10 ")

                elif (pri_letra == "E"):
                    if(pri_num == 1):#LA POSICION ES E1
                        posiciones.append(" E1 ")
                        posiciones.append(" E2 ")
                        posiciones.append(" E3 ")
                        posiciones.append(" E4 ")
                    elif(pri_num == 2):#LA POSICION ES E2
                        posiciones.append(" E2 ")
                        posiciones.append(" E3 ")
                        posiciones.append(" E4 ")
                        posiciones.append(" E5 ")
                    elif(pri_num == 3):#LA POSICION ES E3
                        posiciones.append(" E3 ")
                        posiciones.append(" E4 ")
                        posiciones.append(" E5 ")
                        posiciones.append(" E6 ")
                    elif(pri_num == 4):#LA POSICION ES E4
                        posiciones.append(" E4 ")
                        posiciones.append(" E5 ")
                        posiciones.append(" E6 ")
                        posiciones.append(" E7 ")
                    elif(pri_num == 5):#LA POSICION ES E5
                        posiciones.append(" E5 ")
                        posiciones.append(" E6 ")
                        posiciones.append(" E7 ")
                        posiciones.append(" E8 ")
                    elif(pri_num == 6):#LA POSICION ES E6
                        posiciones.append(" E6 ")
                        posiciones.append(" E7 ")
                        posiciones.append(" E8 ")
                        posiciones.append(" E9 ")
                    elif(pri_num == 7):#LA POSICION ES E7
                        posiciones.append(" E7 ")
                        posiciones.append(" E8 ")
                        posiciones.append(" E9 ")
                        posiciones.append(" E10 ")

                elif (pri_letra == "F"):
                    if(pri_num == 1):#LA POSICION ES F1
                        posiciones.append(" F1 ")
                        posiciones.append(" F2 ")
                        posiciones.append(" F3 ")
                        posiciones.append(" F4 ")
                    elif(pri_num == 2):#LA POSICION ES F2
                        posiciones.append(" F2 ")
                        posiciones.append(" F3 ")
                        posiciones.append(" F4 ")
                        posiciones.append(" F5 ")
                    elif(pri_num == 3):#LA POSICION ES F3
                        posiciones.append(" F3 ")
                        posiciones.append(" F4 ")
                        posiciones.append(" F5 ")
                        posiciones.append(" F6 ")
                    elif(pri_num == 4):#LA POSICION ES F4
                        posiciones.append(" F4 ")
                        posiciones.append(" F5 ")
                        posiciones.append(" F6 ")
                        posiciones.append(" F7 ")
                    elif(pri_num == 5):#LA POSICION ES F5
                        posiciones.append(" F5 ")
                        posiciones.append(" F6 ")
                        posiciones.append(" F7 ")
                        posiciones.append(" F8 ")
                    elif(pri_num == 6):#LA POSICION ES F6
                        posiciones.append(" F6 ")
                        posiciones.append(" F7 ")
                        posiciones.append(" F8 ")
                        posiciones.append(" F9 ")
                    elif(pri_num == 7):#LA POSICION ES F7
                        posiciones.append(" F7 ")
                        posiciones.append(" F8 ")
                        posiciones.append(" F9 ")
                        posiciones.append(" F10 ")

                elif (pri_letra == "G"):
                    if(pri_num == 1):#LA POSICION ES G1
                        posiciones.append(" G1 ")
                        posiciones.append(" G2 ")
                        posiciones.append(" G3 ")
                        posiciones.append(" G4 ")
                    elif(pri_num == 2):#LA POSICION ES G2
                        posiciones.append(" G2 ")
                        posiciones.append(" G3 ")
                        posiciones.append(" G4 ")
                        posiciones.append(" G5 ")
                    elif(pri_num == 3):#LA POSICION ES G3
                        posiciones.append(" G3 ")
                        posiciones.append(" G4 ")
                        posiciones.append(" G5 ")
                        posiciones.append(" G6 ")
                    elif(pri_num == 4):#LA POSICION ES G4
                        posiciones.append(" G4 ")
                        posiciones.append(" G5 ")
                        posiciones.append(" G6 ")
                        posiciones.append(" G7 ")
                    elif(pri_num == 5):#LA POSICION ES G5
                        posiciones.append(" G5 ")
                        posiciones.append(" G6 ")
                        posiciones.append(" G7 ")
                        posiciones.append(" G8 ")
                    elif(pri_num == 6):#LA POSICION ES G6
                        posiciones.append(" G6 ")
                        posiciones.append(" G7 ")
                        posiciones.append(" G8 ")
                        posiciones.append(" G9 ")
                    elif(pri_num == 7):#LA POSICION ES G7
                        posiciones.append(" G7 ")
                        posiciones.append(" G8 ")
                        posiciones.append(" G9 ")
                        posiciones.append(" G10 ")

                elif (pri_letra == "H"):
                    if(pri_num == 1):#LA POSICION ES H1
                        posiciones.append(" H1 ")
                        posiciones.append(" H2 ")
                        posiciones.append(" H3 ")
                        posiciones.append(" H4 ")
                    elif(pri_num == 2):#LA POSICION ES H2
                        posiciones.append(" H2 ")
                        posiciones.append(" H3 ")
                        posiciones.append(" H4 ")
                        posiciones.append(" H5 ")
                    elif(pri_num == 3):#LA POSICION ES H3
                        posiciones.append(" H3 ")
                        posiciones.append(" H4 ")
                        posiciones.append(" H5 ")
                        posiciones.append(" H6 ")
                    elif(pri_num == 4):#LA POSICION ES H4
                        posiciones.append(" H4 ")
                        posiciones.append(" H5 ")
                        posiciones.append(" H6 ")
                        posiciones.append(" H7 ")
                    elif(pri_num == 5):#LA POSICION ES H5
                        posiciones.append(" H5 ")
                        posiciones.append(" H6 ")
                        posiciones.append(" H7 ")
                        posiciones.append(" H8 ")
                    elif(pri_num == 6):#LA POSICION ES H6
                        posiciones.append(" H6 ")
                        posiciones.append(" H7 ")
                        posiciones.append(" H8 ")
                        posiciones.append(" H9 ")
                    elif(pri_num == 7):#LA POSICION ES H7
                        posiciones.append(" H7 ")
                        posiciones.append(" H8 ")
                        posiciones.append(" H9 ")
                        posiciones.append(" H10 ")

                elif (pri_letra == "I"):
                    if(pri_num == 1):#LA POSICION ES I1
                        posiciones.append(" I1 ")
                        posiciones.append(" I2 ")
                        posiciones.append(" I3 ")
                        posiciones.append(" I4 ")
                    elif(pri_num == 2):#LA POSICION ES I2
                        posiciones.append(" I2 ")
                        posiciones.append(" I3 ")
                        posiciones.append(" I4 ")
                        posiciones.append(" I5 ")
                    elif(pri_num == 3):#LA POSICION ES I3
                        posiciones.append(" I3 ")
                        posiciones.append(" I4 ")
                        posiciones.append(" I5 ")
                        posiciones.append(" I6 ")
                    elif(pri_num == 4):#LA POSICION ES I4
                        posiciones.append(" I4 ")
                        posiciones.append(" I5 ")
                        posiciones.append(" I6 ")
                        posiciones.append(" I7 ")
                    elif(pri_num == 5):#LA POSICION ES I5
                        posiciones.append(" I5 ")
                        posiciones.append(" I6 ")
                        posiciones.append(" I7 ")
                        posiciones.append(" I8 ")
                    elif(pri_num == 6):#LA POSICION ES I6
                        posiciones.append(" I6 ")
                        posiciones.append(" I7 ")
                        posiciones.append(" I8 ")
                        posiciones.append(" I9 ")
                    elif(pri_num == 7):#LA POSICION ES I7
                        posiciones.append(" I7 ")
                        posiciones.append(" I8 ")
                        posiciones.append(" I9 ")
                        posiciones.append(" I10 ")

                elif (pri_letra == "J"):
                    if(pri_num == 1):#LA POSICION ES J1
                        posiciones.append(" J1 ")
                        posiciones.append(" J2 ")
                        posiciones.append(" J3 ")
                        posiciones.append(" J4 ")
                    elif(pri_num == 2):#LA POSICION ES J2
                        posiciones.append(" J2 ")
                        posiciones.append(" J3 ")
                        posiciones.append(" J4 ")
                        posiciones.append(" J5 ")
                    elif(pri_num == 3):#LA POSICION ES J3
                        posiciones.append(" J3 ")
                        posiciones.append(" J4 ")
                        posiciones.append(" J5 ")
                        posiciones.append(" J6 ")
                    elif(pri_num == 4):#LA POSICION ES J4
                        posiciones.append(" J4 ")
                        posiciones.append(" J5 ")
                        posiciones.append(" J6 ")
                        posiciones.append(" J7 ")
                    elif(pri_num == 5):#LA POSICION ES J5
                        posiciones.append(" J5 ")
                        posiciones.append(" J6 ")
                        posiciones.append(" J7 ")
                        posiciones.append(" J8 ")
                    elif(pri_num == 6):#LA POSICION ES J6
                        posiciones.append(" J6 ")
                        posiciones.append(" J7 ")
                        posiciones.append(" J8 ")
                        posiciones.append(" J9 ")
                    elif(pri_num == 7):#LA POSICION ES J7
                        posiciones.append(" J7 ")
                        posiciones.append(" J8 ")
                        posiciones.append(" J9 ")
                        posiciones.append(" J10 ")
                        
                else: #en caso de que no sea horizontal, es decir, es vertical:
                    if(pri_num == 1):
                        if(pri_letra == "A"):
                            posiciones.append(" A1 ")
                            posiciones.append(" B1 ")
                            posiciones.append(" C1 ")
                            posiciones.append(" D1 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B1 ")
                            posiciones.append(" C1 ")
                            posiciones.append(" D1 ")
                            posiciones.append(" E1 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C1 ")
                            posiciones.append(" D1 ")
                            posiciones.append(" E1 ")
                            posiciones.append(" F1 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D1 ")
                            posiciones.append(" E1 ")
                            posiciones.append(" F1 ")
                            posiciones.append(" G1 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E1 ")
                            posiciones.append(" F1 ")
                            posiciones.append(" G1 ")
                            posiciones.append(" H1 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F1 ")
                            posiciones.append(" G1 ")
                            posiciones.append(" H1 ")
                            posiciones.append(" I1 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G1 ")
                            posiciones.append(" H1 ")
                            posiciones.append(" I1 ")
                            posiciones.append(" J1 ")

                    elif(pri_num == 2):
                        if(pri_letra == "A"):
                            posiciones.append(" A2 ")
                            posiciones.append(" B2 ")
                            posiciones.append(" C2 ")
                            posiciones.append(" D2 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B2 ")
                            posiciones.append(" C2 ")
                            posiciones.append(" D2 ")
                            posiciones.append(" E2 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C2 ")
                            posiciones.append(" D2 ")
                            posiciones.append(" E2 ")
                            posiciones.append(" F2 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D2 ")
                            posiciones.append(" E2 ")
                            posiciones.append(" F2 ")
                            posiciones.append(" G2 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E2 ")
                            posiciones.append(" F2 ")
                            posiciones.append(" G2 ")
                            posiciones.append(" H2 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F2 ")
                            posiciones.append(" G2 ")
                            posiciones.append(" H2 ")
                            posiciones.append(" I2 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G2 ")
                            posiciones.append(" H2 ")
                            posiciones.append(" I2 ")
                            posiciones.append(" J2 ")

                    elif(pri_num == 3):
                        if(pri_letra == "A"):
                            posiciones.append(" A3 ")
                            posiciones.append(" B3 ")
                            posiciones.append(" C3 ")
                            posiciones.append(" D3 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B3 ")
                            posiciones.append(" C3 ")
                            posiciones.append(" D3 ")
                            posiciones.append(" E3 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C3 ")
                            posiciones.append(" D3 ")
                            posiciones.append(" E3 ")
                            posiciones.append(" F3 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D3 ")
                            posiciones.append(" E3 ")
                            posiciones.append(" F3 ")
                            posiciones.append(" G3 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E3 ")
                            posiciones.append(" F3 ")
                            posiciones.append(" G3 ")
                            posiciones.append(" H3 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F3 ")
                            posiciones.append(" G3 ")
                            posiciones.append(" H3 ")
                            posiciones.append(" I3 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G3 ")
                            posiciones.append(" H3 ")
                            posiciones.append(" I3 ")
                            posiciones.append(" J3 ")

                    elif(pri_num == 4):
                        if(pri_letra == "A"):
                            posiciones.append(" A4 ")
                            posiciones.append(" B4 ")
                            posiciones.append(" C4 ")
                            posiciones.append(" D4 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B4 ")
                            posiciones.append(" C4 ")
                            posiciones.append(" D4 ")
                            posiciones.append(" E4 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C4 ")
                            posiciones.append(" D4 ")
                            posiciones.append(" E4 ")
                            posiciones.append(" F4 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D4 ")
                            posiciones.append(" E4 ")
                            posiciones.append(" F4 ")
                            posiciones.append(" G4 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E4 ")
                            posiciones.append(" F4 ")
                            posiciones.append(" G4 ")
                            posiciones.append(" H4 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F4 ")
                            posiciones.append(" G4 ")
                            posiciones.append(" H4 ")
                            posiciones.append(" I4 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G4 ")
                            posiciones.append(" H4 ")
                            posiciones.append(" I4 ")
                            posiciones.append(" J4 ")

                    elif(pri_num == 5):
                        if(pri_letra == "A"):
                            posiciones.append(" A5 ")
                            posiciones.append(" B5 ")
                            posiciones.append(" C5 ")
                            posiciones.append(" D5 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B5 ")
                            posiciones.append(" C5 ")
                            posiciones.append(" D5 ")
                            posiciones.append(" E5 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C5 ")
                            posiciones.append(" D5 ")
                            posiciones.append(" E5 ")
                            posiciones.append(" F5 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D5 ")
                            posiciones.append(" E5 ")
                            posiciones.append(" F5 ")
                            posiciones.append(" G5 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E5 ")
                            posiciones.append(" F5 ")
                            posiciones.append(" G5 ")
                            posiciones.append(" H5 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F5 ")
                            posiciones.append(" G5 ")
                            posiciones.append(" H5 ")
                            posiciones.append(" I5 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G5 ")
                            posiciones.append(" H5 ")
                            posiciones.append(" I5 ")
                            posiciones.append(" J5 ")

                    elif(pri_num == 6):
                        if(pri_letra == "A"):
                            posiciones.append(" A6 ")
                            posiciones.append(" B6 ")
                            posiciones.append(" C6 ")
                            posiciones.append(" D6 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B6 ")
                            posiciones.append(" C6 ")
                            posiciones.append(" D6 ")
                            posiciones.append(" E6 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C6 ")
                            posiciones.append(" D6 ")
                            posiciones.append(" E6 ")
                            posiciones.append(" F6 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D6 ")
                            posiciones.append(" E6 ")
                            posiciones.append(" F6 ")
                            posiciones.append(" G6 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E6 ")
                            posiciones.append(" F6 ")
                            posiciones.append(" G6 ")
                            posiciones.append(" H6 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F6 ")
                            posiciones.append(" G6 ")
                            posiciones.append(" H6 ")
                            posiciones.append(" I6 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G6 ")
                            posiciones.append(" H6 ")
                            posiciones.append(" I6 ")
                            posiciones.append(" J6 ")

                    elif(pri_num == 7):
                        if(pri_letra == "A"):
                            posiciones.append(" A7 ")
                            posiciones.append(" B7 ")
                            posiciones.append(" C7 ")
                            posiciones.append(" D7 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B7 ")
                            posiciones.append(" C7 ")
                            posiciones.append(" D7 ")
                            posiciones.append(" E7 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C7 ")
                            posiciones.append(" D7 ")
                            posiciones.append(" E7 ")
                            posiciones.append(" F7 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D7 ")
                            posiciones.append(" E7 ")
                            posiciones.append(" F7 ")
                            posiciones.append(" G7 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E7 ")
                            posiciones.append(" F7 ")
                            posiciones.append(" G7 ")
                            posiciones.append(" H7 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F7 ")
                            posiciones.append(" G7 ")
                            posiciones.append(" H7 ")
                            posiciones.append(" I7 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G7 ")
                            posiciones.append(" H7 ")
                            posiciones.append(" I7 ")
                            posiciones.append(" J7 ")

                    elif(pri_num == 8):
                        if(pri_letra == "A"):
                            posiciones.append(" A8 ")
                            posiciones.append(" B8 ")
                            posiciones.append(" C8 ")
                            posiciones.append(" D8 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B8 ")
                            posiciones.append(" C8 ")
                            posiciones.append(" D8 ")
                            posiciones.append(" E8 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C8 ")
                            posiciones.append(" D8 ")
                            posiciones.append(" E8 ")
                            posiciones.append(" F8 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D8 ")
                            posiciones.append(" E8 ")
                            posiciones.append(" F8 ")
                            posiciones.append(" G8 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E8 ")
                            posiciones.append(" F8 ")
                            posiciones.append(" G8 ")
                            posiciones.append(" H8 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F8 ")
                            posiciones.append(" G8 ")
                            posiciones.append(" H8 ")
                            posiciones.append(" I8 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G8 ")
                            posiciones.append(" H8 ")
                            posiciones.append(" I8 ")
                            posiciones.append(" J8 ")

                    elif(pri_num == 9):
                        if(pri_letra == "A"):
                            posiciones.append(" A9 ")
                            posiciones.append(" B9 ")
                            posiciones.append(" C9 ")
                            posiciones.append(" D9 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B9 ")
                            posiciones.append(" C9 ")
                            posiciones.append(" D9 ")
                            posiciones.append(" E9 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C9 ")
                            posiciones.append(" D9 ")
                            posiciones.append(" E9 ")
                            posiciones.append(" F9 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D9 ")
                            posiciones.append(" E9 ")
                            posiciones.append(" F9 ")
                            posiciones.append(" G9 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E9 ")
                            posiciones.append(" F9 ")
                            posiciones.append(" G9 ")
                            posiciones.append(" H9 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F9 ")
                            posiciones.append(" G9 ")
                            posiciones.append(" H9 ")
                            posiciones.append(" I9 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G9 ")
                            posiciones.append(" H9 ")
                            posiciones.append(" I9 ")
                            posiciones.append(" J9 ")

                    elif(pri_num == 10):
                        if(pri_letra == "A"):
                            posiciones.append(" A10 ")
                            posiciones.append(" B10 ")
                            posiciones.append(" C10 ")
                            posiciones.append(" D10 ")
                        elif(pri_letra == "B"):
                            posiciones.append(" B10 ")
                            posiciones.append(" C10 ")
                            posiciones.append(" D10 ")
                            posiciones.append(" E10 ")
                        elif(pri_letra == "C"):
                            posiciones.append(" C10 ")
                            posiciones.append(" D10 ")
                            posiciones.append(" E10 ")
                            posiciones.append(" F10 ")
                        elif(pri_letra == "D"):
                            posiciones.append(" D10 ")
                            posiciones.append(" E10 ")
                            posiciones.append(" F10 ")
                            posiciones.append(" G10 ")
                        elif(pri_letra == "E"):
                            posiciones.append(" E10 ")
                            posiciones.append(" F10 ")
                            posiciones.append(" G10 ")
                            posiciones.append(" H10 ")
                        elif(pri_letra == "F"):
                            posiciones.append(" F10 ")
                            posiciones.append(" G10 ")
                            posiciones.append(" H10 ")
                            posiciones.append(" I10 ")
                        elif(pri_letra == "G"):
                            posiciones.append(" G10 ")
                            posiciones.append(" H10 ")
                            posiciones.append(" I10 ")
                            posiciones.append(" J10 ")
    
def Oca():
    import random
def Oca():
    pos = 0
    posi = 0
    while pos!=64 or posi!=64:
        x=input("Tirar dado SI/NO:")
        if x=="si":
            d1= random.randint(1,6)
            d2=random.randint(1,6)
            t = d1+d2
            pos = pos +t
            print("El primer dado salio:",d1,"El segundo dado salio:",d2,"La suma de los dados es:",t,"Haz avanzado a la casilla :",pos)
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            t = d1 + d2
            posi = posi + t
            print("El primer dado salio:", d1, "El segundo dado salio:", d2,"La suma de los dados del PC es:", t,"El PC ha avanzado al puesto:",posi)
        elif x=="no":
            print("Has decidido no tirar")
        else:
            x=input("Tirar dado SI/NO:")

    tablero= {
        8:["25","24","23","22","21","20","19","18","17","16"],
        7:["26","51","50","49","48","47","46","45","44","15"],
        6:["27","52","64","64","64","64","64","64","43","14"],
        5:["28","53","64","64","64","64","64","63","42","13"],
        4:["29","54","64","64","64","64","64","62","41","12"],
        3:["30","55","56","57","58","59","60","61","40","11"],
        2:["31","32","33","34","35","36","37","38","39","10"],
        1:["00","01","02","03","04","05","06","07","08","09"]
    }
    for x in tablero:
        print(tablero[x])
def Escaleras_y_Serpientes():
    
        def Escaleras_y_Serpientes():
    
        tablero = {
            0: ["100","99","98","97","96","95","E6","S3","92","91"],
        	1: ["81","82","83","84","E5","86","87","88","S2","90"],
        	2: ["E4","79","78","77","S3","75","74","73","72","71"],
        	3: ["61","62","63","64","65","66","E6","68","69","70"],
        	4: ["60","59","58","E5","56","E3","54","53","52","51"],
        	5: ["41","E4","43","44","45","46","47","S2","E2","50"],
        	6: ["40","39","38","E1","36","35","34","33","32","S1"],
        	7: ["21","22","23","24","25","26","E3","28","29","30"],
        	8: ["20","19","18","17","16","15","S1","13","E2","11"],
        	9: ["01","02","03","E1","05","06","07","08","09","10"]             
        }
        import random
        posicio = 0
        d1=random.randint(1,6)
        print("El dado es:",d1)
        if z=="E1":
            print("Tienes que subir hasta siguiente E1")
        elif z=="E2":
            print("Tienes que subir hasta siguiente E2")
        elif z=="E3":
            print("Tienes que subir hasta la siguiente E3")
        elif z=="S1":
            print("Tienes que bajar hasta la S1")
        elif z=="E4":
            print("Tienes que subir hasta la siguiente E4")
        elif z=="E5":
            print("Tienes que subir hasta la siguiente E5")
        elif z=="E6":
            print("Tienes que subir hasta la siguiente E6")
        elif z=="S2":
            print("Tienes que bajar hasta la S2")
        elif z=="S3":
            print("Tienes que bajar hasta la S3")
        elif z=="100":
            print("Felicidaes, haz ganado")
        else:
            
        
        for x in tablero:
            print(tablero[x])
    
    pass
def Quien_es_quien():
    pass
def Conecta_4():
    tablero = {
        0:["G1","G2","G3","G4","G5","G6","G7"],
        1:["F1","F2","F3","F4","F5","F6","F7"],
        2:["E1","E2","E3","E4","E5","E6","E7"],
        3:["D1","D2","D3","D4","D5","D6","D7"],
        4:["C1","C2","C3","C4","C5","C6","C7"],
        5:["B1","B2","B3","B4","B5","B6","B7"],
        6:["A1","A2","A3","A4","A5","A6","A7"]
    }
    lista = ["piedra","papel","tijeras"]
    decision = input("piedra, papel o tijeras?")
    if (decision in lista): 
        import random
        decision_pc = random.choice(lista)
        print("El pc ha escogido:",decision_pc)
        if decision == "piedra":
            if (decision_pc == "piedra"):
                print("Empate")
            elif (decision_pc == "papel"):
                print("Has perdido")
            elif (decision_pc == "tijeras"):
                print("Has ganado")
    
        elif decision == "papel":
            if (decision_pc == "piedra"):
                print("Has ganado")
            elif (decision_pc == "papel"):
                print("Empate")
            elif (decision_pc == "tijeras"):
                print("Has perdido")
   
        elif decision == "tijeras":
            if (decision_pc == "piedra"):
                print("Has perdido")
            elif (decision_pc == "papel"):
                print("Has ganado")
            elif (decision_pc == "tijeras"):
                print("Empate")
    else:
        print("ERROR")
        
Conecta_4()




