import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
	x, y = map(int, input().split())
	g[x-1].append(y-1)
vis = [int(0)] * n
topo = []
def dfs(v):
	vis[v] = 1
	for e in g[v]:
		if vis[e]==0:
			dfs(e)
		elif vis[e]==1:
			print("IMPOSSIBLE")
			exit()
	topo.append(v)
	vis[v] = 2
	
for i in range(n):
	if vis[i]==0:
		dfs(i)

topo.reverse()
for x in topo: 
    print(x+1, end=' \n'[x==topo[-1]])
