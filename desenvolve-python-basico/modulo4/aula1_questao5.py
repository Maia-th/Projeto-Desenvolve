n = int(input('Digite a quantidade de respondentes da pesquisa: '))
soma,controle = 0, n

while controle > 0:
    soma += int(input('Digite o valor da idade: '))
    controle -= 1

print(f'A media das idades é igual a {(soma/n):,.0f} anos.')