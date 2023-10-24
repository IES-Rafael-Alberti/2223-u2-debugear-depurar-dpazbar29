#2.4.1
'''
EJERCICIO DEL BUCLE BURBUJA
'''
def organizador(cadena):
    n = len(cadena)
    for i in range(n-1):
        for j in range(0, n-i-1):
            
            if cadena[j] > cadena[j+1]:
                
                cadena[j], cadena[j+1] = cadena[j+1], cadena[j]
    return cadena

if __name__ == "__main__":

    #entrada  
    cadena = [8, 3, 1, 19, 14]

    #proceso
    devolucion = organizador(cadena)

    print(devolucion)
    