# Desenvolva um dicionário em Python para armazenar o nome e a nota de 3 alunos, realizando a leitura dos valores por meio de um estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retorne a média.
# import numpy as np

matriz=[[0,0], [0,0], [0,0]]

soma=0
media=0

matriz[0][0] = input(f'Digite o nome do 1ºaluno: ')
matriz[0][1] = float(input(f'Digite a nota do 1ºaluno: '))
matriz[1][0] = input(f'Digite o nome do 2ºaluno: ')
matriz[1][1] = float(input(f'Digite a nota do 2ºaluno: '))
matriz[2][0] = input(f'Digite o nome do 3ºaluno: ')
matriz[2][1] = float(input(f'Digite a nota do 3ºaluno: '))

print()
print()
print(matriz, end='')
print()
print()

soma = matriz[0][1] + matriz[1][1] + matriz[2][1]
media = soma /3
print(f'A média dos 3 alunos é {media}')

# soma = 0
# alunos = []

# while True:
#     nome = input('Insira o nome do aluno: ')
#     nota = input('Insira a nota do aluno: ')
#     # alunos = np.array([int(nota), nome])
#     alunos.append([int(nota), nome])
#     if len(alunos) == 3:
#         break

# print(alunos)

# for i in range (alunos.shape[0]):
#     print(alunos[i])
# for d in range(alunos.shape[1]):
#          soma = soma + alunos[i][d]

# print(soma)

# matriz[1][1] = input(f'Digite o nome do aluno: ')
# matriz[2][1] = input(f'Digite o nome do aluno: ')
# for l in range(0, 3):
#     for c in range(0, 2):
#         matriz[0][0] = input(f'Digite o nome do aluno: ')
#         matriz[0][1] = input(f'Digite o nome do aluno: ')
#         matriz[0][2] = input(f'Digite o nome do aluno: ')
