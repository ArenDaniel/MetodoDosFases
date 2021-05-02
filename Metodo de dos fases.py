import os
import math     
import numpy as np #Importar Librerias Math y Numpy

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

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
    x = 1
    for i in soluciones:        
        print('X',x,'',i)
        x = x+1
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

##c = [160, 120, 280,0,0]        #Coeficientes de la funcion Z a optimizar
##A = [
##    [-2, -1,  -4, 1, 0],         #Coeficientes de las restricciones y las variables que adicionmaos
##    [-2, -2, -2, 0, 1],    
##]
##b = [-1, -1.5,]      #Segunda parte de la restriccion
##
##dual = funcion_valor(c, simplex_dual(c, A, b))
##print('Dual: ', dual)

print("Metodo de las dos fases.")

nr = int(input("Ingrese el numero de restricciones: "))
nv = int(input("Ingrese el numero de variables: "))

c = []
a = []
b = []

print("A continuacion ingrese en orden los coeficientes de la Funcion Z a optimizar")
for i in range(nv):    
    print("Ingrese coeficiente",i+1," de la funcion Z")
    z = input("Z: ")
    c.append(float(z))
for i in range(nr):
    c.append(float(0))
    if(nr == 1):
        c.append(float(0))


borrarPantalla()

print("A continuacion ingrese los coeficientes y el segundo miembro de la desigualdad")
for i in range(nr):
    laux =[]
    print("Ingrese coeficientes de la restriccion numero", i+1)
    for j in range(nv+1):
        print("Variable:",j+1)        
        x = float(input("Dato: "))
        x = x*-1        
        if(j == nv):
            b.append(float(x))
        else:
            laux.append(float(x))            
    a.append(laux)    
    borrarPantalla()

if(nr == 1):
    a[0].append(float(1))
    a[0].append(float(0))   
        
if(nr == 2):
    a[0].append(float(1))
    a[0].append(float(0))
    
    a[1].append(float(0))
    a[1].append(float(1))
    
if(nr == 3):
    a[0].append(float(1))
    a[0].append(float(0))
    a[0].append(float(0))
    
    a[1].append(float(0))
    a[1].append(float(1))
    a[1].append(float(0))

    a[2].append(float(0))
    a[2].append(float(0))
    a[2].append(float(1))
    
dual = funcion_valor(c, simplex_dual(c, a, b))
print('Dual: ', dual)

    
        


    

        
        




    
        
    
    




