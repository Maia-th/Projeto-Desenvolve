import os

def main():
    frase = input("Digite uma frase: ")
    nome_arquivo = "frase.txt"

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(frase)
    
    caminho_completo = os.path.abspath(nome_arquivo)
    
    print(f"Frase salva em {caminho_completo}")

if __name__ == "__main__":
    main()