from classes import Nodo, Pilha

# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.
for i in range(5):
    pilha.insere(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

print('\n')

# Remove elementos na pilha.
while pilha.topo != None:
    pilha.remove()
    print("Removendo elemento que está no topo da pilha: ", pilha)
