def mostrar(tablero):
    for x in tablero:
        for y in tablero[x]:
            print(y, end="")
        print()
    print()