import random
from math import sqrt

n = int(input("Digite o valor de n: "))

valores = [random.randint(0, 100) for _ in range(n)]
soma = sum(valores)

raiz = sqrt(soma)

print(f'A raiz quadrada resultante da soma dos {n} valores aleatorios = {raiz:.2f}')