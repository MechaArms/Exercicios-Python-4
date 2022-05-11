#Exercicio 24
'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''

import random
lancamentos = []
for i in range(100):
    lancamentos.append(random.randrange(1, 6 + 1))
for i in range(6):
    print('O número', i + 1, 'foi gerado ', lancamentos.count(i + 1), 'vezes')