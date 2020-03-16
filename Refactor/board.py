from importlib import import_module

from Refactor import pieza

import_module(pieza)

tablero = []

for y in range(0, 11):
    tablero.append([00] * 11)

# coordenadas
tablero[0][0] = 0
tablero[0][1] = 1
tablero[0][2] = 2
tablero[0][3] = 3
tablero[0][4] = 4
tablero[0][5] = 5
tablero[0][6] = 6
tablero[0][7] = 7
tablero[0][8] = 8
tablero[0][9] = 9

tablero[1][0] = 1
tablero[2][0] = 2
tablero[3][0] = 3
tablero[4][0] = 4
tablero[5][0] = 5
tablero[6][0] = 6
tablero[7][0] = 7
tablero[8][0] = 8
tablero[9][0] = 9

tablero[0][10] = 10
tablero[1][10] = 10
tablero[2][10] = 10
tablero[3][10] = 10
tablero[4][10] = 10
tablero[5][10] = 10
tablero[6][10] = 10
tablero[7][10] = 10
tablero[8][10] = 10
tablero[9][10] = 10
tablero[10][10] = 10

tablero[10][0] = 10
tablero[10][1] = 10
tablero[10][2] = 10
tablero[10][3] = 10
tablero[10][4] = 10
tablero[10][5] = 10
tablero[10][6] = 10
tablero[10][7] = 10
tablero[10][8] = 10
tablero[10][9] = 10

# Piezas jugador 1
tablero[1][1] = Lider1 = pieza.Lider("Lider", 8, "vivo", "true", "true", 1)
tablero[1][2] = Asesino1 = pieza.Asesino("Asesino", 8, "vivo", "false", "true", 1)
tablero[1][3] = Militante11 = pieza.Militante("Militante", 2, "vivo", "false", "true", 1)
tablero[2][1] = Reportero1 = pieza.Reportero("Militante", 2, "vivo", "false", "true", 1)
tablero[2][2] = Provocador1 = pieza.Provocador("Provocador", 8, "vivo", "false", "false", 1)
tablero[2][3] = Militante12 = pieza.Militante("Militante", 2, "vivo", "false", "true", 1)
tablero[3][1] = Militante13 = pieza.Militante("Militante", 2, "vivo", "false", "true", 1)
tablero[3][2] = Militante14 = pieza.Militante("Militante", 2, "vivo", "false", "true", 1)
tablero[3][3] = Necro1 = pieza.Necromovil("Necromovil", 8, "vivo", "false", "false", 1)

# Piezas jugador 2
tablero[1][7] = Militante21 = pieza.Militante("Militante", 2, "vivo", "false", "true", 2)
tablero[1][8] = Asesino2 = pieza.Asesino("Asesino", 8, "vivo", "false", "true", 2)
tablero[1][9] = Lider2 = pieza.Lider("Lider", 8, "vivo", "true", "true", 2)
tablero[2][7] = Militante22 = pieza.Militante("Militante", 2, "vivo", "false", "true", 2)
tablero[2][8] = Provocador2 = pieza.Provocador("Provocador", 8, "vivo", "false", "false", 2)
tablero[2][9] = Reportero2 = pieza.Reportero("Militante", 2, "vivo", "false", "true", 2)
tablero[3][7] = Necro2 = pieza.Necromovil("Necromovil", 8, "vivo", "false", "false", 2)
tablero[3][8] = Militante23 = pieza.Militante("Militante", 2, "vivo", "false", "true", 2)
tablero[3][9] = Militante24 = pieza.Militante("Militante", 2, "vivo", "false", "true", 2)

# Piezas jugador 3
tablero[7][1] = 131
tablero[7][2] = 131
tablero[7][3] = 231
tablero[8][1] = 331
tablero[8][2] = 431
tablero[8][3] = 131
tablero[9][1] = 531
tablero[9][2] = 631
tablero[9][3] = 131

# Piezas jugador 4
tablero[7][7] = 241
tablero[7][8] = 141
tablero[7][9] = 141
tablero[8][7] = 141
tablero[8][8] = 441
tablero[8][9] = 341
tablero[9][7] = 141
tablero[9][8] = 641
tablero[9][9] = 541
