import random
import time
from matplotlib import pyplot as plt
# Bubble sort   
def Bubblesort(arr): 
  n, intercambia, x = len(arr), True, -1
  while intercambia:
    intercambia, x = False, x + 1
    for i in range(1, n-x):
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        intercambia = True   


# Insertion sort
def Insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1] = key


# Selection sort
def Selectionsort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min],arr[i]


# Quick sort
def Quicksort(arr):
   quick_(arr,0,len(arr)-1)

def quick_(arr,first,last):
   if first<last:
       splitpoint = partition(arr,first,last)
       quick_(arr,first,splitpoint-1)
       quick_(arr,splitpoint+1,last)

def partition(arr, low, high):
    i = (low-1)       
    pivot = arr[(low+high)//2]    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


# Merge sort
def Mergesort(arr):
    if len(arr)>1:
        piv = len(arr)//2
        l = arr[:piv]
        r = arr[piv:]
        Mergesort(l)
        Mergesort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j +=1
            k += 1
    
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


# Heap Sort            
def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      if l < n and arr[i] < arr[l]:
          largest = l
      if r < n and arr[largest] < arr[r]:
          largest = r
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest) 
def Heapsort(arr):
      n = len(arr)
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)


#Medir el tiempo
def measure_time(sorting_alg, v,X):
  start = time.time()
  sorting_alg(v)
  end = time.time()
  t=end-start
  X.append(t)


#Generar vectores
def GenVec():
  x = random.sample(range(20),5)
  y = random.sample(range(100),10)
  z = random.sample(range(100),50)
  w = random.sample(range(1000),100)
  q = random.sample(range(1000),250)
  p = random.sample(range(1000),500)
  r = random.sample(range(10000),1000)
  t = random.sample(range(100000),10000)
  u = random.sample(range(1000001),100000)
  #c = random.sample(range(1000001),1000000)
  A = [x,y,z,w,q,p,r,t,u]#,c]
  return A

A = GenVec()

Bubble = []
Insertion = []
Selection = []
Merge = []
Quick = []
Heap = []

B = A.copy()

for i in B:
  measure_time(Mergesort, i,Merge)
C = A.copy()
   
for i in C:
  measure_time(Insertionsort, i,Insertion)
D = A.copy()

for i in D:
  measure_time(Bubblesort, i,Bubble)
E = A.copy() 

for i in E:
  measure_time(Quicksort, i,Quick)
F = A.copy()

for i in F:
  measure_time(Selectionsort, i,Selection)
G = A.copy()

for i in G:
  measure_time(Heapsort, i,Heap)




#X: elementos en el arr
arr = [5, 10, 50, 100, 250, 500, 1000, 10000, 100000]#, 1000000]


# Lineas 
plt.plot(arr,Bubble)
plt.plot(arr,Insertion)
plt.plot(arr,Selection)
plt.plot(arr,Merge)
plt.plot(arr,Quick)
plt.plot(arr,Heap)

#Labels
plt.legend(['Bubble','Insertion','Selection','Merge','Quick','Heap'])
plt.xlabel("tiempo")
plt.ylabel("Elementos en el arr")
plt.title("Medicion de tiempos algoritmos de ordenamiento")

#ventana
plt.show()