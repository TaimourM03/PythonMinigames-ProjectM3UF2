def menu():
    juegos = ["1: Hundir la flota","2: Oca","3: Conecta 4","4: Apagar"]
    for x in range(len(juegos)):
        print(juegos[x])
    opcion = int(input("Escoge un juego:"))
    if (opcion == 1):
        Hundir_la_flota()
    elif (opcion == 2):
        Oca()
    elif (opcion == 3):
        Conecta_4()
    elif (opcion == 4):
        print("Apagando...")
    else:
        print("Error! Vuelve a intentarlo")
        menu()

menu()
