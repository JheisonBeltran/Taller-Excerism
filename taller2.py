# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:49:01 2021

@author: Jbeltrant
"""

# TALLER DE EXCERISM - CORTE 2


# EJERCICIO 1 - Two Fer
# Dado un nombre, devuelva una cadena con el mensaje: One for X, one for me.
# Donde X es el nombre dado.
# ‎Si falta el nombre, devuelva el st‎ring: One for you, one for me.
def two_fer(name="you"):
    """
    El metodo regresa una oración con el nombre ingresado
    Parameters
    ----------
    name = nombre ingresado
    Returns
    retorna la oración concatenada con el nombre ingresado
    """
    return f'One for {name}, one for me.'


# EJERCICIO 2 - Isogram
# Determine si una palabra o frase es un isograma.
def is_isogram(string):
    """
    El Metodo indica si una palabra es un isograma o no lo es.

    Parameters
    ----------
    string : Palabra a definir

    Returns
    Retorna un true si la palabra es un isograma o false si no lo es.
    """
    string = string.lower()
    for x in range(len(string)):
        for i in range(len(string)):
            if x != i and string[x] == string[i] and string[x].isalpha():
                return False

    return True

# EJERCICIO 3
