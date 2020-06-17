
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
        lista.append(random.randint(1,6))
    
    return lista


def ordenar2 (numeros):

    numeros_enorden = sorted(numeros)

    return numeros_enorden


def contar (numeros, numero):

    repeticiones = numeros.count(numero)
    
    return repeticiones
    

def buscar (numeros, numero):
    
    if numero in numeros:
        index = numeros.index(numero)
        return index
    else:
        print("error")


    