
def entrada():
    largo_palabra, letras_lista, posiciones_lista = 0, [], []
    
    while True:
        largo_palabra = input("Introduzca el n° de caracteres de su palabra: ")
        if largo_palabra.isdigit() and int(largo_palabra) > 0 :
            break
    while True:
        letras = input("Introduzca las letras que ya conoce (todas seguidas): ")
        if isinstance(letras, str):
            break
    while True:
        posiciones = input("Introdzuca las posiciones respectivas de cada letra (todas seguidas): ")
        if posiciones.isdigit():
            break
    
    for letra in letras:
        letras_lista.append(letra)
    for posicion in posiciones:
        posiciones_lista.append(posicion)

    return largo_palabra, letras_lista, posiciones_lista


def palabra_en_diccionario(largo_palabra, letras_lista, posiciones_lista, diccionario):
    
    palabras_posibles_encontradas = []

    for palabra_dicc in diccionario:
        
        palabra_dicc = palabra_dicc.rstrip().lower()
        
        if int(largo_palabra) == int(len(palabra_dicc)):
            
            letras_palabra_dicc = []
            
            palabra_posible = True
            
            for letra in palabra_dicc:
                letras_palabra_dicc.append(letra)

            i = 0

            for letra in posiciones_lista:
                
                if not letras_palabra_dicc[int(letra)-1] == letras_lista[int(i)]:
                    palabra_posible = False
                    break
                i += 1

            if palabra_posible == True:
                palabras_posibles_encontradas.append(palabra_dicc)


    if len(palabras_posibles_encontradas) > 0:
        return palabras_posibles_encontradas
    return False


def main():
    
    with open("diccionario.txt", "r") as diccionario:  
        
        largo_palabra, letras_lista, posiciones_lista = entrada()

        palabra_en_dicc = palabra_en_diccionario(largo_palabra, letras_lista, posiciones_lista, diccionario)

        if type(palabra_en_dicc) == list:
            print(f"Las palabras encontradas son: {palabra_en_dicc}")
        elif palabra_en_dicc == False:
            print("Su palabra no encuentra en el diccionario.")


main()