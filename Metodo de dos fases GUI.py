import math
import tkinter as tk
from tkinter import *
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

def resolver():
    c = [2, -3,0,0]        #Coeficientes de la funcion Z a optimizar
    A = [
        [1,-1,1,0]      #Coeficientes de las restricciones y las variables que adicionmaos       
    ]
    b = [-10]      #Segunda parte de la restriccion

    dual = funcion_valor(c, simplex_dual(c, A, b))
    print('Dual: ', dual)
class campo(object):
    def __init__(self):
        x = int(NInecuaciones.get())
        self.__ecuaciones = x
        print(self.__ecuaciones)
        self.__camposx = list(range(self.__ecuaciones+1))
        self.__camposy = list(range(self.__ecuaciones+1))
        self.__camposc = list(range(self.__ecuaciones+1))
        self.__li=[]
    def iniciar(self):
        n = int(NInecuaciones.get())
        x = tk.Label(v,text="X",width="5",font=("Helvetica",12), bg="RED")
        i = self.__ecuaciones
        for i in range(0, self.__ecuaciones):
            self.__camposx[i] = tk.Entry(v, width="5")
            self.__camposx[i]
            self.__camposx[i].pack()
            self.__camposx[i].place(x= 50,y=((i+1)*25)+150)   
        for i in range(0, self.__ecuaciones):
            self.__camposy[i] = tk.Entry(v, width="5")
            self.__camposy[i]
            self.__camposy[i].pack()
            self.__camposy[i].place(x= 100,y=((i+1)*25)+150) 
        for i in range(0, self.__ecuaciones):
            self.__camposc[i] = tk.Entry(v, width="5")
            self.__camposc[i]
            self.__camposc[i].pack()
            self.__camposc[i].place(x= 200,y=((i+1)*25)+150)                  
def crearcampos():
    obj = campo()
    obj.iniciar()
    BtnCampos = tk.Button(v, text="Resolver", width="10",bg="RED")
    BtnCampos.pack()
    BtnCampos.place(x= 76, y = 300)     
#Creacion de la Interfaz de Usuario
v = tk.Tk()
v.title("Metodo de las dos fases")
v.geometry("600x700")
#validacion = v.register(only_numbers)
LInecuaciones = tk.Label(v, text="Numero de Inecuaciones",font=("Helvetica", 12),width="30", bg = "#8BB2E4")
LInecuaciones.pack()
LInecuaciones.place(x=10,y=10)
NInecuaciones = tk.Entry(v,width="10", font=("Helvetica", 12))
NInecuaciones.pack()
NInecuaciones.place(x=300 , y=10)
#Numero de Variables
LVariables = tk.Label(v, text="Numero de Variables",font=("Helvetica", 12),width="30", bg = "#8BB2E4")
LVariables.pack()
LVariables.place(x=10,y=75)
NVariables = tk.Entry(v,width="10", font=("Helvetica", 12))
NVariables.pack()
NVariables.place(x=300 , y=75)
#Boton Crear Campos
BtnCampos = tk.Button(v, text="Agregar", command = crearcampos)
BtnCampos.pack()
BtnCampos.place(x= 150, y = 115)
resolver()


