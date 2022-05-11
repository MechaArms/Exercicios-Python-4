#Exercicio 7
#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from functools import reduce
numeros = [1, 2, 3, 4, 5]
multiplicados = reduce((lambda x, y: x * y), numeros)
print("\nSoma: ", sum(numeros), "\nMultiplicão: ", multiplicados, "\nNúmeros: ", numeros)