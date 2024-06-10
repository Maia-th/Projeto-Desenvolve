n=int(input("Digite a quantidade de experimentos: "))
cont,qnt,c,r,s = 0,0,0,0,0

while n != cont:
    tipo=input("Qual animal foi utilizado: C_coelho,R_rato ou S_sapo: ")
    qnt=int(input("Digite a quantidade de cobaias utilizadas: "))
    
    cont +=1
    if tipo=="c" or tipo=="C":
        c+=qnt
    elif tipo=="r" or tipo=="R":
        r+=qnt
    elif tipo=="s" or tipo=="S":
        s+=qnt

total=s+c+r

print(f"\nTotal de cobaias utilizadas: {total}")
print(f"Foram utilizados {c} coelhos, {r} ratos e {s} sapos")
print(f"Sapos representam {s/total*100:2.2f}%, coelhos representam {c/total*100:2.2f}% e ratos representam {r/total*100:2.2f}%.")