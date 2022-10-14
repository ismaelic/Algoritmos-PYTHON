from collections import deque
n, m = map(int, input().split())
g = [[] for x in range(n+1)]
for i in range(m): 
	a, b = [int(x) for x in input().split()] # leo los extremos de la arista
	g[a].append(b) # agrego elemento 2 en la lista del 1
	g[b].append(a) # agrego elemento 1 en la lista del 2
vis = [int(0)] * (n+1)
print("lista de adyacencia: ",g)
q = deque()
def bfs(v):
    q.append(v) #agrego el primer nodo 
    vis[v] = 1 #visito el primer nodo en color negro
    while len(q) > 0: #mientras existan elementos por visitar
        u = q.popleft() #empiezo en el orden de visita
        for e in g[u]:
            if (vis[e]==1 or vis[e]==0) and vis[u]==1: #valido si se visito o si es color negro y si el padre es color negro
                vis[e] = 2 #visito en color blanco
                q.append(e)
            elif vis[e]==0 and vis[u] == 2: #valido si se visito y el padre es blanco
                vis[e] = 1 #visito en color negro
                q.append(e)


for i in range(n+1): #si existen componentes separadas debemos visitarlas tambien
	if not vis[i]:
		bfs(i)


bfs(1)
print("blanco = 2 , Negro = 1, Ignorar = 0") # identificadores de colores
for x,i in enumerate(vis): print("nodo:",x,":",i, sep = '  ') #imprimo numero de nodo y color