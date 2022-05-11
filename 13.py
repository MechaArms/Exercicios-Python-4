#Exercicio 13
'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''
temperatura_meses = []
meses = ['Janeiro', 'Fevereiro', 'Março','Abril',
    'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print('\nMês de ', meses[i], ' :')
    media = temperatura_meses.append(float(input('Digite a temperatura média: ')))

media_anual = sum(temperatura_meses) / 12
print('\n' * 3)
for i in range(12):
    if temperatura_meses[i] > media_anual:
        print('Temperatura a cima da média no mês: ', meses[i])