

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

def Barcos_del_pc(opciones_finales,numeros_posibles,letras_posibles,todas_las_letras,posiciones):
    print("Le toca al PC asignarse las posiciones de los barcos.")
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
    return posiciones







def Barcos_del_user(posiciones_user,posiciones_vert,posiciones_hori):
    while(len(posiciones_user) < 20):
        print("Te toca elegir donde quieres poner los barcos.")
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
    return posiciones_user







def Hundir_la_flota():
    #web normar del juego: https://familiaycole.files.wordpress.com/2012/09/instrucciones-del-juego-de-los-barcos.pdf
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
    opciones_finales = []  # 2 sera vertical, 1 horizontal, posibilidades primera casilla: (1-7) o (A-G)
    numeros_posibles = [1,2,3,4,5,6,7]
    letras_posibles = ["A","B","C","D","E","F","G"]
    todas_las_letras = ["A","B","C","D","E","F","G","H","I","J"]
    posiciones = []
    pos_barcos = Barcos_del_pc(opciones_finales,numeros_posibles,letras_posibles,todas_las_letras,posiciones)
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
    for x in tablero:
        print(tablero[x])
    pos_del_user = Barcos_del_user(posiciones_user,posiciones_vert,posiciones_hori)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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




