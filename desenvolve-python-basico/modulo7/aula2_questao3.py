def remover_pontuacao_e_espacos(frase):
    caracteres_pontuacao = ''',.!?;:()[]{}"'<>'''
    frase_sem_pontuacao = ''.join(caracter for caracter in frase if caracter not in caracteres_pontuacao)
    return frase_sem_pontuacao.lower()

def verificar_palindromo(frase):
    frase = remover_pontuacao_e_espacos(frase)
    if frase == frase[::-1]:
        return True
    else:
        return False

while True:
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    if frase.lower() == 'fim':
        break
    if verificar_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
