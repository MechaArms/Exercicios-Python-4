#Exercicio 21
'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
Calcule e mostre:
    a. O modelo do carro mais econômico;
    b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros 
       e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. 
       Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
       Os dados são fictícios e podem mudar a cada execução do programa. 

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''

veiculos = ['Fusca', 'Palio', 'UNO', 'Ferrari', 'HB20']
consumo_carros = []

print('\nComparativo de Consumo de Combustível\n')

for i in range(5):
    print('veículo',i + 1,'\nNome: ',veiculos[i])
    km_litro = float(input('Km por litro: '))
    consumo_carros.append(km_litro)

print('\nRelatório Final')

for i in range(5):
    print(f'{i+1} - {veiculos[i]:<15} - {consumo_carros[i]:>6.1f} - {round(1000 / consumo_carros[i]):>5.1f} litros - R$ {round(1000 / consumo_carros[i]) * 2.25:.2f}')

indice_menor_consumo = consumo_carros.index(max(consumo_carros))
print('O menor consumo é o do ', veiculos[indice_menor_consumo])