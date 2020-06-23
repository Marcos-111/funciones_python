
__author__ = "escalzo marcos"
__email__ = "escalzomd@gmail.com"
__version__ = "1.0"

import random
from random import sample
from random import randint




def promedio(numeros):

    if numeros == []:
        print("Lista vacia")
    
    else:
        promedio = sum(numeros) / len(numeros)
    
        return promedio


def lista_aleatoria (lista, k):
    
    numeros = sample(lista, k)

    return numeros


def lista_aleatoria2 (minimo, maximo, longitud):

    lista = []

    
    for i in range(longitud):
        lista.append(random.randint(minimo,maximo))  
    
    return lista


def ordenar2 (numeros):

    numeros_enorden = sorted(numeros)

    return numeros_enorden


def contar (numeros, numero):

    repeticiones = numeros.count(numero)
    
    return repeticiones
    

def buscar (numeros, numero):
    index = []
    if numero not in numeros:
        print(index)
    elif numero in numeros:
        
        indice = numeros.index(numero)
        index.append(indice)
        return index

def buscar2 (numeros, numero):

    indices = []
    indice_offset = 0
    while True:
        
        try:
            indice = numeros.index(numero, indice_offset)
            indice_offset = indice + 1
            indices.append(indice)
        
        except:
            
            break

    return indices
        
            


    
