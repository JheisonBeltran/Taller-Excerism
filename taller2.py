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
    El metodo indica si una palabra es un isograma o no lo es.

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


# EJERCICIO 3 - Acronym
# Convierte una frase en su acrónimo.
def abbreviate(words, acronimo=""):
    """
    El metodo Convierte una frase a su acrónimo.
    Parameters
    words : Palabra a abreviar
    Returns
    Retorna las siglas de las iniciales de la frase ingresada
    """

    if "'" in words:
        words = words.replace("'", "")
    words = words.title()
    for letras in words:
        if letras.isalpha and letras.isupper():
            acronimo = acronimo + letras[0].upper()
    return acronimo


# EJERCICIO 4 - Hamming
# Calcula la diferencia de Hamming entre dos hebras de ADN.
def distance(strand_a, strand_b, distancia=0):
    """
    El metodo calcula la distancia de Hamming de dos cadenas de ADN
    Parameters
    ----------
    strand_a : cadena de adn
    strand_b : cadena de adn
    Returns
    Este metodo retorna un numero el cual es la distancia de
    hamming de las dos cadenas
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")
    else:
        for x in range(len(strand_a)):
            if strand_a[x] != strand_b[x]:
                distancia += 1

    return distancia
