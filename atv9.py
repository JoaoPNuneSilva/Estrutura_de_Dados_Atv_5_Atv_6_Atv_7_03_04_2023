# Efetuar o cálculo da
# quantidade de litros de combustível gasto em uma viagem, utilizando um
# automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve
# fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma,
# será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO *
# VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros
# de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA /
# 12.


# O programa deve
# apresentar os valores da velocidade média, tempo gasto na viagem, a distância
# percorrida e a quantidade de litros utilizada na viagem


# - Função para ler os
# valores (não recebe parâmetro e retorna os dois valores)


# - Função para calcular a
# distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)


# - Função para calcular a
# quantidade de litros (recebe como parâmetro a distância e retorna os litros)


# - Função para apresentar
# o resultado (recebe como parâmetro os valores e somente imprime o resultado)

tempViagem = float(input(f'Tempo de viagem gasto (em horas): '))
velocidade = float(input(f'Velocidade média durante a viagem (em km/h): '))
distancia = tempViagem * velocidade
kmPorLitro = distancia / 12
print(f"A distância percorrida foi: {distancia:.2f} km")
print(f"O tempo gasto foi: {tempViagem:.2f} horas")
print(f"A velocidade média foi: {velocidade:.2f} km/h")
print(f"Quantidade de litros utilizados: {kmPorLitro:.2f} L")
