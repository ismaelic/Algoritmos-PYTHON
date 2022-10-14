from collections import deque 

n, m = [int(x) for x in input().split()]

matrix = [[] for x in range(n)]
for i in range(n):
    matrix[i] = list(input())
    for j in range(m):
        if matrix[i][j] == 'A':
            start = (i,j)
        if matrix[i][j] == 'B':
            end = (i,j)

path = [[-1 for i in range(m)] for j in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
Direc = list('DURL')


def valid(x,y):
    return (x>=0) and (x<n) and (y>=0) and (y<m) and (matrix[x][y] != '#') and (path[x][y]==-1)

def drawpath():
    x,y = end
    p = deque()
    while (x,y) != start:
        i = path[x][y]
        p.appendleft(Direc[i])
        x -= dx[i]
        y -= dy[i]
    print("YES")
    print(len(p))
    print(''.join(p))


q = deque([start])
path[start[0]][start[1]] = -2

while len(q)>0:
    x,y = q.popleft()
    if(x,y)==end:
        drawpath()
        exit()
    for i in range(4):
        xp = x + dx[i]
        yp = y + dy[i]
        if valid(xp,yp):
            path[xp][yp] = i
            q.append((xp,yp))

print("NO")