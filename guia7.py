import math as mt
from typing import List

def pertenece (lista: list,elemento: int)->bool:
    for i in range (len(lista)):
        if lista[i] == elemento:
            return True
    return False 

def pertenece2 (lista: List[int],elemento: int):
    indactual :int = 0
    while (indactual < len(lista)):
        valoractual: int = lista[indactual]
        if valoractual == elemento:
            return True
        else:
            indactual += 1
    return False 



def divideatodos (lista:list,elemento:int)->bool:
    for i in range(len(lista)):
        if lista[i] % elemento != 0:
            return False 
    return True



def sumatotal (lista: list)-> int:
    suma: int = 0
    for i in range (len(lista)):
        suma += lista[i]
    return suma 

def sumatotal2 (lista: List[int])->int:
    total: int = 0 
    indactual: int = 0
    while (indactual < len(lista)):
        total = total + lista[indactual]
        indactual += 1
    return (total)



def ordenados (lista: list)-> bool:
    for i in range (len(lista)-1):
        if lista[i] > lista [i+1]:
            return False 
    return True 



def palabralarga (lista: List[str])-> bool:
    for i in range (len(lista)):
        if len(lista[i]) > 7:
            return True
    return False


def palindromo (texto: str) -> bool:
    longitud = len(texto)
    for i in range (longitud):
        if texto[i] != texto[longitud - i - 1]:
            return False 
    return True 



def pertenece3 (lista: list,elemento: chr)->bool:
    for i in range (len(lista)):
        if lista[i] == elemento:
            return True
    return False 

def minuscula (contra: str)->bool:
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    for i in range (len(contra)):
        if (pertenece3 (minusculas,contra[i])):
            return True 
    return False 

def mayuscula (contra: str)->bool:
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range (len(contra)):
        if (pertenece3 (mayusculas,contra[i])):
            return True 
    return False 

def numero (contra: str)->bool:
    numeros = "0123456789"
    for i in range (len(contra)):
        if (pertenece (numeros,contra[i])):
            return True 
    return False 

def fortaleza (contra: str) -> str:
    longitud = len (contra)
    if (longitud > 8 and minuscula(contra) and mayuscula(contra) and numero(contra)):
        return "VERDE"
    if longitud < 5:
        return "ROJA"
    return "AMARILLA"

