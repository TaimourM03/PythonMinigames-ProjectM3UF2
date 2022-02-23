import random,time
def Oca():
    tablero = {
        8: ["25", "24", "23", "22", "21", "20", "19", "18", "17", "16"],
        7: ["26", "51", "50", "49", "48", "47", "46", "45", "44", "15"],
        6: ["27", "52", "  ", "  ", "  ", "  ", "  ", "  ", "43", "14"],
        5: ["28", "53", "  ", "  ", "  ", "  ", "  ", "  ", "42", "13"],
        4: ["29", "54", "  ", "  ", "  ", "  ", "  ", "62", "41", "12"],
        3: ["30", "55", "56", "57", "58", "59", "60", "61", "40", "11"],
        2: ["31", "32", "33", "34", "35", "36", "37", "38", "39", "10"],
        1: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    }
    JU = 0
    PC = 0
    while JU!="" or PC!="":
        x=input("Tirar dado SI/NO:")
        tablero = {
            8: ["25", "24", "23", "22", "21", "20", "19", "18", "17", "16"],
            7: ["26", "51", "50", "49", "48", "47", "46", "45", "44", "15"],
            6: ["27", "52", "  ", "  ", "  ", "  ", "  ", "  ", "43", "14"],
            5: ["28", "53", "  ", "  ", "  ", "  ", "  ", "  ", "42", "13"],
            4: ["29", "54", "  ", "  ", "  ", "  ", "  ", "62", "41", "12"],
            3: ["30", "55", "56", "57", "58", "59", "60", "61", "40", "11"],
            2: ["31", "32", "33", "34", "35", "36", "37", "38", "39", "10"],
            1: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
        }
        if x=="si":
            d1= random.randint(1,6)
            d2=random.randint(1,6)
            t = d1+d2
            JU = JU +t
            time.sleep(1)
            print("El primer dado salio:",d1,",El segundo dado salio:",d2,",La suma de los dados es:",t,",Haz avanzado a la casilla :",JU)
            dp1 = random.randint(1, 6)
            dp2 = random.randint(1, 6)
            to = dp1 + dp2
            PC = PC + to
            time.sleep(1)
            print("El primer dado salio:", dp1, ",El segundo dado salio:", dp2,",La suma de los dados del PC es:", to,",El PC ha avanzado al puesto:",PC)
        elif x=="no":
            print("Has decidido no tirar")
        else:
            x=input("Tirar dado SI/NO:")

        for y in tablero:
            for z in range(len(tablero[y])):
                if (JU == PC and JU != 0):  # JU DISTINTO DE CERO, PORQUE EN LA PRIMERA JUGADA AMBOS ESTARAN IGUAL EN 0!!!
                    if (JU < 10 and tablero[1][z] == "0" + str(JU)):
                        tablero[1][z] = "J|P"
                    elif (tablero[y][z] == str(JU)):
                        tablero[y][z] = "J|P"

                if (JU < 10 and tablero[1][z]=="0"+str(JU)):
                    tablero[1][z] = "JU"
                elif tablero[y][z] == str(JU):
                        tablero[y][z] = "JU"

                if (PC < 10 and tablero[1][z]=="0"+str(PC)):
                    tablero[1][z]="PC"
                elif tablero[y][z] == str(PC):
                    tablero[y][z] = "PC"

            time.sleep(0.1)
            print(tablero[y])

Oca()