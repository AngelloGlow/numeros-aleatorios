
from random import randint
def sorte():
    lista = []
    while True:
        x = randint(1, 60)
        lista.append(x)
        y = list(tuple(set(lista)))
        if len(y) == 6:
          return y
      

print(sorte())

