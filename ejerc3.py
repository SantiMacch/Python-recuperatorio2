palabras = ["manzana", "banana", "pera", "manzana", "naranja", "pera", "pera"]

def cantocurrencias(palabras):
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

archivo = open("conteo_palabras.txt", "w")

for palabra, conteo in cantocurrencias(palabras):
    archivo.write(f'{palabra}: {conteo} ')

print("el archivo se creo correctamente")
