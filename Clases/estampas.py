from itertools import *
def maxConsecutivo(E,D,lista):
    estamp = [0] # se le agrega el cero para permitir valores unitarios por ejemplo 001 = 1
    for i in range(D):
        estamp.append(lista[i]) # agregamos la lista de valores de estampas

    listaOrden = set() #un set con la suma de los digitos
    for i in combinations_with_replacement(estamp,E): #permutamos las combinaciones posibles -> 001 011...etc
        i = list(i)
        sum = 0
        for v in i:
            sum += v
        if sum!=0:
            listaOrden.add(sum)

    consecutivo = 0
    for i in range(len(listaOrden)):
        if 1+i == listaOrden.pop():
            consecutivo+=1
    return consecutivo #encontramos cuantos numeros consecutivos hay en el set

nums = [1,2,3,4,5,6,7,8,9] # por logica en numeros mayores no habran tantos consecutivos asi que del 1 al 9
E, D = map(int, input().split()) 
lista = []
maximoactual = 0
for i in combinations_with_replacement(nums,D): #lista combinaciones del 1-9 de D elementos
    r = maxConsecutivo(E,D,list(i)) # recibe el numero de digitos maximos, el numero de estampas distintas y la lista de las mismas
    if r > maximoactual: 
        lista = list(i) #encontramos el valor de las estampas con la que se forma la mayor consecutividad
        maximoactual = r #encontramos el mayor numero de consecutivos

print("valores de las estampas en soles:",lista," y el numero de combinaciones consecutivas:",maximoactual)