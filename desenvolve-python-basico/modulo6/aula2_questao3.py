import random

lista1,lista2,lista3=[],[],[]

for i in range(1,21):
    a=random.randint(0,50)
    lista1.append(a)
    b=random.randint(0,50)
    lista2.append(b)
    if a in lista2:
        if a not in lista3:
            lista3.append(a)
    if b in lista1:
        if b not in lista3:
            lista3.append(b)
            
print(f"\n\nLista 1 - {lista1} \nLista 2 - {lista2}\nInterseção - {sorted(lista3)}\n")

for i in sorted(lista3):
    print(f"Contagem\n{i}:(lista1 = {lista1.count(i)}, lista2 =  {lista2.count(i)})")