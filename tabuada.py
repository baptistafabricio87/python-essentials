#!/usr/bin/env python3
"""Exercicio Tabuada - Exibe a tabuada do 1 ao 10

Tabuada do 1:
1 x 1 = 1
...
-------------

Tabuada do 2
2 x 1 = 2
...
-------------
"""
__version__ = '0.1.1'
__author__ = 'Fabricio Castro'

# Iterable
numeros = list(range(1, 11))

for numero in numeros:
    print('{:-^20}'.format(f' Tabuada do {numero} '))
    print()
    for outro_numero in numeros:
        resultado = numero * outro_numero
        print('{:^20}'.format(f'{numero} x {outro_numero} = {resultado}'))

    print()
    print('#' * 20)
