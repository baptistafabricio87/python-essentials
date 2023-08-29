#!/usr/bin/env python3
"""Exercicio Tabuada"""

numeros = [1, 2, 3, 4, 5, 6, 8, 9, 10]

for numero in numeros:
	print(f'Tabuada do {numero}: \n')
	for outro_numero in numeros:
		print(f'{numero} x {outro_numero} = {numero*outro_numero}')
	print('\n---------------')
