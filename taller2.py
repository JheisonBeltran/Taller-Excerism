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


# EJERCICIO 5 - Raindrops
# Convierta un número en una cadena que depende de los factores del número.
# Si el número tiene 3 como factor, salida 'Pling'.
# Si el número tiene 5 como factor, salida 'Plang'.
# Si el número tiene 7 como factor, salida 'Plong'.
# Si el número no tiene 3, 5 o 7 como factor,
# simplemente pase los dígitos del número directamente a través.
def convert(number, result=""):
    """
    El metodo convierte un número en una cadena que contenga sonidos de gotas
    de lluvias correspondientes a factores potenciales.
    Parameters
    ----------
    number = numero a convertir.
    Returns
    Retorna una cadena de PlingPlongPlang o en su caso el mismo número
    """

    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        result = f"{number}"
    return result


# EJERCICIO 6 - Scrabble Score
# Con una palabra, calcule la puntuación de scrabble para esa palabra.
# Letter                           Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10
def score(word, puntaje=0):
    """
    Este Metodo calcula un puntaje para una palabra, tomando puntos por letras
    Parameters
    word : palabra a calcular puntaje
    Returns
    retorna el puntaje de la palabra ingresada
    """

    for le in word.lower():
        if le in "aeioulnrst":
            puntaje = puntaje + 1
        if le in "dg":
            puntaje = puntaje + 2
        if le in "bcmp":
            puntaje = puntaje + 3
        if le in "fhvwy":
            puntaje = puntaje + 4
        if le in "k":
            puntaje = puntaje + 5
        if le in "jx":
            puntaje = puntaje + 8
        if le in "qz":
            puntaje = puntaje + 10
    return puntaje


# EJERCICIO 7 Pangram
# Determine si una oración es un pangrama.
def es_pangrama(cadena):
    import string
    cadena = cadena.lower()
    alfabeto = string.ascii_lowercase
    for letra in alfabeto:
        if letra not in cadena:
            return False
    return True
