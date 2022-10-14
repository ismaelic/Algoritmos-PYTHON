from itertools import *
import time
def FuerzaBruta():
    Pastor = False
    ind = {0:False,1:False,2:False,3:False}
    for i in product(ind.keys(), repeat=7):
        Pastor = False
        ind = {0:False,1:False,2:False,3:False} 
        for j in i:
            if Pastor == ind[j]:
                ind[j] = not ind[j]
                Pastor = not Pastor
                ind[3] = Pastor
            if (Pastor != ind[0] and Pastor != ind[1]) or (Pastor != ind[1] and Pastor != ind[2]): 
                break
        if(ind[0] and ind[1] and ind[2]):
            print(i)


def Backtraking(H,n,sol,Pastor,v):
    if H == n:
        if(v[0] and v[1] and v[2]):
            print(sol)
    else:
        for i in range(0,4):
            sol[H]=i
            sig = False
            x = v.copy()
            y = Pastor
            if Pastor == v[i]:
                Pastor = not Pastor
                v[i] = not v[i]
                v[3] = Pastor
                sig = True
                
            if (Pastor != v[0] and Pastor != v[1]) or (Pastor != v[1] and Pastor != v[2]):
                sig = False
            if sig:
                Backtraking(H+1,n,sol,Pastor,v)
            v = x
            Pastor = y


Pastor=False
v=[False,False,False,False]          
sol=[-1]*7
start = time.time()
Backtraking(0,7,sol,Pastor,v) 
end = time.time()
t=end-start
print(t)
#FuerzaBruta()
# sol: 1 3 0 1 2 3 1
# 0:lobo 1:oveja 2:col 3:solo