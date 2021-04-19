import math     
import numpy as np #Importar Librerias Math y Numpy

def tablau(c, A, b):    #Funcion que obtiene los valores del problema y retorna unal ista para uso del programa
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

def basico(columna): #Retorna suma de las columnas
    return sum(columna) == 1 and len([c for c in columna if c == 0]) == len(columna) - 1

def solucion(tabla): #Nos devuelve las soluciones en una lista 
    columnas = np.array(tabla).T #Guardar las columnas de la tabla
    soluciones = [] #Crear lista de soluciones
    for columna in columnas[:-1]:
        solucion = 0
        if basico(columna):
            uno = columna.tolist().index(1)
            solucion = columnas[-1][uno] #Solucionamos la columna
        soluciones.append(solucion)        
    return soluciones #Retornamos la lista soluciones

def paso_pivote(tabla, pos_pivote): ##Obtener la posicion del pivote
    nueva_tabla = [[] for eq in tabla]    
    i, j = pos_pivote
    pivote_valor = tabla[i][j]
    nueva_tabla[i] = np.array(tabla[i]) /  pivote_valor
    
    for eq_i, eq in enumerate(tabla):
        if eq_i != i:
            multi = np.array(nueva_tabla[i]) * tabla[eq_i][j]
            nueva_tabla[eq_i] = np.array(tabla[eq_i]) - multi  
    return nueva_tabla

def funcion_valor(c, solution):    
    return sum(np.array(c) * np.array(solution))

def verificar_dual(tabla): #Funcion para verificar la solucion por metodo de dos fases
    entradas    = [fila[-1] for fila in tabla[:-1]]
    return any([entry < 0 for entry in entradas])

def pivote_dual(tabla): #De la tabla obtenemos el pivote y usamos dos fases para retornar la fila y columna donde se encuentra
    entradas = [fila[-1] for fila in tabla[:-1]]
    valor_min = min(entradas)
    fila = entradas.index(valor_min)
    
    columnas = []
    for index, element in enumerate(tabla[fila][:-1]):
        if element < 0:
            columnas.append(index)
    columnas_valores = [tabla[fila][c] / tabla[-1][c] for c in columnas]
    column_min_index = columnas_valores.index(min(columnas_valores))
    column = columnas[column_min_index]
    return fila, column

def simplex_dual(c, A, b): ##Resolvemos por dos fases
    tabla = tablau(c, A, b)

    while verificar_dual(tabla):
        pivot_position = pivote_dual(tabla)
        tabla = paso_pivote(tabla, pivot_position)

    return solucion(tabla)

c = [315, 110, 50,0,0,0] #Coeficientes de la funcion Z a optimizar
A = [
    [-15, -2,  -1, 1, 0,0], #Coeficientes de las restricciones
    [-7.5, -3, -1, 0, 1,0],
    [-5, -2, -1, 0, 0, 1]
]
b = [-200, -150, -120] #Segunda parte de la restriccion

dual = funcion_valor(c, simplex_dual(c, A, b))
print('Dual: ', dual)
