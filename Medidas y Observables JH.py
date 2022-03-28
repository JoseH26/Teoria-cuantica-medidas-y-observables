import numpy as np
import math

def sumacomplejos(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

def productocomplejos(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)

def modulocomplejos(a):
    return math.sqrt((a[0])**2 + (a[1])**2)

def conjugadocomplejos(a):
    return (a[0], -1*a[1])

def productomatrices(A, B):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        fila = []
        for j in range(f):
            suma = (0,0)
            for k in range(c):
                suma = sumacomplejos(suma, productocomplejos(A[i][k], B[k][j]))
            fila += [suma]
        m = m + [fila]
    return m

def producto_interno(A, B):
    for i in range(len(A)):
        A[i][0] = conjugadocomplejos(A[i][0])
    filas = len(A)
    matriz = [0 for i in range(filas)]
    for i in range(filas):
        matriz[i] = A[i][0]
    suma = (0,0)
    for i in range(len(matriz)):
        suma = sumacomplejos(suma, productocomplejos(matriz[i], B[i][0]))
    return suma

def norma_vector(v):
    x = [a[:] for a in v]
    n = producto_interno(v,x)
    return math.sqrt(n[0])

def matrizinversa(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [(-1*A[i][j][0],-1*A[i][j][1])]
        matriz = matriz + [fila]
    return matriz

def adicionmatrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila = fila + [sumacomplejos(A[i][j], B[i][j])]
        matriz = matriz + [fila]
    return matriz

def divisionComplejos(c1, c2):
    return c1/c2

def multiplicacionescalarmatriz(c, A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [(c*A[i][j][0],c*A[i][j][1])]
        matriz = matriz + [fila]
    return matriz

def probabilidadenunpunto(posicion, vector):
    return (100 * ((modulocomplejos(vector[posicion][0]))**2)/((norma_vector(vector))**2))

def probabilidadVectorAOtro(vector1, vector2):
    t = norma_vector(vector1) * norma_vector(vector2)
    p = producto_interno(vector2, vector1)
    return (100*(divisionComplejos(complex(p[0], p[1]), t)) )

def accionmatrizvectorComplejos(A,v):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        suma = (0,0)
        for j in range(columnas):
            suma = sumacomplejos(suma, productocomplejos(A[i][j], v[j][0]))
        matriz = matriz + [(suma)]
    return matriz

def valoresperado(matriz, vector):
    return producto_interno(accionmatrizvectorComplejos(matriz, vector), vector)

def unitaria(n):
    unitaria = []
    for i in range(n):
        fila = []
        for j in range(n):
            if j == i:
                fila += [(1,1)]
            else:
                fila += [(0, 0)]
        unitaria.append(fila)

def mediaobservable(observable, vectorket):
    return adicionmatrices(observable, inversamatriz(multiplicacionescalarmatriz(valoresperado(observable, vectorket), unitaria(len(observable[0])))))

def conjugadamatriz(A):
    matriz = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [conjugadocomplejos(A[i][j])]
        matriz = matriz + [fila]
    return matriz

def traspuestacomplejos(A):
    filas = len(A)
    columnas = len(A[0])
    matriz = [[0 for i in range(filas)]for i in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[j][i] = A[i][j]
    return matriz

def adjuntamatriz(A):
    return traspuestacomplejos(conjugadamatriz(A))

def productointernomatriz(A, B):
    longitud = len(A)
    suma = (0,0)
    A = adjuntamatriz(A)
    for i in range(longitud):
        for j in range(longitud):
            suma += sumacomplejos(suma, productocomplejos(A[i][j], B[i][j]))
    return suma

def varianza(observable, vectorket):
    m = mediaobservable(observable, vectorket)
    return valoresperado(productomatrices(m, m),vectorket)


def trazaComplejos(matriz):
    suma = (0,0)
    for i in range(len(matriz)):
        suma += sumacomplejos(suma, matriz[i][i])
    return suma

def main():
    print("Punto a")
    posiciones = int(input("Ingrese el numero de posiciones: "))
    vectorinicial = []
    for i in range(posiciones):
        valores = input("Digite la amplitud, (real, img): ")
        amplitud = tuple(int(x) for x in valores.split(","))
        vectorinicial += [[amplitud]]
    posicion = int(input("Digite la posicion en la cual quiere saber la probabilidad: "))
    vector1 = [x[:] for x in vectorinicial]
    print("La probabilidad es:",probabilidadenunpunto(posicion, vector1))

    print("Punto b")
    vector2 = []
    for i in range(posiciones):
        valores = input("Digite la amplitud, (real, img): ")
        amplitud = tuple(int(x) for x in valores.split(","))
        vector2 += [[amplitud]]
    print("La probabilidad es:",probabilidadVectorAOtro(vector2, vectorinicial))

main()
