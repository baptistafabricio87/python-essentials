#!/usr/bin/env python3
"""Exercicio Tabuada - Retorna a tabuada do 1 ao 10

Tabuada do 1:
1 x 1 = 1
...
-------------

Tabuada do 2:
2 x 1 = 2
...
-------------
"""

__version__ = '0.1.1'
__author__ = 'Fabricio Castro'


# numeros = [1, 2, 3, 4, 5, 6, 8, 9, 10]
# Iterable
numeros = list(range(1,11))


for numero in numeros:
	print("{:-^20}".format(f' Tabuada do {numero} '))
	print()
	for outro_numero in numeros:
	    resultado = numero * outro_numero
	    print("{:^20}".format(f'{numero} x {outro_numero} = {resultado}'))

	print()
	print('#' * 20)
