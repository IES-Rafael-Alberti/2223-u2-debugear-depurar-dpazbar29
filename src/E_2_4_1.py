#2.4.1
'''
EJERCICIO DEL BUCLE BURBUJA
'''
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-i-1):
            # Comparar elementos adyacentes
            if a[j] > a[j+1]:
                # Intercambiar elementos si están desordenados
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    
    a = [8, 3, 1, 19, 14]
    # Lista de ejemplo


    print(bubble_sort(a))
    