

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
    0:[" J1 "," J2 "," J3 "," J4 "," J5 "," J6 "," J7 "," J8 "," J9 "," J10 "],
    1:[" I1 "," I2 "," I3 "," I4 "," I5 "," I6 "," I7 "," I8 "," I9 "," I10 "],
    2:[" H1 "," H2 "," H3 "," H4 "," H5 "," H6 "," H7 "," H8 "," H9 "," H10 "],
    3:[" G1 "," G2 "," G3 "," G4 "," G5 "," G6 "," G7 "," G8 "," G9 "," G10 "],
    4:[" F1 "," F2 "," F3 "," F4 "," F5 "," F6 "," F7 "," F8 "," F9 "," F10 "],
    5:[" E1 "," E2 "," E3 "," E4 "," E5 "," E6 "," E7 "," E8 "," E9 "," E10 "],
    6:[" D1 "," D2 "," D3 "," D4 "," D5 "," D6 "," D7 "," D8 "," D9 "," D10 "],
    7:[" C1 "," C2 "," C3 "," C4 "," C5 "," C6 "," C7 "," C8 "," C9 "," C10 "],
    8:[" B1 "," B2 "," B3 "," B4 "," B5 "," B6 "," B7 "," B8 "," B9 "," B10 "],
    9:[" A1 "," A2 "," A3 "," A4 "," A5 "," A6 "," A7 "," A8 "," A9 "," A10 "],
    #10:[" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "," 10"]
    }

    for x in range(len(tablero)):
        print(tablero[x])
def Oca():
    pass
def Escaleras_y_Serpientes():
    pass
def Quien_es_quien():
    pass
def Conecta_4():
    pass

menu()


"""import random
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
        x=input("Tirar dado SI/NO:")"""
