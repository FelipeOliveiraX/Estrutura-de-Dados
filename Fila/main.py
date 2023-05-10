from classes import Nodo, Fila

# Cria uma fila vazia.
fila = Fila()
print("Fila vazia: ", fila)

# Insere elementos na fila.
for i in range(5):
    fila.insere(i)
    print("Insere o valor {0} final da fila: {1}".format(i, fila))
    
print('\n')

# Remove elementos da fila.
while fila.primeiro != None:
    fila.remove()
    print("Removendo elemento que está no começo da fila: ", fila)
