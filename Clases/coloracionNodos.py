n, m = [int(x) for x in input().split()]
g = [[] for x in range(n+1)]
for i in range(m): 
	a, b = [int(x) for x in input().split()]
	g[a].append(b) 
	g[b].append(a) 

colores = ['A','N','V','M']
ady =  ["COLOR:"] * (n+1)

for i in range(1,n+1):
    col = []
    colaux = colores[:]
    if ady[i] == "COLOR:":
        for v in g[i]:
            if ((ady[v]) not in col) and ady[v] != 'COLOR:':
                col.append(ady[v])
                colaux.remove(ady[v])
        ady[i] = colaux[0]
print (ady)