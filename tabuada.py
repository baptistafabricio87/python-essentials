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

__version__ = '0.1.0'
__author__ = 'Fabricio Castro'


# numeros = [1, 2, 3, 4, 5, 6, 8, 9, 10]
# Iterable
numeros = list(range(1,11))


for numero in numeros:
	print(f'Tabuada do {numero}: \n')
	for outro_numero in numeros:
		print(f'{numero} x {outro_numero} = {numero*outro_numero}\n')
	print('-' * 12)
