n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x, y):
  if x<0 or x>=n or y<0 or y>=m:
    return
    
  if graph[x][y]==0:
    return  
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx<0 or nx>=n or ny<0 or ny>=m:
      continue
    
    if graph[nx][ny]==0:
      continue  
    
    if graph[nx][ny]==1:
      graph[nx][ny] = graph[x][y] + 1
      dfs(nx, ny)

dfs(0,0)

for i in graph:
  print(i)

print(graph[n-1][m-1])