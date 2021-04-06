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

import unittest

from two_fer import two_fer


class TwoFerTest(unittest.TestCase):
    def test_no_name_given(self):
        self.assertEqual(two_fer(), "One for you, one for me.")

    def test_a_name_given(self):
        self.assertEqual(two_fer("Leonela"), "One for Leonela, one for me.")

    def test_another_name_given(self):
        self.assertEqual(two_fer("Jorge"), "One for Jorge, one for me.")


if __name__ == "__main__":
    unittest.main()


