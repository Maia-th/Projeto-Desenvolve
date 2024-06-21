import random
elementos=[]
num_elementos=random.randint(5,20)

for i in range(num_elementos):
    elementos.append(random.randint(1,10))

print("\nLista: \n\n",elementos)
print("\nSoma dos valores da lista: ",sum(elementos))
media = sum(elementos)/len(elementos)
print(f"\nMédia dos valores da lista: {media:.2f}")