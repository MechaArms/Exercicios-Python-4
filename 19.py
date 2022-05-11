#Exercicio 19
'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

    'Qual o melhor Sistema Operacional para uso em servidores?'
    
    As possíveis respostas são:
    
    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro


Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes 
e informar o vencedor da enquete. 
O formato da saída foi dado pela empresa, e é o seguinte:

    Sistema Operacional     Votos   %
    -------------------     -----   ---
    Windows Server           1500   17%
    Unix                     3500   40%
    Linux                    3000   34%
    Netware                   500    5%
    Mac OS                    150    2%
    Outro                     150    2%
    -------------------     -----
    Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''


print(''''Qual o melhor Sistema Operacional para uso em servidores?'

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')

urna = []
sistemas = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
indice_vitoria = []
indice_porcentagem_vitoria = []
eleitor = True
num_voto = 1

while eleitor != 0:
    print(f'\nEleitor nº {num_voto}\n')
    voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
    if voto == 0:
        break
    else:
        while voto < 0 or voto > 6:
            print('[Numero Inválido]')
            voto = int(input('Digite o seu voto [1 a 6] ou Digite [0] para sair: '))
        print('[Voto Confirmado]\n')
        urna.append(voto)
    num_voto += 1

print('\n' * 2)
print('{:<19}{:>10}{:>4}'.format('Sistema Operacional','Votos','%'))
print('{:<19}{:>10}{:>6}'.format('-'*19,'-'*5,'-'*3))

contador = 0
for i in range(len(sistemas)):
    porcentagem_voto = round((urna.count(contador+1) / len(urna)) * 100)
    print('{:<19}{:>10}{:>5}%'.format(sistemas[contador],urna.count(contador+1),porcentagem_voto))
    contador +=1
    indice_vitoria.append(urna.count(contador+1))
    indice_porcentagem_vitoria.append(porcentagem_voto)

print('{:<19}{:>10}'.format('-'*19,'-'*5,))
print('{:<19}{:>10}'.format('Total',len(urna)))

vitoria = max(indice_vitoria)
for i in range(len(sistemas)):
    if indice_vitoria[i] == vitoria:
        print('\nO sistema mais votado foi o ', sistemas[i], end=' ')

print('com ', max(indice_vitoria), ' votos, correspondendo a ', max(indice_porcentagem_vitoria), '% dos votos.')

