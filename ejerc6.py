matriz = [[6, 4, 2, 5],
          [8, 2, 6, 9],
          [4, 2, 8, 1],
          [2, 6, 4, 7]]

def suma_diagonales(matriz):
    diagonalprincipal = 0
    diagonalsecundaria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            