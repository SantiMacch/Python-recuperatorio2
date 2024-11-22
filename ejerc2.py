palabras = ["manzana", "banana", "pera", "manzana", "naranja", "pera", "pera"]

def cantocurrencias(palabras):
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    print(contador) 
    
cantocurrencias(palabras)

