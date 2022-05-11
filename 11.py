#Exercicio 11
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
C = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
intercalada = []
contador = 0
for i in range(10):
    intercalada.append(A[contador])
    intercalada.append(B[contador])
    intercalada.append(C[contador])
    contador += 1
print(intercalada)