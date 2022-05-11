#Exercicio 6
'''
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''

notas = []
media_turma = []

cont = 1
for i in range(10):
    print('\nAluno ',cont)
    for j in range(4):
        nota = float(input('Digite a nota: '))
        notas.append(nota)
    media = sum(notas) / len(notas)
    media_turma.append(media)
    print('\nNotas:', notas,'\nMedia: %.2f'% media)
    cont += 1
    notas.clear()

print('\nMelhores Medias\n')

for i in range(10):
    if media_turma[i] >= 7:
        print('Aluno nº ',i + 1,'Media: ',media_turma[i])