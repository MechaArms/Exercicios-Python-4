#Exercicio 12
#Foram anotadas as idades e alturas de 30 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random
idades = []
alturas = []
aluno_13 = []
media_13 = []

for i in range(30):
    numero_aleatorio = idades.append(random.randrange(1, 20))
    numero_aleatorio2 = alturas.append(random.randrange(50, 200))

for i in range(30):
    if idades[i] > 13:
        aluno_13.append(alturas[i])

media = sum(aluno_13) / len(aluno_13)

for i in range(len(aluno_13)):
    if aluno_13[i] < media:
        media_13.append(aluno_13[i])

print('\nA idade dos alunos são:\n',idades,'\nA altura dos alunos em cm são:\n',alturas)
print('\nForam ',len(aluno_13),' alunos com idade acima de 13 anos que são:\n',aluno_13)
print('\nA média de altura desses ',len(aluno_13),' alunos é:', media,'cm')
print('\nForam ',len(media_13),' alunos com mais de 13 anos possuem altura inferior à média de altura:\n',media_13)