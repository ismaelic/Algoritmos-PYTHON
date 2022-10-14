import random
from itertools import *
import time
def Contra(C,A):
    m = len(C)
    n = len(A)
    print("1. el espacio de busqueda es de: ", pow(n,m),"elementos")
    j = 0
    for i in product(A, repeat=m):
        i = ''.join(i)
        j+=1
        if i == C:
            print("Se encontro la contraseña en la iteracion:",j)
            break

A = [x for x in input('ingrese los digitos a usar:').split()]
m = 9
C = ''.join([random.choice(A) for i in range(m)])
print(C)
def measure_time(X,Y):
  start = time.time()
  Contra(X,Y)
  end = time.time()
  t=end-start
  print("2. el tiempo de ejecucion fue: ",t)

measure_time(C,A)
