import random, time
#funciones Hundir_la_flota, Barcos_del_pc, Barcos_del_user, Hundir_la_flota_turno_pc, Hundir_la_flota_turno_user, Partida_terminada
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
    todos_los_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letras_posibles = ["A","B","C","D","E","F","G"]
    todas_las_letras = ["A","B","C","D","E","F","G","H","I","J"]
    posiciones = []
    posiciones_no_disp = []
    for cont in range(1, 100):
        time.sleep(0.03)
        print("Cargando...", cont, "%")
    time.sleep(1)
    print("Hundir la Flota ha cargado exitosamente!")
    time.sleep(1)
    decision_normas = input("Desea repasar las normas rápidamente? (SI/NO):")
    if (decision_normas == "SI" or decision_normas == "Si" or decision_normas == "si" or decision_normas == "sI" or decision_normas == "s" or decision_normas == "S"):
        print("Ok! Te recordare las normas.")
        time.sleep(2)
        print("El juego consiste en hundir la flota del contrincante, el cual sera el PC.")
        time.sleep(3)
        print("Ambos dispondrán de un tablero como este:")
        time.sleep(3)
        for x in tablero:
            print(tablero[x])
        time.sleep(4)
        print("En este Tablero habrá que ir colocando diferentes barcos de distintos tamaños:")
        time.sleep(4)
        print("1 barco de 4 cuadros.")
        time.sleep(3)
        print("2 barcos de 3 cuadros.")
        time.sleep(3)
        print("3 barcos de 2 cuadros.")
        time.sleep(3)
        print("4 barcos 1 cuadro.")
        time.sleep(3)
        print("Los barcos se tienen que colocar respetando una franja de cuadros en blanco alrededor.")
        time.sleep(5)
        print("Sí pueden colocarse junto a los bordes de la cuadrícula, pero sin llegar a pegarse un barco con otro.")
        time.sleep(5)
        print("Habra que decir las casillas en las cuales se desea colocar el barco en orden Alfabeticamente [A-Z] y Numericamente [0-9](de menor a mayor).")
        time.sleep(5)
        print("Se iran turnando una vez cada uno, para lanzar un mísil a la casilla deseada.")
        time.sleep(5)
        print("Ganara el primero que logre destruir la flota enemiga, y por ende se terminara el juego.")
        time.sleep(5)
        print("Eso es todo.")
        time.sleep(2)
    print("Empieza el juego.")
    time.sleep(2)
    print("Buena suerte!")
    tab_pc = Barcos_del_pc(numeros_posibles,letras_posibles,todas_las_letras,posiciones,tablero_ordenador,posiciones_no_disp,todos_los_numeros)
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
    posiciones_no_disp2 = []
    tab_user = Barcos_del_user(posiciones_user,posiciones_vert,posiciones_hori,tablero,todas_las_letras,posiciones_no_disp2,todos_los_numeros)
    print("Empieza el juego!")
    while (True):
        Hundir_la_flota_turno_pc(tablero_del_pc_para_user,posiciones_vert,posiciones,posiciones_dichas)
        Hundir_la_flota_turno_user(tablero_del_user_para_pc, posiciones_vert, posiciones_dichas_2,posiciones_user)

def Barcos_del_pc(numeros_posibles,letras_posibles,todas_las_letras,posiciones,tablero_ordenador,posiciones_no_disp,todos_los_numeros):
    print("Le toca al PC asignarse las posiciones de los barcos.")
    time.sleep(3)
    while (len(posiciones) < 20):
        while (len(posiciones) < 3):  # barco de 4 casillas (solo hay uno)
            barco = random.randint(1, 2)
            if (barco == 1):  # HORIZONTAL   #EJ: A1, A2, A3, A4
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(todas_las_letras)
                p1 = pri_letra + str(pri_num)
                p2 = pri_letra + str(pri_num + 1)
                p3 = pri_letra + str(pri_num + 2)
                p4 = pri_letra + str(pri_num + 3)
                posiciones.append(p1)
                posiciones.append(p2)
                posiciones.append(p3)
                posiciones.append(p4)
                for ir in range(len(todas_las_letras)):
                    if (pri_letra == "A" and pri_letra == todas_las_letras[ir]):
                        p_1 = todas_las_letras[ir+1] + str(pri_num)
                        p_2 = todas_las_letras[ir+1] + str(pri_num + 1)
                        p_3 = todas_las_letras[ir+1] + str(pri_num + 2)
                        p_4 = todas_las_letras[ir+1] + str(pri_num + 3)
                        posiciones_no_disp.append(p_1)
                        posiciones_no_disp.append(p_2)
                        posiciones_no_disp.append(p_3)
                        posiciones_no_disp.append(p_4)
                        if (pri_num == 0):
                            p_5 = todas_las_letras[ir+1] + str(pri_num + 4)
                            p_6 = pri_letra + str(pri_num + 4)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        elif (pri_num == 6):
                            p_5 = todas_las_letras[ir+1] + str(pri_num - 1)
                            p_6 = pri_letra + str(pri_num-1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        else:
                            p_5 = todas_las_letras[ir + 1] + str(pri_num + 4)
                            p_6 = pri_letra + str(pri_num + 4)
                            p_7 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            p_8 = pri_letra + str(pri_num - 1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                            posiciones_no_disp.append(p_7)
                            posiciones_no_disp.append(p_8)
                    elif (pri_letra == "J" and pri_letra == todas_las_letras[ir]):
                        p_1 = todas_las_letras[ir - 1] + str(pri_num)
                        p_2 = todas_las_letras[ir - 1] + str(pri_num + 1)
                        p_3 = todas_las_letras[ir - 1] + str(pri_num + 2)
                        p_4 = todas_las_letras[ir - 1] + str(pri_num + 3)
                        posiciones_no_disp.append(p_1)
                        posiciones_no_disp.append(p_2)
                        posiciones_no_disp.append(p_3)
                        posiciones_no_disp.append(p_4)
                        if (pri_num == 0):
                            p_5 = todas_las_letras[ir-1] + str(pri_num + 4)
                            p_6 = pri_letra + str(pri_num + 4)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        elif (pri_num == 6):
                            p_5 = todas_las_letras[ir-1] + str(pri_num - 1)
                            p_6 = pri_letra + str(pri_num-1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        else:
                            p_5 = todas_las_letras[ir - 1] + str(pri_num + 4)
                            p_6 = pri_letra + str(pri_num + 4)
                            p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            p_8 = pri_letra + str(pri_num - 1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                            posiciones_no_disp.append(p_7)
                            posiciones_no_disp.append(p_8)
                    elif (pri_letra == todas_las_letras[ir]):
                        p_1 = todas_las_letras[ir + 1] + str(pri_num)
                        p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                        p_3 = todas_las_letras[ir + 1] + str(pri_num + 2)
                        p_4 = todas_las_letras[ir + 1] + str(pri_num + 3)
                        posiciones_no_disp.append(p_1)
                        posiciones_no_disp.append(p_2)
                        posiciones_no_disp.append(p_3)
                        posiciones_no_disp.append(p_4)
                        p_7 = todas_las_letras[ir - 1] + str(pri_num)
                        p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                        p_9 = todas_las_letras[ir - 1] + str(pri_num + 2)
                        p_10 = todas_las_letras[ir - 1] + str(pri_num + 3)
                        posiciones_no_disp.append(p_7)
                        posiciones_no_disp.append(p_8)
                        posiciones_no_disp.append(p_9)
                        posiciones_no_disp.append(p_10)
                        if (pri_num == 0):
                            p_5 = todas_las_letras[ir + 1] + str(pri_num + 4)
                            posiciones_no_disp.append(p_5)
                            p_11 = todas_las_letras[ir - 1] + str(pri_num + 4)
                            posiciones_no_disp.append(p_11)
                            p_13 = pri_letra + str(pri_num + 4)
                            posiciones_no_disp.append(p_13)
                        elif (pri_num == 6):
                            p_0 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            posiciones_no_disp.append(p_0)
                            p_6 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            posiciones_no_disp.append(p_6)
                            p_12 = pri_letra + str(pri_num - 1)
                            posiciones_no_disp.append(p_12)
                        else:
                            p_0 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            p_5 = todas_las_letras[ir + 1] + str(pri_num + 4)
                            posiciones_no_disp.append(p_0)
                            posiciones_no_disp.append(p_5)
                            p_6 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            p_11 = todas_las_letras[ir - 1] + str(pri_num + 4)
                            posiciones_no_disp.append(p_6)
                            posiciones_no_disp.append(p_11)
                            p_12 = pri_letra + str(pri_num - 1)
                            p_13 = pri_letra + str(pri_num + 4)
                            posiciones_no_disp.append(p_12)
                            posiciones_no_disp.append(p_13)
                        break
            else:  # VERTICAL     #EJ: A1, B1, C1, D1
                pri_num = random.choice(todos_los_numeros)
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
                        for ir in range(len(todas_las_letras)):
                            if (pri_num == 0 and pri_letra == todas_las_letras[ir]):
                                p_1 = todas_las_letras[ir + 0] + str(pri_num + 1)
                                p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                                p_3 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                p_4 = todas_las_letras[ir + 3] + str(pri_num + 1)
                                posiciones_no_disp.append(p_1)
                                posiciones_no_disp.append(p_2)
                                posiciones_no_disp.append(p_3)
                                posiciones_no_disp.append(p_4)
                                if (pri_letra == "A"):
                                    p_5 = todas_las_letras[ir + 4] + str(pri_num)
                                    p_6 = todas_las_letras[ir + 4] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                elif (pri_letra == "G"):
                                    p_5 = todas_las_letras[ir - 1] + str(pri_num)
                                    p_6 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                else:
                                    p_5 = todas_las_letras[ir + 4] + str(pri_num)
                                    p_6 = todas_las_letras[ir + 4] + str(pri_num + 1)
                                    p_7 = todas_las_letras[ir - 1] + str(pri_num)
                                    p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                    posiciones_no_disp.append(p_7)
                                    posiciones_no_disp.append(p_8)
                            elif (pri_num == 9 and pri_letra == todas_las_letras[ir]):
                                p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)#g8
                                p_2 = todas_las_letras[ir + 1] + str(pri_num - 1)#h8
                                p_3 = todas_las_letras[ir + 2] + str(pri_num - 1)#i8
                                p_4 = todas_las_letras[ir + 3] + str(pri_num - 1)#j8
                                posiciones_no_disp.append(p_1)
                                posiciones_no_disp.append(p_2)
                                posiciones_no_disp.append(p_3)
                                posiciones_no_disp.append(p_4)
                                if (pri_letra == "A"):
                                    p_5 = todas_las_letras[ir + 4] + str(pri_num - 1)
                                    p_6 = todas_las_letras[ir + 4] + str(pri_num)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                elif (pri_letra == "G"):
                                    p_5 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                    p_6 = todas_las_letras[ir - 1] + str(pri_num)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                else:
                                    p_5 = todas_las_letras[ir + 4] + str(pri_num - 1)
                                    p_6 = todas_las_letras[ir + 4] + str(pri_num)
                                    p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                    p_8 = todas_las_letras[ir - 1] + str(pri_num)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                    posiciones_no_disp.append(p_7)
                                    posiciones_no_disp.append(p_8)
                            elif (pri_letra == todas_las_letras[ir]):
                                p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)
                                p_2 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                p_3 = todas_las_letras[ir + 2] + str(pri_num - 1)
                                p_4 = todas_las_letras[ir + 3] + str(pri_num - 1)
                                p_5 = todas_las_letras[ir + 0] + str(pri_num + 1)
                                p_6 = todas_las_letras[ir + 1] + str(pri_num + 1)
                                p_7 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                p_8 = todas_las_letras[ir + 3] + str(pri_num + 1)
                                posiciones_no_disp.append(p_1)
                                posiciones_no_disp.append(p_2)
                                posiciones_no_disp.append(p_3)
                                posiciones_no_disp.append(p_4)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                                posiciones_no_disp.append(p_7)
                                posiciones_no_disp.append(p_8)
                                if (pri_letra == "A"):
                                    p_9 = todas_las_letras[ir + 4] + str(pri_num - 1)
                                    p_10 = todas_las_letras[ir + 4] + str(pri_num + 1)
                                    p_11 = todas_las_letras[ir + 4] + str(pri_num)
                                    posiciones_no_disp.append(p_9)
                                    posiciones_no_disp.append(p_10)
                                    posiciones_no_disp.append(p_11)
                                elif (pri_letra == "G"):
                                    p_9 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                    p_10 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                    p_11 = todas_las_letras[ir - 1] + str(pri_num)
                                    posiciones_no_disp.append(p_9)
                                    posiciones_no_disp.append(p_10)
                                    posiciones_no_disp.append(p_11)
                                else:
                                    p_9 = todas_las_letras[ir + 4] + str(pri_num - 1)
                                    p_10 = todas_las_letras[ir + 4] + str(pri_num + 1)
                                    p_11 = todas_las_letras[ir + 4] + str(pri_num)
                                    p_12 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                    p_13 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                    p_14 = todas_las_letras[ir - 1] + str(pri_num)
                                    posiciones_no_disp.append(p_9)
                                    posiciones_no_disp.append(p_10)
                                    posiciones_no_disp.append(p_11)
                                    posiciones_no_disp.append(p_12)
                                    posiciones_no_disp.append(p_13)
                                    posiciones_no_disp.append(p_14)
        letras_posibles.append("H")
        while (len(posiciones) > 3 and len(posiciones) < 9):  # aqui haremos los dos barcos de 3 casillas
            barco = random.randint(1, 2)
            if (barco == 1):  # HORIZONTAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(todas_las_letras)
                p1 = pri_letra + str(pri_num)
                p2 = pri_letra + str(pri_num + 1)
                p3 = pri_letra + str(pri_num + 2)
                if (p1 not in posiciones and p1 not in posiciones_no_disp and p2 not in posiciones and p2 not in posiciones_no_disp and p3 not in posiciones and p3 not in posiciones_no_disp):
                    posiciones.append(p1)
                    posiciones.append(p2)
                    posiciones.append(p3)
                    for ir in range(len(todas_las_letras)):
                        if (pri_letra == "A" and pri_letra == todas_las_letras[ir]):
                            p_1 = todas_las_letras[ir + 1] + str(pri_num)
                            p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            p_3 = todas_las_letras[ir + 1] + str(pri_num + 2)
                            posiciones_no_disp.append(p_1)
                            posiciones_no_disp.append(p_2)
                            posiciones_no_disp.append(p_3)
                            if (pri_num == 0):
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 3)
                                p_6 = pri_letra + str(pri_num + 3)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            elif (pri_num == 7):
                                p_5 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                p_6 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            else:
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 3)
                                p_6 = pri_letra + str(pri_num + 3)
                                p_7 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                p_8 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                                posiciones_no_disp.append(p_7)
                                posiciones_no_disp.append(p_8)

                        elif (pri_letra == "J" and pri_letra == todas_las_letras[ir]):
                            p_1 = todas_las_letras[ir - 1] + str(pri_num)
                            p_2 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            p_3 = todas_las_letras[ir - 1] + str(pri_num + 2)
                            posiciones_no_disp.append(p_1)
                            posiciones_no_disp.append(p_2)
                            posiciones_no_disp.append(p_3)
                            if (pri_num == 0):
                                p_5 = todas_las_letras[ir - 1] + str(pri_num + 3)
                                p_6 = pri_letra + str(pri_num + 3)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            elif (pri_num == 7):
                                p_5 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                p_6 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            else:
                                p_5 = todas_las_letras[ir - 1] + str(pri_num + 3)
                                p_6 = pri_letra + str(pri_num + 3)
                                p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                p_8 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                                posiciones_no_disp.append(p_7)
                                posiciones_no_disp.append(p_8)

                        elif (pri_letra == todas_las_letras[ir]):
                            p_1 = todas_las_letras[ir + 1] + str(pri_num)
                            p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            p_3 = todas_las_letras[ir + 1] + str(pri_num + 2)
                            posiciones_no_disp.append(p_1)
                            posiciones_no_disp.append(p_2)
                            posiciones_no_disp.append(p_3)
                            p_7 = todas_las_letras[ir - 1] + str(pri_num)
                            p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            p_9 = todas_las_letras[ir - 1] + str(pri_num + 2)
                            posiciones_no_disp.append(p_7)
                            posiciones_no_disp.append(p_8)
                            posiciones_no_disp.append(p_9)
                            if (pri_num == 0):
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 3)
                                posiciones_no_disp.append(p_5)
                                p_11 = todas_las_letras[ir - 1] + str(pri_num + 3)
                                posiciones_no_disp.append(p_11)
                                p_13 = pri_letra + str(pri_num + 3)
                                posiciones_no_disp.append(p_13)
                            elif (pri_num == 7):
                                p_0 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                posiciones_no_disp.append(p_0)
                                p_6 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                posiciones_no_disp.append(p_6)
                                p_12 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_12)
                            else:
                                p_0 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 3)
                                posiciones_no_disp.append(p_0)
                                posiciones_no_disp.append(p_5)
                                p_6 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                p_11 = todas_las_letras[ir - 1] + str(pri_num + 3)
                                posiciones_no_disp.append(p_6)
                                posiciones_no_disp.append(p_11)
                                p_12 = pri_letra + str(pri_num - 1)
                                p_13 = pri_letra + str(pri_num + 4)
                                posiciones_no_disp.append(p_12)
                                posiciones_no_disp.append(p_13)
                            break
                else:  # si la posicion creada ya esta ocupada por otro barco:
                    continue
            else:  # VERTICAL
                pri_num = random.choice(todos_los_numeros)
                pri_letra = random.choice(letras_posibles)
                for x in range(len(todas_las_letras)):
                    if (pri_letra == todas_las_letras[x]):
                        p1 = todas_las_letras[x + 0] + str(pri_num)
                        p2 = todas_las_letras[x + 1] + str(pri_num)
                        p3 = todas_las_letras[x + 2] + str(pri_num)
                        if (p1 not in posiciones and p1 not in posiciones_no_disp and p2 not in posiciones and p2 not in posiciones_no_disp and p3 not in posiciones and p3 not in posiciones_no_disp):
                            posiciones.append(p1)
                            posiciones.append(p2)
                            posiciones.append(p3)
                            for ir in range(len(todas_las_letras)):
                                if (pri_num == 0 and pri_letra == todas_las_letras[ir]):
                                    p_1 = todas_las_letras[ir + 0] + str(pri_num + 1)
                                    p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                                    p_3 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_1)
                                    posiciones_no_disp.append(p_2)
                                    posiciones_no_disp.append(p_3)
                                    if (pri_letra == "A"):
                                        p_5 = todas_las_letras[ir + 3] + str(pri_num)
                                        p_6 = todas_las_letras[ir + 3] + str(pri_num + 1)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    elif (pri_letra == "H"):
                                        p_5 = todas_las_letras[ir - 1] + str(pri_num)
                                        p_6 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    else:
                                        p_5 = todas_las_letras[ir + 3] + str(pri_num)
                                        p_6 = todas_las_letras[ir + 3] + str(pri_num + 1)
                                        p_7 = todas_las_letras[ir - 1] + str(pri_num)
                                        p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                        posiciones_no_disp.append(p_7)
                                        posiciones_no_disp.append(p_8)

                                elif (pri_num == 9 and pri_letra == todas_las_letras[ir]):
                                    p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)  # g8
                                    p_2 = todas_las_letras[ir + 1] + str(pri_num - 1)  # h8
                                    p_3 = todas_las_letras[ir + 2] + str(pri_num - 1)  # i8
                                    posiciones_no_disp.append(p_1)
                                    posiciones_no_disp.append(p_2)
                                    posiciones_no_disp.append(p_3)
                                    if (pri_letra == "A"):
                                        p_5 = todas_las_letras[ir + 3] + str(pri_num - 1)
                                        p_6 = todas_las_letras[ir + 3] + str(pri_num)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    elif (pri_letra == "H"):
                                        p_5 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_6 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    else:
                                        p_5 = todas_las_letras[ir + 3] + str(pri_num - 1)
                                        p_6 = todas_las_letras[ir + 3] + str(pri_num)
                                        p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_8 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                        posiciones_no_disp.append(p_7)
                                        posiciones_no_disp.append(p_8)

                                elif (pri_letra == todas_las_letras[ir]):
                                    p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)
                                    p_2 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                    p_3 = todas_las_letras[ir + 2] + str(pri_num - 1)
                                    p_5 = todas_las_letras[ir + 0] + str(pri_num + 1)
                                    p_6 = todas_las_letras[ir + 1] + str(pri_num + 1)
                                    p_7 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_1)
                                    posiciones_no_disp.append(p_2)
                                    posiciones_no_disp.append(p_3)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                    posiciones_no_disp.append(p_7)
                                    if (pri_letra == "A"):
                                        p_9 = todas_las_letras[ir + 3] + str(pri_num - 1)
                                        p_10 = todas_las_letras[ir + 3] + str(pri_num + 1)
                                        p_11 = todas_las_letras[ir + 3] + str(pri_num)
                                        posiciones_no_disp.append(p_9)
                                        posiciones_no_disp.append(p_10)
                                        posiciones_no_disp.append(p_11)
                                    elif (pri_letra == "H"):
                                        p_9 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_10 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        p_11 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_9)
                                        posiciones_no_disp.append(p_10)
                                        posiciones_no_disp.append(p_11)
                                    else:
                                        p_9 = todas_las_letras[ir + 3] + str(pri_num - 1)
                                        p_10 = todas_las_letras[ir + 3] + str(pri_num + 1)
                                        p_11 = todas_las_letras[ir + 3] + str(pri_num)
                                        p_12 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_13 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        p_14 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_9)
                                        posiciones_no_disp.append(p_10)
                                        posiciones_no_disp.append(p_11)
                                        posiciones_no_disp.append(p_12)
                                        posiciones_no_disp.append(p_13)
                                        posiciones_no_disp.append(p_14)
                        else:  # si la posicion creada ya esta ocupada por otro barco:
                            continue
        letras_posibles.append("I")
        while (len(posiciones) > 9 and len(posiciones) < 15):  # aqui haremos los tres barcos de 2 casillas
            barco = random.randint(1, 2)
            if (barco == 1):  # HORIZONTAL
                pri_num = random.choice(numeros_posibles)
                pri_letra = random.choice(todas_las_letras)
                p1 = pri_letra + str(pri_num)
                p2 = pri_letra + str(pri_num + 1)
                if (p1 not in posiciones and p1 not in posiciones_no_disp and p2 not in posiciones and p2 not in posiciones_no_disp):
                    posiciones.append(p1)
                    posiciones.append(p2)
                    for ir in range(len(todas_las_letras)):
                        if (pri_letra == "A" and pri_letra == todas_las_letras[ir]):
                            p_1 = todas_las_letras[ir + 1] + str(pri_num)
                            p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_1)
                            posiciones_no_disp.append(p_2)
                            if (pri_num == 0):
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 2)
                                p_6 = pri_letra + str(pri_num + 2)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            elif (pri_num == 8):
                                p_5 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                p_6 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            else:
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 2)
                                p_6 = pri_letra + str(pri_num + 2)
                                p_7 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                p_8 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                                posiciones_no_disp.append(p_7)
                                posiciones_no_disp.append(p_8)

                        elif (pri_letra == "J" and pri_letra == todas_las_letras[ir]):
                            p_1 = todas_las_letras[ir - 1] + str(pri_num)
                            p_2 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_1)
                            posiciones_no_disp.append(p_2)
                            if (pri_num == 0):
                                p_5 = todas_las_letras[ir - 1] + str(pri_num + 2)
                                p_6 = pri_letra + str(pri_num + 2)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            elif (pri_num == 8):
                                p_5 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                p_6 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                            else:
                                p_5 = todas_las_letras[ir - 1] + str(pri_num + 2)
                                p_6 = pri_letra + str(pri_num + 2)
                                p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                p_8 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_5)
                                posiciones_no_disp.append(p_6)
                                posiciones_no_disp.append(p_7)
                                posiciones_no_disp.append(p_8)

                        elif (pri_letra == todas_las_letras[ir]):
                            p_1 = todas_las_letras[ir + 1] + str(pri_num)
                            p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_1)
                            posiciones_no_disp.append(p_2)
                            p_7 = todas_las_letras[ir - 1] + str(pri_num)
                            p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_7)
                            posiciones_no_disp.append(p_8)
                            if (pri_num == 0):
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 2)
                                posiciones_no_disp.append(p_5)
                                p_11 = todas_las_letras[ir - 1] + str(pri_num + 2)
                                posiciones_no_disp.append(p_11)
                                p_13 = pri_letra + str(pri_num + 2)
                                posiciones_no_disp.append(p_13)
                            elif (pri_num == 8):
                                p_0 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                posiciones_no_disp.append(p_0)
                                p_6 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                posiciones_no_disp.append(p_6)
                                p_12 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_12)
                            else:
                                p_5 = todas_las_letras[ir + 1] + str(pri_num + 2)
                                posiciones_no_disp.append(p_5)
                                p_11 = todas_las_letras[ir - 1] + str(pri_num + 2)
                                posiciones_no_disp.append(p_11)
                                p_13 = pri_letra + str(pri_num + 2)
                                posiciones_no_disp.append(p_13)
                                p_0 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                posiciones_no_disp.append(p_0)
                                p_6 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                posiciones_no_disp.append(p_6)
                                p_12 = pri_letra + str(pri_num - 1)
                                posiciones_no_disp.append(p_12)

                            break
                else:  # si la posicion creada ya esta ocupada por otro barco:
                    continue
            else:  # VERTICAL
                pri_num = random.choice(todos_los_numeros)
                pri_letra = random.choice(letras_posibles)
                for x in range(len(todas_las_letras)):
                    if (pri_letra == todas_las_letras[x]):
                        p1 = todas_las_letras[x + 0] + str(pri_num)
                        p2 = todas_las_letras[x + 1] + str(pri_num)
                        if (p1 not in posiciones and p1 not in posiciones_no_disp and p2 not in posiciones and p2 not in posiciones_no_disp):
                            posiciones.append(p1)
                            posiciones.append(p2)
                            for ir in range(len(todas_las_letras)):
                                if (pri_num == 0 and pri_letra == todas_las_letras[ir]):
                                    p_1 = todas_las_letras[ir + 0] + str(pri_num + 1)
                                    p_2 = todas_las_letras[ir + 1] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_1)
                                    posiciones_no_disp.append(p_2)
                                    if (pri_letra == "A"):
                                        p_5 = todas_las_letras[ir + 2] + str(pri_num)
                                        p_6 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    elif (pri_letra == "I"):
                                        p_5 = todas_las_letras[ir - 1] + str(pri_num)
                                        p_6 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    else:
                                        p_5 = todas_las_letras[ir + 2] + str(pri_num)
                                        p_6 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                        p_7 = todas_las_letras[ir - 1] + str(pri_num)
                                        p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                        posiciones_no_disp.append(p_7)
                                        posiciones_no_disp.append(p_8)

                                elif (pri_num == 9 and pri_letra == todas_las_letras[ir]):
                                    p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)
                                    p_2 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                    posiciones_no_disp.append(p_1)
                                    posiciones_no_disp.append(p_2)
                                    if (pri_letra == "A"):
                                        p_5 = todas_las_letras[ir + 2] + str(pri_num - 1)
                                        p_6 = todas_las_letras[ir + 2] + str(pri_num)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    elif (pri_letra == "I"):
                                        p_5 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_6 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                    else:
                                        p_5 = todas_las_letras[ir + 2] + str(pri_num - 1)
                                        p_6 = todas_las_letras[ir + 2] + str(pri_num)
                                        p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_8 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_5)
                                        posiciones_no_disp.append(p_6)
                                        posiciones_no_disp.append(p_7)
                                        posiciones_no_disp.append(p_8)

                                elif (pri_letra == todas_las_letras[ir]):
                                    p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)
                                    p_2 = todas_las_letras[ir + 1] + str(pri_num - 1)
                                    p_5 = todas_las_letras[ir + 0] + str(pri_num + 1)
                                    p_6 = todas_las_letras[ir + 1] + str(pri_num + 1)
                                    posiciones_no_disp.append(p_1)
                                    posiciones_no_disp.append(p_2)
                                    posiciones_no_disp.append(p_5)
                                    posiciones_no_disp.append(p_6)
                                    if (pri_letra == "A"):
                                        p_9 = todas_las_letras[ir + 2] + str(pri_num - 1)
                                        p_10 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                        p_11 = todas_las_letras[ir + 2] + str(pri_num)
                                        posiciones_no_disp.append(p_9)
                                        posiciones_no_disp.append(p_10)
                                        posiciones_no_disp.append(p_11)
                                    elif (pri_letra == "I"):
                                        p_9 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_10 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        p_11 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_9)
                                        posiciones_no_disp.append(p_10)
                                        posiciones_no_disp.append(p_11)
                                    else:
                                        p_9 = todas_las_letras[ir + 2] + str(pri_num - 1)
                                        p_10 = todas_las_letras[ir + 2] + str(pri_num + 1)
                                        p_11 = todas_las_letras[ir + 2] + str(pri_num)
                                        p_12 = todas_las_letras[ir - 1] + str(pri_num - 1)
                                        p_13 = todas_las_letras[ir - 1] + str(pri_num + 1)
                                        p_14 = todas_las_letras[ir - 1] + str(pri_num)
                                        posiciones_no_disp.append(p_9)
                                        posiciones_no_disp.append(p_10)
                                        posiciones_no_disp.append(p_11)
                                        posiciones_no_disp.append(p_12)
                                        posiciones_no_disp.append(p_13)
                                        posiciones_no_disp.append(p_14)
                        else:
                            continue
        letras_posibles.append("J")
        while (len(posiciones) > 15 and len(posiciones) < 20):  # aqui haremos los cuatro barcos de 1 casilla
            # HORIZONTAL = VERTICAL, PQ SOLO ES DE UNA CASILLA
            pri_num = random.choice(todos_los_numeros)
            pri_letra = random.choice(todas_las_letras)
            p1 = pri_letra + str(pri_num)
            if (p1 not in posiciones and p1 not in posiciones_no_disp):
                posiciones.append(p1)
                for ir in range(len(todas_las_letras)):
                    if (pri_num == 0 and pri_letra == todas_las_letras[ir]):
                        p_1 = todas_las_letras[ir + 0] + str(pri_num + 1)
                        posiciones_no_disp.append(p_1)
                        if (pri_letra == "A"):
                            p_5 = todas_las_letras[ir + 1] + str(pri_num)
                            p_6 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        elif (pri_letra == "J"):
                            p_5 = todas_las_letras[ir - 1] + str(pri_num)
                            p_6 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        else:
                            p_5 = todas_las_letras[ir + 1] + str(pri_num)
                            p_6 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            p_7 = todas_las_letras[ir - 1] + str(pri_num)
                            p_8 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                            posiciones_no_disp.append(p_7)
                            posiciones_no_disp.append(p_8)
                    elif (pri_num == 9 and pri_letra == todas_las_letras[ir]):
                        p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)
                        posiciones_no_disp.append(p_1)
                        if (pri_letra == "A"):
                            p_5 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            p_6 = todas_las_letras[ir + 1] + str(pri_num)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        elif (pri_letra == "J"):
                            p_5 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            p_6 = todas_las_letras[ir - 1] + str(pri_num)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                        else:
                            p_5 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            p_6 = todas_las_letras[ir + 1] + str(pri_num)
                            p_7 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            p_8 = todas_las_letras[ir - 1] + str(pri_num)
                            posiciones_no_disp.append(p_5)
                            posiciones_no_disp.append(p_6)
                            posiciones_no_disp.append(p_7)
                            posiciones_no_disp.append(p_8)
                    elif (pri_letra == todas_las_letras[ir]):
                        p_1 = todas_las_letras[ir + 0] + str(pri_num - 1)
                        p_5 = todas_las_letras[ir + 0] + str(pri_num + 1)
                        posiciones_no_disp.append(p_1)
                        posiciones_no_disp.append(p_5)
                        if (pri_letra == "A"):
                            p_9 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            p_10 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            p_11 = todas_las_letras[ir + 1] + str(pri_num)
                            posiciones_no_disp.append(p_9)
                            posiciones_no_disp.append(p_10)
                            posiciones_no_disp.append(p_11)
                        elif (pri_letra == "J"):
                            p_9 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            p_10 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            p_11 = todas_las_letras[ir - 1] + str(pri_num)
                            posiciones_no_disp.append(p_9)
                            posiciones_no_disp.append(p_10)
                            posiciones_no_disp.append(p_11)
                        else:
                            p_9 = todas_las_letras[ir + 1] + str(pri_num - 1)
                            p_10 = todas_las_letras[ir + 1] + str(pri_num + 1)
                            p_11 = todas_las_letras[ir + 1] + str(pri_num)
                            p_12 = todas_las_letras[ir - 1] + str(pri_num - 1)
                            p_13 = todas_las_letras[ir - 1] + str(pri_num + 1)
                            p_14 = todas_las_letras[ir - 1] + str(pri_num)
                            posiciones_no_disp.append(p_9)
                            posiciones_no_disp.append(p_10)
                            posiciones_no_disp.append(p_11)
                            posiciones_no_disp.append(p_12)
                            posiciones_no_disp.append(p_13)
                            posiciones_no_disp.append(p_14)
            else:  # si la posicion creada ya esta ocupada por otro barco:
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

    for x in range(len(posiciones_no_disp)):
        for z in range(10):  # de 0 a 9
            if (posiciones_no_disp[x] == (todas_las_letras[0] + str(z))):
                tablero_ordenador[todas_las_letras[0]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[1] + str(z))):
                tablero_ordenador[todas_las_letras[1]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[2] + str(z))):
                tablero_ordenador[todas_las_letras[2]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[3] + str(z))):
                tablero_ordenador[todas_las_letras[3]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[4] + str(z))):
                tablero_ordenador[todas_las_letras[4]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[5] + str(z))):
                tablero_ordenador[todas_las_letras[5]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[6] + str(z))):
                tablero_ordenador[todas_las_letras[6]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[7] + str(z))):
                tablero_ordenador[todas_las_letras[7]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[8] + str(z))):
                tablero_ordenador[todas_las_letras[8]][z] = "--"
            elif (posiciones_no_disp[x] == (todas_las_letras[9] + str(z))):
                tablero_ordenador[todas_las_letras[9]][z] = "--"

    return tablero_ordenador

def Barcos_del_user(posiciones_user,posiciones_vert,posiciones_hori,tablero,todas_las_letras,posiciones_no_disp2,todos_los_numeros):
    while (len(posiciones_user) < 20):
        print("Te toca elegir donde quieres poner los barcos.")
        time.sleep(3)
        for we in tablero:
            print(tablero[we])
        while (len(posiciones_user) < 3):  # barco de 4 casillas (solo hay uno)
            print("Turno para crear el barco de 4 casillas.")
            dir = input("Quieres crear el barco horizontal o vertical? (H,V):")
            c1 = input("Dime la 1/4 casilla que ocupara el barco:")
            c2 = input("Dime la 2/4 casilla que ocupara el barco:")
            c3 = input("Dime la 3/4 casilla que ocupara el barco:")
            c4 = input("Dime la 4/4 casilla que ocupara el barco:")
            if (dir == "V" or dir == "v" or dir == "Vertical" or dir == "vertical" or dir == "Verticalmente" or dir == "verticalmente"):
                for e in range(len(posiciones_vert)):
                    if (c1 == posiciones_vert[e]):
                        if ((c2 == posiciones_vert[e + 1] and c3 == posiciones_vert[e + 2] and c4 == posiciones_vert[e + 3])):
                            posiciones_user.append(c1)
                            posiciones_user.append(c2)
                            posiciones_user.append(c3)
                            posiciones_user.append(c4)
                            print("Posiciones asignadas correctamente!")
                            for l in range(len(todas_las_letras)):
                                for n in range(len(todos_los_numeros)):
                                    if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[n] == 0):
                                        p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] + 1)
                                        p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_3 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                        p_4 = todas_las_letras[l + 3] + str(todos_los_numeros[n] + 1)
                                        posiciones_no_disp2.append(p_1)
                                        posiciones_no_disp2.append(p_2)
                                        posiciones_no_disp2.append(p_3)
                                        posiciones_no_disp2.append(p_4)
                                        if (todas_las_letras[l] == "A"):
                                            p_5 = todas_las_letras[l + 4] + str(todos_los_numeros[n])
                                            p_6 = todas_las_letras[l + 4] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        elif (todas_las_letras[l] == "G"):
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        else:
                                            p_5 = todas_las_letras[l + 4] + str(todos_los_numeros[n])
                                            p_6 = todas_las_letras[l + 4] + str(todos_los_numeros[n] + 1)
                                            p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            posiciones_no_disp2.append(p_7)
                                            posiciones_no_disp2.append(p_8)
                                    elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[
                                        n] == 9):
                                        p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] - 1)
                                        p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                        p_3 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                        p_4 = todas_las_letras[l + 3] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_1)
                                        posiciones_no_disp2.append(p_2)
                                        posiciones_no_disp2.append(p_3)
                                        posiciones_no_disp2.append(p_4)
                                        if (todas_las_letras[l] == "A"):
                                            p_5 = todas_las_letras[l + 4] + str(todos_los_numeros[n] - 1)
                                            p_6 = todas_las_letras[l + 4] + str(todos_los_numeros[n])
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        elif (todas_las_letras[l] == "G"):
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        else:
                                            p_5 = todas_las_letras[l + 4] + str(todos_los_numeros[n] - 1)
                                            p_6 = todas_las_letras[l + 4] + str(todos_los_numeros[n])
                                            p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            posiciones_no_disp2.append(p_7)
                                            posiciones_no_disp2.append(p_8)
                                    elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[
                                        n] != 9 and todos_los_numeros[n] != 0):
                                        p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] - 1)
                                        p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                        p_3 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                        p_4 = todas_las_letras[l + 3] + str(todos_los_numeros[n] - 1)
                                        p_5 = todas_las_letras[l + 0] + str(todos_los_numeros[n] + 1)
                                        p_6 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_7 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                        p_8 = todas_las_letras[l + 3] + str(todos_los_numeros[n] + 1)
                                        posiciones_no_disp2.append(p_1)
                                        posiciones_no_disp2.append(p_2)
                                        posiciones_no_disp2.append(p_3)
                                        posiciones_no_disp2.append(p_4)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                        posiciones_no_disp2.append(p_7)
                                        posiciones_no_disp2.append(p_8)
                                        if (todas_las_letras[l] == "A"):
                                            p_9 = todas_las_letras[l + 4] + str(todos_los_numeros[n] - 1)
                                            p_10 = todas_las_letras[l + 4] + str(todos_los_numeros[n] + 1)
                                            p_11 = todas_las_letras[l + 4] + str(todos_los_numeros[n])
                                            posiciones_no_disp2.append(p_9)
                                            posiciones_no_disp2.append(p_10)
                                            posiciones_no_disp2.append(p_11)
                                        elif (todas_las_letras[l] == "G"):
                                            p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_10 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            p_11 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            posiciones_no_disp2.append(p_9)
                                            posiciones_no_disp2.append(p_10)
                                            posiciones_no_disp2.append(p_11)
                                        else:
                                            p_9 = todas_las_letras[l + 4] + str(todos_los_numeros[n] - 1)
                                            p_10 = todas_las_letras[l + 4] + str(todos_los_numeros[n] + 1)
                                            p_11 = todas_las_letras[l + 4] + str(todos_los_numeros[n])
                                            p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_13 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            p_14 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            posiciones_no_disp2.append(p_9)
                                            posiciones_no_disp2.append(p_10)
                                            posiciones_no_disp2.append(p_11)
                                            posiciones_no_disp2.append(p_12)
                                            posiciones_no_disp2.append(p_13)
                                            posiciones_no_disp2.append(p_14)
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            continue
                    elif (c1 not in posiciones_vert):
                        print("Incorrecto! Vuelve a intentarlo")
                        continue

            elif (dir == "H"):
                for x in range(len(posiciones_hori)):
                    if (c1 == posiciones_hori[x]):
                        if ((c2 == posiciones_hori[x + 1] and c3 == posiciones_hori[x + 2] and c4 == posiciones_hori[x + 3])):
                            posiciones_user.append(c1)
                            posiciones_user.append(c2)
                            posiciones_user.append(c3)
                            posiciones_user.append(c4)
                            print("Posiciones asignadas correctamente!")
                            for l in range(len(todas_las_letras)):
                                for n in range(len(todos_los_numeros)):
                                    if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "A"):
                                        p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                        p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_3 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                        p_4 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 3)
                                        posiciones_no_disp2.append(p_1)
                                        posiciones_no_disp2.append(p_2)
                                        posiciones_no_disp2.append(p_3)
                                        posiciones_no_disp2.append(p_4)
                                        if (todos_los_numeros[n] == 0):
                                            p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 4)
                                            p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 4)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        elif (todos_los_numeros[n] == 6):
                                            p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        else:
                                            p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 4)
                                            p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 4)
                                            p_7 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            posiciones_no_disp2.append(p_7)
                                            posiciones_no_disp2.append(p_8)
                                    elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[
                                        l] == "J"):
                                        p_1 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                        p_2 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                        p_3 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                        p_4 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 3)
                                        posiciones_no_disp2.append(p_1)
                                        posiciones_no_disp2.append(p_2)
                                        posiciones_no_disp2.append(p_3)
                                        posiciones_no_disp2.append(p_4)
                                        if (todos_los_numeros[n] == 0):
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 4)
                                            p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 4)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        elif (todos_los_numeros[n] == 6):
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                        else:
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 4)
                                            p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 4)
                                            p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            posiciones_no_disp2.append(p_7)
                                            posiciones_no_disp2.append(p_8)
                                    elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] != "A" and todas_las_letras[l] != "J"):
                                        p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                        p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_3 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                        p_4 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 3)
                                        posiciones_no_disp2.append(p_1)
                                        posiciones_no_disp2.append(p_2)
                                        posiciones_no_disp2.append(p_3)
                                        posiciones_no_disp2.append(p_4)
                                        p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                        p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                        p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                        p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 3)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                        posiciones_no_disp2.append(p_7)
                                        posiciones_no_disp2.append(p_8)
                                        if (todos_los_numeros[n] == 0):
                                            p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 4)
                                            p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 4)
                                            p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 4)
                                            posiciones_no_disp2.append(p_9)
                                            posiciones_no_disp2.append(p_10)
                                            posiciones_no_disp2.append(p_11)
                                        elif (todos_los_numeros[n] == 6):
                                            p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_10 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                            p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_9)
                                            posiciones_no_disp2.append(p_10)
                                            posiciones_no_disp2.append(p_11)
                                        else:
                                            p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 4)
                                            p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 4)
                                            p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 4)
                                            p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                            p_13 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                            p_14 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_9)
                                            posiciones_no_disp2.append(p_10)
                                            posiciones_no_disp2.append(p_11)
                                            posiciones_no_disp2.append(p_12)
                                            posiciones_no_disp2.append(p_13)
                                            posiciones_no_disp2.append(p_14)
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            continue
                    elif (c1 not in posiciones_hori):
                        print("Incorrecto! Vuelve a intentarlo")
                        continue
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
            for x in range(len(posiciones_no_disp2)):
                for z in range(10):  # de 0 a 9
                    if (posiciones_no_disp2[x] == (todas_las_letras[0] + str(z))):
                        tablero[todas_las_letras[0]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[1] + str(z))):
                        tablero[todas_las_letras[1]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[2] + str(z))):
                        tablero[todas_las_letras[2]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[3] + str(z))):
                        tablero[todas_las_letras[3]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[4] + str(z))):
                        tablero[todas_las_letras[4]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[5] + str(z))):
                        tablero[todas_las_letras[5]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[6] + str(z))):
                        tablero[todas_las_letras[6]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[7] + str(z))):
                        tablero[todas_las_letras[7]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[8] + str(z))):
                        tablero[todas_las_letras[8]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[9] + str(z))):
                        tablero[todas_las_letras[9]][z] = "--"
            for lm in tablero:
                print(tablero[lm])

        while (len(posiciones_user) > 3 and len(posiciones_user) < 9):  # aqui haremos los dos barcos de 3 casillas
            print("Turno para crear los barcos de 3 casillas.")
            dir = input("Quieres crear el barco horizontal o vertical? (H,V):")
            c1 = input("Dime la 1/3 casilla que ocupara el barco:")
            c2 = input("Dime la 2/3 casilla que ocupara el barco:")
            c3 = input("Dime la 3/3 casilla que ocupara el barco:")
            if (dir == "V"):
                for e in range(len(posiciones_vert)):
                    if (c1 == posiciones_vert[e]):
                        if ((c2 == posiciones_vert[e + 1] and c3 == posiciones_vert[e + 2])):
                            if (c1 not in posiciones_user and c1 not in posiciones_no_disp2 and c2 not in posiciones_user and c2 not in posiciones_no_disp2 and c3 not in posiciones_user and c3 not in posiciones_no_disp2):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                posiciones_user.append(c3)
                                print("Posiciones asignadas correctamente!")
                                for l in range(len(todas_las_letras)):
                                    for n in range(len(todos_los_numeros)):
                                        if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[n] == 0):
                                            p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] + 1)
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            p_3 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_3)
                                            if (todas_las_letras[l] == "A"):
                                                p_5 = todas_las_letras[l + 3] + str(todos_los_numeros[n])
                                                p_6 = todas_las_letras[l + 3] + str(todos_los_numeros[n] + 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todas_las_letras[l] == "H"):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l + 3] + str(todos_los_numeros[n])
                                                p_6 = todas_las_letras[l + 3] + str(todos_los_numeros[n] + 1)
                                                p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[n] == 9):
                                            p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] - 1)  # g8
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)  # h8
                                            p_3 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)  # i8
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_3)
                                            if (todas_las_letras[l] == "A"):
                                                p_5 = todas_las_letras[l + 3] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l + 3] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todas_las_letras[l] == "H"):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l + 3] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l + 3] + str(todos_los_numeros[n])
                                                p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1):
                                            p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] - 1)
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            p_3 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                            p_5 = todas_las_letras[l + 0] + str(todos_los_numeros[n] + 1)
                                            p_6 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            p_7 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_3)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            posiciones_no_disp2.append(p_7)
                                            if (todas_las_letras[l] == "A"):
                                                p_9 = todas_las_letras[l + 3] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l + 3] + str(todos_los_numeros[n] + 1)
                                                p_11 = todas_las_letras[l + 3] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            elif (todas_las_letras[l] == "H"):
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                p_11 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            else:
                                                p_9 = todas_las_letras[l + 3] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l + 3] + str(todos_los_numeros[n] + 1)
                                                p_11 = todas_las_letras[l + 3] + str(todos_los_numeros[n])
                                                p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_13 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                p_14 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                                posiciones_no_disp2.append(p_12)
                                                posiciones_no_disp2.append(p_13)
                                                posiciones_no_disp2.append(p_14)
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                continue
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            continue
                    elif (c1 not in posiciones_vert):
                        print("Incorrecto! Vuelve a intentarlo")
                        continue

            elif (dir == "H"):
                for e in range(len(posiciones_hori)):
                    if (c1 == posiciones_hori[e]):
                        if ((c2 == posiciones_hori[e + 1] and c3 == posiciones_hori[e + 2])):
                            if (c1 not in posiciones_user and c1 not in posiciones_no_disp2 and c2 not in posiciones_user and c2 not in posiciones_no_disp2 and c3 not in posiciones_user and c3 not in posiciones_no_disp2):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                posiciones_user.append(c3)
                                print("Posiciones asignadas correctamente!")
                                for l in range(len(todas_las_letras)):
                                    for n in range(len(todos_los_numeros)):
                                        if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "A"):
                                            p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            p_3 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_3)
                                            if (todos_los_numeros[n] == 0):
                                                p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 3)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 3)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todos_los_numeros[n] == 7):
                                                p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 3)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 3)
                                                p_7 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "J"):
                                            p_1 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            p_2 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            p_3 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_3)
                                            if (todos_los_numeros[n] == 0):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 3)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 3)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todos_los_numeros[n] == 7):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 3)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 3)
                                                p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] != "A" and todas_las_letras[l] != "J"):
                                            p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            p_3 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_3)
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            posiciones_no_disp2.append(p_7)
                                            if (todos_los_numeros[n] == 0):
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 3)
                                                p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 3)
                                                p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 3)
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            elif (todos_los_numeros[n] == 7):
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            else:
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 3)
                                                p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 3)
                                                p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 3)
                                                p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_13 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                p_14 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                                posiciones_no_disp2.append(p_12)
                                                posiciones_no_disp2.append(p_13)
                                                posiciones_no_disp2.append(p_14)
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                continue
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            continue
                    elif (c1 not in posiciones_hori):
                        print("Incorrecto! Vuelve a intentarlo")
                        continue
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
            for x in range(len(posiciones_no_disp2)):
                for z in range(10):  # de 0 a 9
                    if (posiciones_no_disp2[x] == (todas_las_letras[0] + str(z))):
                        tablero[todas_las_letras[0]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[1] + str(z))):
                        tablero[todas_las_letras[1]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[2] + str(z))):
                        tablero[todas_las_letras[2]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[3] + str(z))):
                        tablero[todas_las_letras[3]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[4] + str(z))):
                        tablero[todas_las_letras[4]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[5] + str(z))):
                        tablero[todas_las_letras[5]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[6] + str(z))):
                        tablero[todas_las_letras[6]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[7] + str(z))):
                        tablero[todas_las_letras[7]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[8] + str(z))):
                        tablero[todas_las_letras[8]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[9] + str(z))):
                        tablero[todas_las_letras[9]][z] = "--"
            for lm in tablero:
                print(tablero[lm])

        while (len(posiciones_user) > 9 and len(posiciones_user) < 15):  # aqui haremos los tres barcos de 2 casillas
            print("Turno para crear los barcos de 2 casillas.")
            dir = input("Quieres crear el barco horizontal o vertical? (H,V):")
            c1 = input("Dime la 1/2 casilla que ocupara el barco:")
            c2 = input("Dime la 2/2 casilla que ocupara el barco:")
            if (dir == "V"):
                for e in range(len(posiciones_vert)):
                    if (c1 == posiciones_vert[e]):
                        if ((c2 == posiciones_vert[e + 1])):
                            if (c1 not in posiciones_user and c1 not in posiciones_no_disp2 and c2 not in posiciones_user and c2 not in posiciones_no_disp2):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                print("Posiciones asignadas correctamente!")
                                for l in range(len(todas_las_letras)):
                                    for n in range(len(todos_los_numeros)):
                                        if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[n] == 0):
                                            p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] + 1)
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            if (todas_las_letras[l] == "A"):
                                                p_5 = todas_las_letras[l + 2] + str(todos_los_numeros[n])
                                                p_6 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todas_las_letras[l] == "I"):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l + 2] + str(todos_los_numeros[n])
                                                p_6 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                                p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todos_los_numeros[n] == 9):
                                            p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] - 1)
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            if (todas_las_letras[l] == "A"):
                                                p_5 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l + 2] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todas_las_letras[l] == "I"):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l + 2] + str(todos_los_numeros[n])
                                                p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_8 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1):
                                            p_1 = todas_las_letras[l + 0] + str(todos_los_numeros[n] - 1)
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                            p_5 = todas_las_letras[l + 0] + str(todos_los_numeros[n] + 1)
                                            p_6 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            if (todas_las_letras[l] == "A"):
                                                p_9 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                                p_11 = todas_las_letras[l + 2] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            elif (todas_las_letras[l] == "I"):
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                p_11 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            else:
                                                p_9 = todas_las_letras[l + 2] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l + 2] + str(todos_los_numeros[n] + 1)
                                                p_11 = todas_las_letras[l + 2] + str(todos_los_numeros[n])
                                                p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_13 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                                p_14 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                                posiciones_no_disp2.append(p_12)
                                                posiciones_no_disp2.append(p_13)
                                                posiciones_no_disp2.append(p_14)
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                continue
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            continue
                    elif (c1 not in posiciones_vert):
                        print("Incorrecto! Vuelve a intentarlo")
                        continue

            elif (dir == "H" or dir == "h" or dir == "Horizontal" or dir == "horizontal" or dir == "Horizontalmente" or dir == "horizontalmente"):
                for e in range(len(posiciones_hori)):
                    if (c1 == posiciones_hori[e]):
                        if ((c2 == posiciones_hori[e + 1])):
                            if (c1 not in posiciones_user and c1 not in posiciones_no_disp2 and c2 not in posiciones_user and c2 not in posiciones_no_disp2):
                                posiciones_user.append(c1)
                                posiciones_user.append(c2)
                                print("Posiciones asignadas correctamente!")
                                for l in range(len(todas_las_letras)):
                                    for n in range(len(todos_los_numeros)):
                                        if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "A"):
                                            p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            if (todos_los_numeros[n] == 0):
                                                p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 2)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todos_los_numeros[n] == 8):
                                                p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 2)
                                                p_7 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "J"):
                                            p_1 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            p_2 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            if (todos_los_numeros[n] == 0):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 2)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            elif (todos_los_numeros[n] == 8):
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                            else:
                                                p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                                p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 2)
                                                p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_5)
                                                posiciones_no_disp2.append(p_6)
                                                posiciones_no_disp2.append(p_7)
                                                posiciones_no_disp2.append(p_8)
                                        elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] != "A" and todas_las_letras[l] != "J"):
                                            p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                            p_2 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_1)
                                            posiciones_no_disp2.append(p_2)
                                            p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                            p_6 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                            posiciones_no_disp2.append(p_5)
                                            posiciones_no_disp2.append(p_6)
                                            if (todos_los_numeros[n] == 0):
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                                p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 2)
                                                p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            elif (todos_los_numeros[n] == 8):
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_10 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                            else:
                                                p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 2)
                                                p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 2)
                                                p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 2)
                                                p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                                p_13 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                                p_14 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                                posiciones_no_disp2.append(p_9)
                                                posiciones_no_disp2.append(p_10)
                                                posiciones_no_disp2.append(p_11)
                                                posiciones_no_disp2.append(p_12)
                                                posiciones_no_disp2.append(p_13)
                                                posiciones_no_disp2.append(p_14)
                            else:
                                print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                                continue
                        else:
                            print("Incorrecto! Vuelve a intentarlo")
                            continue
                    elif (c1 not in posiciones_hori):
                        print("Incorrecto! Vuelve a intentarlo")
                        continue
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
            for x in range(len(posiciones_no_disp2)):
                for z in range(10):  # de 0 a 9
                    if (posiciones_no_disp2[x] == (todas_las_letras[0] + str(z))):
                        tablero[todas_las_letras[0]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[1] + str(z))):
                        tablero[todas_las_letras[1]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[2] + str(z))):
                        tablero[todas_las_letras[2]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[3] + str(z))):
                        tablero[todas_las_letras[3]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[4] + str(z))):
                        tablero[todas_las_letras[4]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[5] + str(z))):
                        tablero[todas_las_letras[5]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[6] + str(z))):
                        tablero[todas_las_letras[6]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[7] + str(z))):
                        tablero[todas_las_letras[7]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[8] + str(z))):
                        tablero[todas_las_letras[8]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[9] + str(z))):
                        tablero[todas_las_letras[9]][z] = "--"
            for lm in tablero:
                print(tablero[lm])

        while (len(posiciones_user) > 15 and len(posiciones_user) < 20):  # aqui haremos los cuatro barcos de 1 casilla
            print("Turno para crear los barcos de 1 casilla.")
            c1 = input("Dime la 1/1 casilla que ocupara el barco:")
            for e in range(len(posiciones_hori)):
                if (c1 == posiciones_hori[e]):
                    if (c1 not in posiciones_user and c1 not in posiciones_no_disp2):
                        posiciones_user.append(c1)
                        print("Posiciones asignadas correctamente!")
                        for l in range(len(todas_las_letras)):
                            for n in range(len(todos_los_numeros)):
                                if (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "A"):
                                    p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                    posiciones_no_disp2.append(p_1)
                                    if (todos_los_numeros[n] == 0):
                                        p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 1)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                    elif (todos_los_numeros[n] == 9):
                                        p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                        p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                    else:
                                        p_5 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 1)
                                        p_7 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                        p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                        posiciones_no_disp2.append(p_7)
                                        posiciones_no_disp2.append(p_8)
                                elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] == "J"):
                                    p_1 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                    posiciones_no_disp2.append(p_1)
                                    if (todos_los_numeros[n] == 0):
                                        p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                        p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 1)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                    elif (todos_los_numeros[n] == 8):
                                        p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                        p_6 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                    else:
                                        p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                        p_6 = todas_las_letras[l] + str(todos_los_numeros[n] + 1)
                                        p_7 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                        p_8 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_5)
                                        posiciones_no_disp2.append(p_6)
                                        posiciones_no_disp2.append(p_7)
                                        posiciones_no_disp2.append(p_8)
                                elif (todas_las_letras[l] + str(todos_los_numeros[n]) == c1 and todas_las_letras[l] != "A" and todas_las_letras[l] != "J"):
                                    p_1 = todas_las_letras[l + 1] + str(todos_los_numeros[n])
                                    posiciones_no_disp2.append(p_1)
                                    p_5 = todas_las_letras[l - 1] + str(todos_los_numeros[n])
                                    posiciones_no_disp2.append(p_5)
                                    if (todos_los_numeros[n] == 0):
                                        p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                        p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 1)
                                        p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        posiciones_no_disp2.append(p_9)
                                        posiciones_no_disp2.append(p_10)
                                        posiciones_no_disp2.append(p_11)
                                    elif (todos_los_numeros[n] == 9):
                                        p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                        p_10 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                        p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_9)
                                        posiciones_no_disp2.append(p_10)
                                        posiciones_no_disp2.append(p_11)
                                    else:
                                        p_9 = todas_las_letras[l - 1] + str(todos_los_numeros[n] + 1)
                                        p_10 = todas_las_letras[l] + str(todos_los_numeros[n] + 1)
                                        p_11 = todas_las_letras[l + 1] + str(todos_los_numeros[n] + 1)
                                        p_12 = todas_las_letras[l - 1] + str(todos_los_numeros[n] - 1)
                                        p_13 = todas_las_letras[l] + str(todos_los_numeros[n] - 1)
                                        p_14 = todas_las_letras[l + 1] + str(todos_los_numeros[n] - 1)
                                        posiciones_no_disp2.append(p_9)
                                        posiciones_no_disp2.append(p_10)
                                        posiciones_no_disp2.append(p_11)
                                        posiciones_no_disp2.append(p_12)
                                        posiciones_no_disp2.append(p_13)
                                        posiciones_no_disp2.append(p_14)
                    else:
                        print("Incorrecto! Posiciones ya asignadas a otro barco! Intentalo de nuevo")
                        continue
                elif (c1 not in posiciones_hori):
                    print("Incorrecto! Vuelve a intentarlo")
                    continue
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
            for x in range(len(posiciones_no_disp2)):
                for z in range(10):  # de 0 a 9
                    if (posiciones_no_disp2[x] == (todas_las_letras[0] + str(z))):
                        tablero[todas_las_letras[0]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[1] + str(z))):
                        tablero[todas_las_letras[1]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[2] + str(z))):
                        tablero[todas_las_letras[2]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[3] + str(z))):
                        tablero[todas_las_letras[3]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[4] + str(z))):
                        tablero[todas_las_letras[4]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[5] + str(z))):
                        tablero[todas_las_letras[5]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[6] + str(z))):
                        tablero[todas_las_letras[6]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[7] + str(z))):
                        tablero[todas_las_letras[7]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[8] + str(z))):
                        tablero[todas_las_letras[8]][z] = "--"
                    elif (posiciones_no_disp2[x] == (todas_las_letras[9] + str(z))):
                        tablero[todas_las_letras[9]][z] = "--"
            for lm in tablero:
                print(tablero[lm])
    time.sleep(2)
    print("Tu tablero se ha generado correctamente.")
    time.sleep(3)
    return tablero

def Hundir_la_flota_turno_pc(tablero_del_pc_para_user,posiciones_vert,posiciones,posiciones_dichas,):
    for a in range(1):
        print("Es tu turno para escoger una casilla!")
        time.sleep(2)
        print("Tu tablero para atacar:")
        time.sleep(2)
        for mi in tablero_del_pc_para_user:
            print(tablero_del_pc_para_user[mi])
        time.sleep(2)
        c = input("Dime la coordenada a la que deseas lanzar un misil:")
        if (c not in posiciones_vert):
            print("ERROR! La coordenada insertada no existe")
            time.sleep(2)
            print("Vuelve a intentarlo!")
            Hundir_la_flota_turno_pc(tablero_del_pc_para_user,posiciones_vert,posiciones,posiciones_dichas,)
        elif (c in posiciones_vert):
            if (c in posiciones_dichas):
                print("ERROR! La coordenada insertada ya fue escogida!")
                time.sleep(2)
                print("Vuelve a intentarlo!")
                Hundir_la_flota_turno_pc(tablero_del_pc_para_user, posiciones_vert,posiciones,posiciones_dichas)
            elif (c not in posiciones_dichas):
                print("Lanzando misil a:",c)
                for x in range(3, 0, -1):
                    time.sleep(1)
                    print(x)
                print("Misil lanzado correctamente!")
                time.sleep(2)
                for x in tablero_del_pc_para_user:
                    for z in range(len(tablero_del_pc_para_user[x])):
                        if (c in posiciones and tablero_del_pc_para_user[x][z] == c):
                            tablero_del_pc_para_user[x][z] = "XX"
                            posiciones_dichas.append(c)
                            total = 0
                            pos = posiciones.index(c)
                            if (pos <= 3):
                                if (posiciones[0] in posiciones_dichas and posiciones[1] in posiciones_dichas and posiciones[2] in posiciones_dichas and posiciones[3] in posiciones_dichas):
                                    print("Hundido!")
                                else:
                                    print("Tocado!")
                            elif (pos <= 6):
                                if (posiciones[4] in posiciones_dichas and posiciones[5] in posiciones_dichas and posiciones[6] in posiciones_dichas):
                                    print("Hundido!")
                                else:
                                    print("Tocado!")
                            elif (pos <= 9):
                                if (posiciones[7] in posiciones_dichas and posiciones[8] in posiciones_dichas and posiciones[9] in posiciones_dichas):
                                    print("Hundido!")
                                else:
                                    print("Tocado!")
                            elif (pos <= 11):
                                if (posiciones[10] in posiciones_dichas and posiciones[11] in posiciones_dichas):
                                    print("Hundido!")
                                else:
                                    print("Tocado!")
                            elif (pos <= 13):
                                if (posiciones[12] in posiciones_dichas and posiciones[13] in posiciones_dichas):
                                    print("Hundido!")
                                else:
                                    print("Tocado!")
                            elif (pos <= 15):
                                if (posiciones[14] in posiciones_dichas and posiciones[15] in posiciones_dichas):
                                    print("Hundido!")
                                else:
                                    print("Tocado!")
                            elif (pos <= 16):
                                if (posiciones[16] in posiciones_dichas):
                                    print("Hundido!")
                            elif (pos <= 17):
                                if (posiciones[17] in posiciones_dichas):
                                    print("Hundido!")
                            elif (pos <= 18):
                                if (posiciones[18] in posiciones_dichas):
                                    print("Hundido!")
                            elif (pos <= 19):
                                if (posiciones[19] in posiciones_dichas):
                                    print("Hundido!")
                            for w in range(len(posiciones_dichas)):
                                if (posiciones_dichas[w] in posiciones):
                                    total = total + 1
                                if (total == len(posiciones)):  # en caso de que todas las posiciones que las posiciones introducidas por el usuario esten en la lista de las posiciones donde hay barcos, gana la partida.
                                    ganador = "Usuario"
                                    Partida_terminada(ganador,tablero_del_pc_para_user)
                                    print("Has ganado!")
                                    time.sleep(1)
                                    print("Felicidades!")
                                    time.sleep(1)
                                    for q in tablero_del_pc_para_user:
                                        print(tablero_del_pc_para_user[q])
                                    time.sleep(1)
                                    print("Este es el tablero final!")

                        elif (c not in posiciones):
                            if (tablero_del_pc_para_user[x][z] == c):
                                print("Agua")
                                time.sleep(2)
                                tablero_del_pc_para_user[x][z] = "~~"
                                posiciones_dichas.append(c)


def Hundir_la_flota_turno_user(tablero_del_user_para_pc,posiciones_vert,posiciones_dichas_2,posiciones_user):
    for t in range(1):
        print("Es el turno de PC para escoger una casilla!")
        casilla = random.choice(posiciones_vert)
        if (casilla in posiciones_dichas_2):
            Hundir_la_flota_turno_user(tablero_del_user_para_pc,posiciones_vert,posiciones_dichas_2,posiciones_user)
        elif (casilla not in posiciones_dichas_2):
            time.sleep(2)
            for p in tablero_del_user_para_pc:
                print(tablero_del_user_para_pc[p])
            time.sleep(2)
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
                    if (casilla in posiciones_user and tablero_del_user_para_pc[b][n] == casilla):
                        tablero_del_user_para_pc[b][n] = "XX"
                        posiciones_dichas_2.append(casilla)
                        tota = 0
                        pos = posiciones_user.index(casilla)
                        if (pos <= 3):
                            if (posiciones_user[0] in posiciones_dichas_2 and posiciones_user[1] in posiciones_dichas_2 and posiciones_user[2] in posiciones_dichas_2 and posiciones_user[3] in posiciones_dichas_2):
                                print("Hundido!")
                            else:
                                print("Tocado!")
                        elif (pos <= 6):
                            if (posiciones_user[4] in posiciones_dichas_2 and posiciones_user[5] in posiciones_dichas_2 and posiciones_user[6] in posiciones_dichas_2):
                                print("Hundido!")
                            else:
                                print("Tocado!")
                        elif (pos <= 9):
                            if (posiciones_user[7] in posiciones_dichas_2 and posiciones_user[8] in posiciones_dichas_2 and posiciones_user[9] in posiciones_dichas_2):
                                print("Hundido!")
                            else:
                                print("Tocado!")
                        elif (pos <= 11):
                            if (posiciones_user[10] in posiciones_dichas_2 and posiciones_user[11] in posiciones_dichas_2):
                                print("Hundido!")
                            else:
                                print("Tocado!")
                        elif (pos <= 13):
                            if (posiciones_user[12] in posiciones_dichas_2 and posiciones_user[13] in posiciones_dichas_2):
                                print("Hundido!")
                            else:
                                print("Tocado!")
                        elif (pos <= 15):
                            if (posiciones_user[14] in posiciones_dichas_2 and posiciones_user[15] in posiciones_dichas_2):
                                print("Hundido!")
                            else:
                                print("Tocado!")
                        elif (pos <= 16):
                            if (posiciones_user[16] in posiciones_dichas_2):
                                print("Hundido!")
                        elif (pos <= 17):
                            if (posiciones_user[17] in posiciones_dichas_2):
                                print("Hundido!")
                        elif (pos <= 18):
                            if (posiciones_user[18] in posiciones_dichas_2):
                                print("Hundido!")
                        elif (pos <= 19):
                            if (posiciones_user[19] in posiciones_dichas_2):
                                print("Hundido!")
                        for w in range(len(posiciones_dichas_2)):
                            if (posiciones_dichas_2[w] in posiciones_user):
                                tota = tota + 1
                            if (tota == len(posiciones_user)):  # en caso de que todas las posiciones que las posiciones introducidas por el usuario esten en la lista de las posiciones donde hay barcos, gana la partida.
                                ganador = "PC"
                                Partida_terminada(ganador,tablero_del_user_para_pc)
                    elif (casilla not in posiciones_user):
                        if (tablero_del_user_para_pc[b][n] == casilla):
                            print("Agua")
                            time.sleep(2)
                            tablero_del_user_para_pc[b][n] = "~~"
                            posiciones_dichas_2.append(casilla)

def Partida_terminada(ganador,tabl):
    if (ganador == "PC"):
        time.sleep(2)
        print("Se acabó la partida!")
        time.sleep(2)
        print("PC ha destruido tu Flota!")
        time.sleep(2)
        print("Este era el tablero de",ganador)
        for q in tabl:
            print(tabl[q])
    else:
        time.sleep(2)
        print("Se acabó la partida!")
        time.sleep(3)
        print("Felicidades! Has destruido la Flota de PC")

    time.sleep(4)
    print("Volviendo al menu principal.")
    time.sleep(3)
    from MAIN_aka_Menu_principal import menu
    menu()

