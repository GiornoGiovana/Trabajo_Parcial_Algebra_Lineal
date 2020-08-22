'''
Pida el ingreso de n[8,12] y genere aleatoriamente npares ordenados. 
El programa debemostrar gráficamente la curva que se aproxime mejor linealmente a los npares ordenados. 
El usuario debe seleccionar el tipo de curva: polinomial(de grado 𝑚≤6), exponencial o potencial.
'''
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
#from matplotlib.figure import Figure

import random


'''
def gencoordinates(m, n):
    seen = set()

    x, y = randint(m, n), randint(m, n)

    while True:
        seen.add((x, y))
        yield (x, y)
        x, y = randint(m, n), randint(m, n)
        while (x, y) in seen:
            x, y = randint(m, n), randint(m, n) 


def pair_generator(numbers): 
  """Return an iterator of random pairs from a list of numbers.""" 
  # Keep track of already generated pairs 
  used_pairs = set() 
 
  while True: 
    pair = random.sample(numbers, 2) exit
    
    # Avoid generating both (1, 2) and (2, 1) 
    pair = tuple(sorted(pair)) 
    if pair not in used_pairs: 
      used_pairs.add(pair) 
      yield pair 
     
# A relatively long list 
numbers = list(range(1000000)) 
gen = pair_generator(numbers) 
 
# Get 10 pairs: 
for i in xrange(10): 
  pair = gen.next() 
  print(pair) 
'''

# funcion que genera los pares de acurdo al numero de pares seleccionados,
# y muestra en la interfaz los pares que se generaron


def generar_arreglo():
    a = []
    n = numeroPares.get()  # devuelve el valor de la escala
    for i in range(n):
        rand = random.randint(0, 15)
        a.append(rand)
    print(a)
    return a

# ejemplo de arreglo: [3, 9, 12, 14, 5, 13, 8, 1]


def pares(arreglo):
    """Return an iterator of random pairs from a list of numbers."""
    # Keep track of already generated pairs
    used_pairs = set()

    while True:
        pair = random.sample(arreglo, 2)
        # Avoid generating both (1, 2) and (2, 1)
        pair = tuple(sorted(pair))
        if pair not in used_pairs:
            used_pairs.add(pair)
            yield pair
    return tuple(pair)


def exit():
    return root.destroy()


def generarpares():
    paresde = pares(generar_arreglo())
    print(pares)


# --------- INTERFAZ DEL PROGRAMA -----------
root = Tk()
root.title('Regresión Lineal')
root.maxsize(1100, 800)
root.geometry('500x300')
root.config(bg='white')


UI_frame = Frame(root, width=800, height=400, bg='white')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

# Escala para los numeros de pares ordenados que vamos a tener
numeroPares = Scale(UI_frame, from_=8, to=12, length=200, digits=1,
                    resolution=1, orient=HORIZONTAL, label="Numero de elementos")
numeroPares.grid(row=0, column=1, padx=5, pady=5)


# Boton para generar los pares ordenados
Button(UI_frame, text="Generar Pares", command=generarpares,
       bg='green').grid(row=0, column=4, padx=10, pady=10)

# Boton para salir del programa
Button(UI_frame, text="Salir", command=exit, bg='red').grid(
    row=0, column=5, padx=10, pady=10)

root.mainloop()
