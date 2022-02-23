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
    pass

def Oca():
    pass

def Escaleras_y_Serpientes():
    pass

def Quien_es_quien():
    pass

def Conecta_4():
    pass

menu()