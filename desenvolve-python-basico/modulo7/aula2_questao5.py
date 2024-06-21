import random

def embaralhar_palavras(frase):
    palavras = frase.split()  
    frase_embaralhada = []
    for palavra in palavras:
        if len(palavra) > 3: 
            caracteres = list(palavra[1:-1])  
            random.shuffle(caracteres)  
            palavra_embaralhada = palavra[0] + ''.join(caracteres) + palavra[-1]  
            frase_embaralhada.append(palavra_embaralhada)
        else:
            frase_embaralhada.append(palavra)  

    return ' '.join(frase_embaralhada)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
