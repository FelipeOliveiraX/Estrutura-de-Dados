class Nodo:
  """Esta classe representa um nodo de uma estrutura encadeada."""
  def __init__(self, dado=0, nodo_anterior=None):
    self.dado = dado
    self.anterior = nodo_anterior

  def __repr__(self):
    return '%s -> %s' % (self.dado, self.anterior)


class Pilha:
  """Esta classe representa uma pilha usando uma estrutura encadeada."""

  def __init__(self):
    self.topo = None


  def __repr__(self):
    return "[" + str(self.topo) + "]"
  
  def insere(self, novo_dado):
    """Insere um elemento no final da pilha."""

    # Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = Nodo(novo_dado)

    # Faz com que o novo nodo seja o topo da pilha.
    novo_nodo.anterior = self.topo

    # Faz com que a cabeça da lista referencie o novo nodo.
    self.topo = novo_nodo  

  def remove(self):
    """Remove o elemento que está no topo da pilha."""

    assert self.topo, "Impossível remover valor de pilha vazia."

    self.topo = self.topo.anterior