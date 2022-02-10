

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
        # 10:[" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "," 10"]
    }
    def imprimir_separador_horizontal():
    # Imprimir un renglón dependiendo de las columnas
    for _ in range(COLUMNAS+1):
        print("+---", end="")
    print("+")
    
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
    letras_posibles = [A,B,C,D,E,F,G]
    posiciones = []
    for x in range(10):
        barco = opciones_finales.append(random.randint(1,2))
        for x in range(1): #barco de 4 casillas (solo hay uno)
        if (barco == 1):
            pri_num= random.choice(numeros_posibles)
            pri_letra = random.choice(letras_posibles)
            if (pri_letra == "A"):#FALTA ADIVINAR EL NUMERO QUE HAY EN LA POSICION
                if(pri_num == 1):#LA POSICION ES A1
                    posiciones.append("A1")
                elif(pri_num == 2):#LA POSICION ES A2
                    posiciones.append("A2")
                elif(pri_num == 3):#LA POSICION ES A3
                    posiciones.append("A3")
                elif(pri_num == 4):#LA POSICION ES A4
                    posiciones.append("A4")
                elif(pri_num == 5):#LA POSICION ES A5
                    posiciones.append("A5")
                elif(pri_num == 6):#LA POSICION ES A6
                    posiciones.append("A6")
                elif(pri_num == 7):#LA POSICION ES A7
                    posiciones.append("A7")
                    
            elif (pri_letra == "B"):
                if(pri_num == 1):#LA POSICION ES B1
                    posiciones.append("B1")
                elif(pri_num == 2):#LA POSICION ES B2
                    posiciones.append("B2")
                elif(pri_num == 3):#LA POSICION ES B3
                    posiciones.append("B3")
                elif(pri_num == 4):#LA POSICION ES B4
                    posiciones.append("B4")
                elif(pri_num == 5):#LA POSICION ES B5
                    posiciones.append("B5")
                elif(pri_num == 6):#LA POSICION ES B6
                    posiciones.append("B6")
                elif(pri_num == 7):#LA POSICION ES B7
                    posiciones.append("B7")
                    
            elif (pri_letra == "C"):
                if(pri_num == 1):#LA POSICION ES C1
                    posiciones.append("C1")
                elif(pri_num == 2):#LA POSICION ES C2
                    posiciones.append("C2")
                elif(pri_num == 3):#LA POSICION ES C3
                    posiciones.append("C3")
                elif(pri_num == 4):#LA POSICION ES C4
                    posiciones.append("C4")
                elif(pri_num == 5):#LA POSICION ES C5
                    posiciones.append("C5")
                elif(pri_num == 6):#LA POSICION ES C6
                    posiciones.append("C6")
                elif(pri_num == 7):#LA POSICION ES C7
                    posiciones.append("C7")
                
            elif (pri_letra == "D"):
                if(pri_num == 1):#LA POSICION ES D1
                    posiciones.append("D1")
                elif(pri_num == 2):#LA POSICION ES D2
                    posiciones.append("D2")
                elif(pri_num == 3):#LA POSICION ES D3
                    posiciones.append("D3")
                elif(pri_num == 4):#LA POSICION ES D4
                    posiciones.append("D4")
                elif(pri_num == 5):#LA POSICION ES D5
                    posiciones.append("D5")
                elif(pri_num == 6):#LA POSICION ES D6
                    posiciones.append("D6")
                elif(pri_num == 7):#LA POSICION ES D7
                    posiciones.append("D7")
            
            elif (pri_letra == "E"):
                if(pri_num == 1):#LA POSICION ES E1
                    posiciones.append("E1")
                elif(pri_num == 2):#LA POSICION ES E2
                    posiciones.append("E2")
                elif(pri_num == 3):#LA POSICION ES E3
                    posiciones.append("E3")
                elif(pri_num == 4):#LA POSICION ES E4
                    posiciones.append("E4")
                elif(pri_num == 5):#LA POSICION ES E5
                    posiciones.append("E5")
                elif(pri_num == 6):#LA POSICION ES E6
                    posiciones.append("E6")
                elif(pri_num == 7):#LA POSICION ES E7
                    posiciones.append("E7")
                    
            elif (pri_letra == "F"):
                if(pri_num == 1):#LA POSICION ES F1
                    posiciones.append("F1")
                elif(pri_num == 2):#LA POSICION ES F2
                    posiciones.append("F2")
                elif(pri_num == 3):#LA POSICION ES F3
                    posiciones.append("F3")
                elif(pri_num == 4):#LA POSICION ES F4
                    posiciones.append("F4")
                elif(pri_num == 5):#LA POSICION ES F5
                    posiciones.append("F5")
                elif(pri_num == 6):#LA POSICION ES F6
                    posiciones.append("F6")
                elif(pri_num == 7):#LA POSICION ES F7
                    posiciones.append("F7")
            
            elif (pri_letra == "G"):
                if(pri_num == 1):#LA POSICION ES G1
                    posiciones.append("G1")
                elif(pri_num == 2):#LA POSICION ES G2
                    posiciones.append("G2")
                elif(pri_num == 3):#LA POSICION ES G3
                    posiciones.append("G3")
                elif(pri_num == 4):#LA POSICION ES G4
                    posiciones.append("G4")
                elif(pri_num == 5):#LA POSICION ES G5
                    posiciones.append("G5")
                elif(pri_num == 6):#LA POSICION ES G6
                    posiciones.append("G6")
                elif(pri_num == 7):#LA POSICION ES G7
                    posiciones.append("G7")
            
            elif (pri_letra == "H"):
                if(pri_num == 1):#LA POSICION ES H1
                    posiciones.append("H1")
                elif(pri_num == 2):#LA POSICION ES H2
                    posiciones.append("H2")
                elif(pri_num == 3):#LA POSICION ES H3
                    posiciones.append("H3")
                elif(pri_num == 4):#LA POSICION ES H4
                    posiciones.append("H4")
                elif(pri_num == 5):#LA POSICION ES H5
                    posiciones.append("H5")
                elif(pri_num == 6):#LA POSICION ES H6
                    posiciones.append("H6")
                elif(pri_num == 7):#LA POSICION ES H7
                    posiciones.append("H7")
            
            elif (pri_letra == "I"):
                if(pri_num == 1):#LA POSICION ES I1
                    posiciones.append("I1")
                elif(pri_num == 2):#LA POSICION ES I2
                    posiciones.append("I2")
                elif(pri_num == 3):#LA POSICION ES I3
                    posiciones.append("I3")
                elif(pri_num == 4):#LA POSICION ES I4
                    posiciones.append("I4")
                elif(pri_num == 5):#LA POSICION ES I5
                    posiciones.append("I5")
                elif(pri_num == 6):#LA POSICION ES I6
                    posiciones.append("I6")
                elif(pri_num == 7):#LA POSICION ES I7
                    posiciones.append("I7")
            
            elif (pri_letra == "J"):
                if(pri_num == 1):#LA POSICION ES J1
                    posiciones.append("J1")
                elif(pri_num == 2):#LA POSICION ES J2
                    posiciones.append("J2")
                elif(pri_num == 3):#LA POSICION ES J3
                    posiciones.append("J3")
                elif(pri_num == 4):#LA POSICION ES J4
                    posiciones.append("J4")
                elif(pri_num == 5):#LA POSICION ES J5
                    posiciones.append("J5")
                elif(pri_num == 6):#LA POSICION ES J6
                    posiciones.append("J6")
                elif(pri_num == 7):#LA POSICION ES J7
                    posiciones.append("J7")
    
def Oca():
    import random
ju=int(input("Cuantos jugadores hay:"))
for i in range(ju):
    x=input("Tirar dado SI/NO:")
    if x=="si":
        d1= random.randint(1,6)
        d2=random.randint(1,6)
        print ("El primer dado salio:",d1,"El segundo dado salio:",d2)
        t= d1+d2
        print("La suma de los dados es:",t)
    elif x=="no":
        print("Has decidido no tirar")
    else: 
        x=input("Tirar dado SI/NO:")
def Escaleras_y_Serpientes():
    pass
def Quien_es_quien():
    pass
def Conecta_4():
    NUMERO_FILAS = 6
NUMERO_COLUMNAS = 7
def crear_tablero():
tablero =
    pass

menu()



