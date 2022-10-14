import numpy as np
def Karatsuba(X,Y):
    X,Y = str(X),str(Y)
    n = max(len(X),len(Y))
    if n>1:
        if n % 2 != 0:
            X,Y = '0'+X,'0'+Y
            n+=1
        a,b,c,d = X[:int(n/2)],X[int(n/2):],Y[:int(n/2)],Y[int(n/2):]
        resultado=(10**n)*Karatsuba(a,c)+10**int(n/2)*(Karatsuba(a,d)+Karatsuba(b,c))+Karatsuba(b,d)
        return np.long(resultado)
    return np.long(int(X))*np.long(int(Y))

print(Karatsuba(123456,789101))