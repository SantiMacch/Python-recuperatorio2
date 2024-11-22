matriz = [[6, 4, 2],
          [8, 2, 6],
          [4, 2, 8]]


def suma_filas(matriz):
   for i in range(len(matriz)) :
       suma = 0
       for elemento in i:
           suma += elemento
           print(suma)
       

def suma_columnas(matriz):
    for j in range(len(matriz)) :
        suma = 0
        for elemento in j:
            suma += elemento
            print(suma)
        

def transpuesta(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = matriz[j][i]
            print(matriz)


print(suma_filas(matriz))
print(suma_columnas(matriz))
print(transpuesta(matriz))
