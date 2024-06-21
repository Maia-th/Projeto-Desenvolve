import random
lista=[]
for i in range(20):
    lista.append(random.randint(-100,100))
print("Lista ordenada:\n\n",sorted(lista))
print("\nLista original:\n\n",lista)
print("\nÍndice do maior valor da lista: ",lista.index(max(lista)))
print("\nÍndice do menor valor da lista: ",lista.index(min(lista)))