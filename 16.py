#Exercicio 16
'''
Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
    a -  $200 - $299
    b -  $300 - $399
    c -  $400 - $499
    d -  $500 - $599
    e -  $600 - $699
    f -  $700 - $799
    g -  $800 - $899
    h -  $900 - $999
    i -  $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

possiveis_salarios = [
    [200,299],[300,399],[400,499],
    [500,599],[600,699], [700,799],
    [800,899],[900,999]
    ]
quantidades = [0,0,0,0,0,0,0,0,0]           # pode se usar tambem quantidades = [0] * 9

salarios = []
vendas_brutas = True
while vendas_brutas != 0:
    vendas_brutas = float(input("\nDigite a valor das vendas: "))
    if vendas_brutas == 0:
        break
    else:
        salario = (vendas_brutas * 0.09) + 200
        if salario < 1000:
            for i in range(len(possiveis_salarios)):
                if salario > possiveis_salarios[i][0] and salario < possiveis_salarios[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
print("\n" * 3)
for i in range(len(possiveis_salarios)):
    print("Entre R$", possiveis_salarios[i][0], "e R$", possiveis_salarios[i][1], ":", quantidades[i])
print("Salarios maiores que R$1000:", quantidades[8])