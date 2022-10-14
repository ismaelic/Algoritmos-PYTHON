def Anillo(H,n,solucion):
    if H == n:
        print(solucion)
        return
    else:
        for i in range(0,n):
            solucion[H] = i+1
        
            sig = True

            for i in range(H):
                if solucion[H] == solucion[i]:
                    sig = False
                    break
            
            if H>0:
                X = solucion[H] + solucion[H-1]
                cont=0
                cont2=0
                for i in range(1,X+1):
                    if X % i == 0:
                        cont+=1
                if H+1 == n:
                    X = solucion[H] + solucion[0]
                    for i in range(1,X+1):
                        if X % i == 0:
                            cont2+=1
                if cont > 2 or cont2 > 2:
                    sig = False
               
            if sig:
                Anillo(H+1,n,solucion)


n = 8
sol = [-1]*n
Anillo(0,n,sol)
            

        
            
        

        