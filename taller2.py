# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:49:01 2021

@author: Jbeltrant
"""

# TALLER DE EXCERISM - CORTE 2


# EJERCICIO 1 - Binary
# Convierta un número binario, representado como una cadena.
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
        return str(decimal) + binario


numero = int(input('Ingresar el número a convertir a número binario: '))
print(binarizar(numero))


# EJERCICIO 2 - Acronym
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


# EJERCICIO 3 - Hamming
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


# EJERCICIO 4 - Raindrops
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


# EJERCICIO 5 - Scrabble Score
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


# EJERCICIO 6 Pangram
# Determine si una oración es un pangrama.
def es_pangrama(cadena):
    import string
    cadena = cadena.lower()
    alfabeto = string.ascii_lowercase
    for letra in alfabeto:
        if letra not in cadena:
            return False
    return True


# EJERCICIO 7 - Accumulate
# Determinar correctamente el menor número de monedas que se deben dar a un
# cliente de tal forma que la suma del valor de las monedas equivaldría
# a la cantidad correcta de cambio.
def vueltasRec(listaValoresMonedas, vueltas):
    minMonedas = vueltas
    if vueltas in listaValoresMonedas:
        return 1
    else:
        for i in [m for m in listaValoresMonedas if m <= vueltas]:
            numeroMonedas = 1 + vueltasRec(listaValoresMonedas, vueltas-i)
            if numeroMonedas < minMonedas:
                minMonedas = numeroMonedas
                return minMonedas


print(vueltasRec([1, 5, 10, 25], 63))

# EJERCICIO 8 - Sieve
# Utilice el Tamiz de Eratosthenes para encontrar todos los primos
# de 2 a un número dado.
pp = 2
ps = [pp]
lim = raw_input("Quieres generar números primos hasta qué número: ")
    while pp < int(lim):
        pp += 1
        for a in ps:
            if a*a > pp:
                ps.append(pp)
                break
            if pp % a == 0:
                break


# EJERCICIO 9 - Isogram
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


# EJERCICIO 10 - Leap
# Dado un año, informe si es un año bisiesto.
def bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return 'El año %d es bisiesto.' % año
    else:
        return 'El año %d no es bisiesto.' % año


try:
    año = int(raw_input('Ingresa un número de año: '))
    print bisiesto(año)

# JABT
