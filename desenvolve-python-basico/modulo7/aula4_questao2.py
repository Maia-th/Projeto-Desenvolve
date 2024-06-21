import string

def limpar_palavra(palavra):
    palavra_limpa = ''.join(caracter for caracter in palavra if caracter.isalpha())
    return palavra_limpa.lower()

def main():
    arquivo_entrada = "frase.txt"
    arquivo_saida = "palavras.txt"
    
    with open(arquivo_entrada, 'r') as arquivo:
        frase = arquivo.read().strip()
    
    palavras = frase.split()
    
    palavras_limpas = []
    
    for palavra in palavras:
        palavra_limpa = limpar_palavra(palavra)
        if palavra_limpa:
            palavras_limpas.append(palavra_limpa)
    
    with open(arquivo_saida, 'w') as arquivo:
        for palavra in palavras_limpas:
            arquivo.write(palavra + '\n')
    
    with open(arquivo_saida, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

if __name__ == "__main__":
    main()

