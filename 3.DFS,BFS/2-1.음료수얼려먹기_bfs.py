from collections import deque

n, m = map(int, input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int, input())))

result = 0

def bfs(x, y):
  if graph[x][y]==1:
    return False
    
  queue = deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
    if x<0 or x>=n or y<0 or y>=m:
      continue
    if graph[x][y]==1:
      continue
    if graph[x][y]==0:
      graph[x][y]=1
      queue.append((x+1, y))
      queue.append((x-1, y))
      queue.append((x, y+1))
      queue.append((x, y-1))
  
  return True


for i in range(n):
  for j in range(m):
    if bfs(i, j):
      result+=1
    
print(result)