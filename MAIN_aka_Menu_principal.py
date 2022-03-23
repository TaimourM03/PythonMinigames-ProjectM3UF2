from Hundir_la_flota import Hundir_la_flota
from Conecta4 import Conecta_4
from Oca import Oca
def menu():
    juegos = ["1: Hundir la flota","2: Oca","3: Conecta 4"]
    for x in range(len(juegos)):
        print(juegos[x])
    opcion = int(input("Escoge un juego:"))
    if (opcion == 1):
        Hundir_la_flota()
    elif (opcion == 2):
        Oca()
    elif (opcion == 3):
        Conecta_4()
    else:
        print("Error! Vuelve a intentarlo")
        menu()

menu()
