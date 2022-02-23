import random, time

def Hundir_la_flota():
    #web normas del juego: https://familiaycole.files.wordpress.com/2012/09/instrucciones-del-juego-de-los-barcos.pdf
    tablero = {
        "J": ["J0", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9"],
        "I": ["I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"],
        "H": ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"],
        "G": ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
        "F": ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"],
        "E": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"],
        "D": ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9"],
        "C": ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
        "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"],
    }
    tablero_ordenador = {
        "J": ["J0", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9"],
        "I": ["I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"],
        "H": ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"],
        "G": ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
        "F": ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"],
        "E": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"],
        "D": ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9"],
        "C": ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
        "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"],
    }
    tablero_del_pc_para_user = {
        "J": ["J0", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9"],
        "I": ["I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"],
        "H": ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"],
        "G": ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
        "F": ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"],
        "E": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"],
        "D": ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9"],
        "C": ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
        "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"],
    }
    tablero_del_user_para_pc = {
        "J": ["J0", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9"],
        "I": ["I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"],
        "H": ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"],
        "G": ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
        "F": ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"],
        "E": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"],
        "D": ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9"],
        "C": ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
        "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"],
    }
    opciones_finales = []  # 2 sera vertical, 1 horizontal, posibilidades primera casilla: (1-7) o (A-G)
    numeros_posibles = [0,1,2,3,4,5,6]
    letras_posibles = ["A","B","C","D","E","F","G"]
    todas_las_letras = ["A","B","C","D","E","F","G","H","I","J"]
    posiciones = []
    posiciones2 = []
    tab_pc = Barcos_del_pc(opciones_finales,numeros_posibles,letras_posibles,todas_las_letras,posiciones,tablero_ordenador)
    posiciones_user = []
    posiciones_vert = ["A0", "B0", "C0", "D0", "E0", "F0", "G0", "H0", "I0", "J0", "A1", "B1", "C1", "D1", "E1", "F1",
                       "G1", "H1", "I1", "J1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "A3", "B3",
                       "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
                       "I4", "J4", "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "A6", "B6", "C6", "D6",
                       "E6", "F6", "G6", "H6", "I6", "J6", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7",
                       "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "A9", "B9", "C9", "D9", "E9", "F9",
                       "G9", "H9", "I9", "J9"]
    posiciones_hori = ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "B0", "B1", "B2", "B3", "B4", "B5",
                       "B6", "B7", "B8", "B9", "C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "D0", "D1",
                       "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7",
                       "E8", "E9", "F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "G0", "G1", "G2", "G3",
                       "G4", "G5", "G6", "G7", "G8", "G9", "H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9",
                       "I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "J0", "J1", "J2", "J3", "J4", "J5",
                       "J6", "J7", "J8", "J9"]
    posiciones_dichas = []
    posiciones_dichas_2 = []
    ganador = ""
    #tab_user = Barcos_del_user(posiciones_user,posiciones_vert,posiciones_hori,tablero,todas_las_letras)
    #for x in tab_user:
        #print(tab_user[x])
        #print("Empieza el juego!")
    while (ganador == ""):
        Hundir_la_flota_turno_pc(tablero_del_pc_para_user,posiciones_vert,posiciones,posiciones_dichas,ganador)
        if (ganador == ""):
            Hundir_la_flota_turno_user(tablero_del_user_para_pc, posiciones_vert, posiciones2, posiciones_dichas_2,ganador)

def Barcos_del_pc(opciones_finales,numeros_posibles,letras_posibles,todas_las_letras,posiciones,tablero_ordenador):
    print("Le toca al PC asignarse las posiciones de los barcos.")
    time.sleep(3)
    while (len(posiciones) < 20):
        barco = random.randint(1, 2)
        opciones_finales.append(barco)
        while (len(posiciones) < 3):  # barco de 4 casillas (solo hay uno)
            if (barco == 1):  # HORIZONTAL   #EJ: A1, A2, A3, A4
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                p1 = pri_letra + str(pri_num)
                p2 = pri_letra + str(pri_num + 1)
                p3 = pri_letra + str(pri_num + 2)
                p4 = pri_letra + str(pri_num + 3)
                posiciones.append(p1)
                posiciones.append(p2)
                posiciones.append(p3)
                posiciones.append(p4)
            else:  # VERTICAL     #EJ: A1, B1, C1, D1
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                for x in range(len(todas_las_letras)):
                    if (pri_letra == todas_las_letras[x]):
                        p1 = todas_las_letras[x + 0] + str(pri_num)
                        p2 = todas_las_letras[x + 1] + str(pri_num)
                        p3 = todas_las_letras[x + 2] + str(pri_num)
                        p4 = todas_las_letras[x + 3] + str(pri_num)
                        posiciones.append(p1)
                        posiciones.append(p2)
                        posiciones.append(p3)
                        posiciones.append(p4)

        while (len(posiciones) > 3 and len(posiciones) < 9):  # aqui haremos los dos barcos de 3 casillas
            if (barco == 1):  # HORIZONTAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                p1 = pri_letra + str(pri_num)
                p2 = pri_letra + str(pri_num + 1)
                p3 = pri_letra + str(pri_num + 2)
                if (p1 not in posiciones and p2 not in posiciones and p3 not in posiciones):
                    posiciones.append(p1)
                    posiciones.append(p2)
                    posiciones.append(p3)
                else:  # si la posicion creada ya esta ocupada por otro barco:
                    continue
            else:  # VERTICAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                for x in range(len(todas_las_letras)):
                    if (pri_letra == todas_las_letras[x]):
                        p1 = todas_las_letras[x + 0] + str(pri_num)
                        p2 = todas_las_letras[x + 1] + str(pri_num)
                        p3 = todas_las_letras[x + 2] + str(pri_num)
                        if (p1 not in posiciones and p2 not in posiciones and p3 not in posiciones):
                            posiciones.append(p1)
                            posiciones.append(p2)
                            posiciones.append(p3)
                        else:  # si la posicion creada ya esta ocupada por otro barco:
                            continue

        while (len(posiciones) > 9 and len(posiciones) < 15):  # aqui haremos los tres barcos de 2 casillas
            if (barco == 1):  # HORIZONTAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                p1 = pri_letra + str(pri_num)
                p2 = pri_letra + str(pri_num + 1)
                if (p1 not in posiciones and p2 not in posiciones):
                    posiciones.append(p1)
                    posiciones.append(p2)
                else:  # si la posicion creada ya esta ocupada por otro barco:
                    continue
            else:  # VERTICAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                for x in range(len(todas_las_letras)):
                    if (pri_letra == todas_las_letras[x]):
                        p1 = todas_las_letras[x + 0] + str(pri_num)
                        p2 = todas_las_letras[x + 1] + str(pri_num)
                        if (p1 not in posiciones and p2 not in posiciones):
                            posiciones.append(p1)
                            posiciones.append(p2)
                        else:
                            continue

        while (len(posiciones) > 15 and len(posiciones) < 20):  # aqui haremos los cuatro barcos de 1 casilla
            if (barco == 1):  # HORIZONTAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                p1 = pri_letra + str(pri_num)
                if (p1 not in posiciones):
                    posiciones.append(p1)
                else:  # si la posicion creada ya esta ocupada por otro barco:
                    continue
            else:  # VERTICAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(letras_posibles)
                for x in range(len(todas_las_letras)):
                    if (pri_letra == todas_las_letras[x]):
                        p1 = todas_las_letras[x + 0] + str(pri_num)
                        if (p1 not in posiciones):
                            posiciones.append(p1)
                        else:
                            continue
    print("PC ya se ha asignado las posicones de los barcos.")
    time.sleep(2)
    for x in range(len(posiciones)):
        for z in range(10):  # de 0 a 9
            if (posiciones[x] == (todas_las_letras[0] + str(z))):
                tablero_ordenador[todas_las_letras[0]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[1] + str(z))):
                tablero_ordenador[todas_las_letras[1]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[2] + str(z))):
                tablero_ordenador[todas_las_letras[2]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[3] + str(z))):
                tablero_ordenador[todas_las_letras[3]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[4] + str(z))):
                tablero_ordenador[todas_las_letras[4]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[5] + str(z))):
                tablero_ordenador[todas_las_letras[5]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[6] + str(z))):
                tablero_ordenador[todas_las_letras[6]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[7] + str(z))):
                tablero_ordenador[todas_las_letras[7]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[8] + str(z))):
                tablero_ordenador[todas_las_letras[8]][z] = "XX"
            elif (posiciones[x] == (todas_las_letras[9] + str(z))):
                tablero_ordenador[todas_las_letras[9]][z] = "XX"
    return posiciones

def Barcos_del_user(posiciones_user,posiciones_vert,posiciones_hori,tablero,todas_las_letras):
    while(len(posiciones_user) < 20):
        print("Te toca elegir donde quieres poner los barcos.")
        time.sleep(3)
        while (len(posiciones_user) < 3):  # barco de 4 casillas (solo hay uno)
            print("Turno para crear el barco de 4 casillas.")
            dir = input("Quieres crear el barco horizontal o vertical? (H,V):")
            c1 = input("Dime la 1/4 casilla que ocupara el barco:")
            c2 = input("Dime la 2/4 casilla que ocupara el barco:")
            c3 = input("Dime la 3/4 casilla que ocupara el barco:")
            c4 = input("Dime la 4/4 casilla que ocupara el barco:")
            if (dir == "V"):
                for e in range(len(posiciones_vert)):
                    if (c1 == posiciones_vert[e]):
                        if (c2 == posiciones_vert[e + 1] and c3 == posiciones_vert[e + 2] and c4 == posiciones_vert[e + 3]):
                            posiciones_user.append(c1)
                            posiciones_user.append(c2)
                            posiciones_user.append(c3)
                            posiciones_user.append(c4)
                            print("Posiciones asignadas correctamente!")
                            break
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            break
                    elif (c1 not in posiciones_vert):
                        print("Incorrecto! Vuelve a intentarlo")
                        break

            elif (dir == "H"):
                for x in range(len(posiciones_hori)):
                    if (c1 == posiciones_hori[x]):
                        if (c2 == posiciones_hori[x + 1] and c3 == posiciones_hori[x + 2] and c4 == posiciones_hori[x + 3]):
                            posiciones_user.append(c1)
                            posiciones_user.append(c2)
                            posiciones_user.append(c3)
                            posiciones_user.append(c4)
                            print("Posiciones asignadas correctamente!")
                            break
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            break
                    elif (c1 not in posiciones_hori):
                        print("Incorrecto! Vuelve a intentarlo")
                        break

        while (len(posiciones_user) > 3 and len(posiciones_user) < 9):  # aqui haremos los dos barcos de 3 casillas
            print("Turno para crear los barcos de 3 casillas.")
            dir = input("Quieres crear el barco horizontal o vertical? (H,V):")
            c1 = input("Dime la 1/3 casilla que ocupara el barco:")
            c2 = input("Dime la 2/3 casilla que ocupara el barco:")
            c3 = input("Dime la 3/3 casilla que ocupara el barco:")
            if (dir == "V"):
                for e in range(len(posiciones_vert)):
                    if (c1 == posiciones_vert[e]):
                        if (c2 == posiciones_vert[e + 1] and c3 == posiciones_vert[e + 2]):
                            if (c1 not in posiciones_user and c2 not in posiciones_user and c3 not in posiciones_user):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                posiciones_user.append(c3)
                                print("Posiciones asignadas correctamente!")
                                break
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                break
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            break
                    elif (c1 not in posiciones_vert):
                        print("Incorrecto! Vuelve a intentarlo")
                        break

            elif (dir == "H"):
                for e in range(len(posiciones_hori)):
                    if (c1 == posiciones_hori[e]):
                        if (c2 == posiciones_hori[e + 1] and c3 == posiciones_hori[e + 2]):
                            if (c1 not in posiciones_user and c2 not in posiciones_user and c3 not in posiciones_user):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                posiciones_user.append(c3)
                                print("Posiciones asignadas correctamente!")
                                break
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                break
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            break
                    elif (c1 not in posiciones_hori):
                        print("Incorrecto! Vuelve a intentarlo")
                        break

        while (len(posiciones_user) > 9 and len(posiciones_user) < 15):  # aqui haremos los tres barcos de 2 casillas
            print("Turno para crear los barcos de 2 casillas.")
            dir = input("Quieres crear el barco horizontal o vertical? (H,V):")
            c1 = input("Dime la 1/2 casilla que ocupara el barco:")
            c2 = input("Dime la 2/2 casilla que ocupara el barco:")
            if (dir == "V"):
                for e in range(len(posiciones_vert)):
                    if (c1 == posiciones_vert[e]):
                        if (c2 == posiciones_vert[e + 1]):
                            if (c1 not in posiciones_user and c2 not in posiciones_user):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                print("Posiciones asignadas correctamente!")
                                break
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                break
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            break
                    elif (c1 not in posiciones_vert):
                        print("Incorrecto! Vuelve a intentarlo")
                        break

            elif (dir == "H"):
                for e in range(len(posiciones_hori)):
                    if (c1 == posiciones_hori[e]):
                        if (c2 == posiciones_hori[e + 1]):
                            if (c1 not in posiciones_user and c2 not in posiciones_user):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                print("Posiciones asignadas correctamente!")
                                break
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                break
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            break
                    elif (c1 not in posiciones_hori):
                        print("Incorrecto! Vuelve a intentarlo")
                        break

        while (len(posiciones_user) > 15 and len(posiciones_user) < 20):  # aqui haremos los cuatro barcos de 1 casilla
            print("Turno para crear los barcos de 1 casilla.")
            c1 = input("Dime la 1/1 casilla que ocupara el barco:")
            for e in range(len(posiciones_vert)):
                if (c1 == posiciones_vert[e]):
                    if (c1 not in posiciones_user):
                        posiciones_user.append(c1)
                        print("Posiciones asignadas correctamente!")
                        break
                    else:
                        print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                        break
                elif (c1 not in posiciones_vert):
                    print("Incorrecto! Vuelve a intentarlo")
                    break

    for x in range(len(posiciones_user)):  # 3 veces
        for z in range(10):  # de 0 a 9
            if (posiciones_user[x] == (todas_las_letras[0] + str(z))):
                tablero[todas_las_letras[0]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[1] + str(z))):
                tablero[todas_las_letras[1]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[2] + str(z))):
                tablero[todas_las_letras[2]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[3] + str(z))):
                tablero[todas_las_letras[3]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[4] + str(z))):
                tablero[todas_las_letras[4]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[5] + str(z))):
                tablero[todas_las_letras[5]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[6] + str(z))):
                tablero[todas_las_letras[6]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[7] + str(z))):
                tablero[todas_las_letras[7]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[8] + str(z))):
                tablero[todas_las_letras[8]][z] = "XX"
            elif (posiciones_user[x] == (todas_las_letras[9] + str(z))):
                tablero[todas_las_letras[9]][z] = "XX"
    print("Tu tablero se ha generado correctamente.")
    time.sleep(3)
    return tablero

def Hundir_la_flota_turno_pc(tablero_del_pc_para_user,posiciones_vert,posiciones,posiciones_dichas,ganador):
    for a in range(1):
        print("Es tu turno para escoger una casilla!")
        time.sleep(2)
        for mi in tablero_del_pc_para_user:
            print(tablero_del_pc_para_user[mi])
        time.sleep(2)
        c = input("Dime la coordenada a la que deseas lanzar un misil:")
        if (c not in posiciones_vert):
            print("ERROR! La coordenada insertada no existe")
            time.sleep(2)
            print("Vuelve a intentarlo!")
            Hundir_la_flota_turno_pc(tablero_del_pc_para_user,posiciones_vert,posiciones,posiciones_dichas,ganador)
        elif (c in posiciones_vert):
            if (c in posiciones_dichas):
                print("ERROR! La coordenada insertada ya fue escogida!")
                time.sleep(2)
                print("Vuelve a intentarlo!")
                Hundir_la_flota_turno_pc(tablero_del_pc_para_user, posiciones_vert,posiciones,posiciones_dichas,ganador)
            elif (c not in posiciones_dichas):
                print("Lanzando misil a:",c)
                for x in range(3, 0, -1):
                    time.sleep(1)
                    print(x)
                print("Misil lanzado correctamente!")
                time.sleep(2)
                for x in tablero_del_pc_para_user:
                    for z in range(len(tablero_del_pc_para_user[x])):
                        if (c in posiciones):
                            if (tablero_del_pc_para_user[x][z] == c):
                                print("Tocado!")
                                tablero_del_pc_para_user[x][z] = "XX"
                                posiciones_dichas.append(c)
                                total = 0
                                for w in range(len(posiciones_dichas)):
                                    if (posiciones_dichas[w] in posiciones):
                                        total = total + 1
                                    if (total == len(posiciones)): #en caso de que todas las posiciones que las posiciones introducidas por el usuario esten en la lista de las posiciones donde hay barcos, gana la partida.
                                        print("Has ganado!")
                                        time.sleep(1)
                                        print("Felicidades!")
                                        time.sleep(1)
                                        for q in tablero_del_pc_para_user:
                                            print(tablero_del_pc_para_user[q])
                                        time.sleep(1)
                                        print("Este es el tablero final!")
                                        ganador = "user"

                        elif (c not in posiciones):
                            if (tablero_del_pc_para_user[x][z] == c):
                                print("Agua")
                                tablero_del_pc_para_user[x][z] = "~~"
                                posiciones_dichas.append(c)
        time.sleep(2)
        for x in tablero_del_pc_para_user:
            print(tablero_del_pc_para_user[x])
        time.sleep(2)

def Hundir_la_flota_turno_user(tablero_del_user_para_pc,posiciones_vert,posiciones2,posiciones_dichas_2,ganador):
    for t in range(1):
        print("Es el turno de PC para escoger una casilla!")
        time.sleep(2)
        for p in tablero_del_user_para_pc:
            print(tablero_del_user_para_pc[p])
        time.sleep(2)
        casilla = random.choice(posiciones_vert)
        if (casilla in posiciones_dichas_2):
            Hundir_la_flota_turno_user(tablero_del_user_para_pc,posiciones_vert,posiciones2,posiciones_dichas_2,ganador)
        elif (casilla not in posiciones_dichas_2):
            print("El PC ha escogido la casilla:",casilla)
            time.sleep(1)
            print("Lanzando misil a:", casilla)
            for x in range(3, 0, -1):
                time.sleep(1)
                print(x)
            print("Misil lanzado correctamente!")
            time.sleep(2)
            for b in tablero_del_user_para_pc:
                for n in range(len(tablero_del_user_para_pc[b])):
                    if (casilla in posiciones2):
                        if (tablero_del_user_para_pc[b][n] == casilla):
                            print("Tocado!")
                            tablero_del_user_para_pc[b][n] = "XX"
                            posiciones_dichas_2.append(casilla)
                            tota = 0
                            for m in range(len(posiciones_dichas_2)):
                                if (posiciones_dichas_2[m] in posiciones2):
                                    tota = tota + 1
                                    print(tota)
                                    print(posiciones_dichas_2)
                                if (tota == len(posiciones2)):  # en caso de que todas las posiciones que las posiciones introducidas por el usuario esten en la lista de las posiciones donde hay barcos, gana la partida.
                                    print("Ha ganado el PC!")
                                    time.sleep(1)
                                    print(":c")
                                    time.sleep(1)
                                    for o in tablero_del_user_para_pc:
                                        print(tablero_del_user_para_pc[o])
                                    time.sleep(1)
                                    print("Este es el tablero final!")
                                    ganador = "pc"
                    elif (casilla not in posiciones2):
                        if (tablero_del_user_para_pc[b][n] == casilla):
                            print("Agua")
                            tablero_del_user_para_pc[b][n] = "~~"
                            posiciones_dichas_2.append(casilla)
        time.sleep(2)
        for x in tablero_del_user_para_pc:
            print(tablero_del_user_para_pc[x])
        time.sleep(2)