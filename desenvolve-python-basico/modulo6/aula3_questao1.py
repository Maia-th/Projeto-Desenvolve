def solicitar_numeros():
    numeros = []
    
    while len(numeros) < 4:
        try:
            numero = int(input("Digite um número inteiro (mínimo de 4 valores): "))
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um valor inteiro válido.")
    
    while True:
        try:
            numero = int(input("Digite mais um número inteiro ou 'q' para parar: "))
            numeros.append(numero)
        except ValueError:
            print("Finalizando a entrada de números.")
            break
    
    return numeros

def main():
    numeros = solicitar_numeros()
    
    print("Lista original:", numeros)
    print("Os 3 primeiros elementos:", numeros[:3])
    print("Os 2 últimos elementos:", numeros[-2:])
    print("A lista invertida:", numeros[::-1])
    print("Elementos de índice par:", numeros[::2])
    print("Elementos de índice ímpar:", numeros[1::2])

if __name__ == "__main__":
    main()