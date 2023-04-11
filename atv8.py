# Ler uma temperatura
# em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de
# conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C
# é a temperatura em graus Celsius


# - Função para ler e
# retorna o valor da temperatura (não recebe parâmetro)


# - Função para fazer o
# cálculo (recebe como parâmetro a temperatura em graus Celsius)


# - Função para mostrar o
# resultado, recebendo como parâmetro o valor e fazendo a impressão

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()