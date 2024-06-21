import urllib.request

def download_roteiro(url, nome_arquivo):
    try:
        urllib.request.urlretrieve(url, nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' baixado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

def analisar_roteiro(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            print(f"Texto das primeiras 25 linhas do arquivo '{nome_arquivo}':")
            for i in range(min(25, len(linhas))):  
                print(linhas[i].rstrip()) 
            
            num_linhas = len(linhas)
            print(f"\nNúmero total de linhas do arquivo '{nome_arquivo}': {num_linhas}")
            
            linha_mais_longa = max(linhas, key=len).rstrip()
            num_caracteres = len(linha_mais_longa)
            print(f"\nLinha com maior número de caracteres (comprimento {num_caracteres}):")
            print(linha_mais_longa)
            
            nome_personagens = ["Nonato", "Íria"]
            contagem_nonato = 0
            contagem_iria = 0
            
            for linha in linhas:
                linha_lower = linha.lower() 
                for nome in nome_personagens:
                    contagem = linha_lower.count(nome.lower())
                    if nome.lower() == "nonato":
                        contagem_nonato += contagem
                    elif nome.lower() == "íria":
                        contagem_iria += contagem
            
            print(f"\nNúmero de menções aos personagens 'Nonato' e 'Íria':")
            print(f"Nonato: {contagem_nonato}")
            print(f"Íria: {contagem_iria}")
            
    except Exception as e:
        print(f"Ocorreu um erro durante a leitura do arquivo: {e}")

def main():
    url_roteiro = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"
    nome_arquivo = "estomago.txt"
    
    download_roteiro(url_roteiro, nome_arquivo)
    analisar_roteiro(nome_arquivo)

if __name__ == "__main__":
    main()
