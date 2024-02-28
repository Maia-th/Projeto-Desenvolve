saque = int(input("Digite um valor inteiro: "))

notas100 = saque // 100
saque = saque % 100

notas50 = saque // 50
saque = saque % 50

notas20 = saque // 20
saque = saque % 20

notas10 = saque // 10
saque = saque % 10

notas5 = saque // 5
saque = saque % 5

notas2 = saque // 2
saque = saque % 2

notas1 = saque // 1

print(f'\n{notas100} nota(s) de 100,00\n{notas50} nota(s) de 50,00\n{notas20} nota(s) de 20,00\n{notas10} nota(s) de 10,00\n{notas5} nota(s) de 5,00\n{notas2} nota(s) de 2,00\n{notas1} nota(s) de 1,00\n')