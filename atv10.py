# Crie uma função que
# recebe um único parâmetro, uma lista de números.


#  - Dentro da função, calcule a média dos
# números na lista e retorne o valor da média


# - Fora da função, crie
# uma lista de números (Por exemplo, [10, 20, 30, 40, 50] e atribua a uma variável


# - Apresenta o resultado
# da função

def calcularMedia(listaNumeros):
  media = sum(listaNumeros) / len(listaNumeros)
  return media

numerosLista = [10, 20, 30, 40, 50, 60, 80, 90, 70]
mediaNumeros = calcularMedia(numerosLista)
print("A média dos números é: ",mediaNumeros)
