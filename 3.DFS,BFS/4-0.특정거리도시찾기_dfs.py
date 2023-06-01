INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [INF] * (n+1)
distance[x] = 0

def dfs(start):
  if not graph[start]:
    return
  
  for edge in graph[start]:
    if distance[start] + 1 < distance[edge]:
      distance[edge] = distance[start] + 1
    dfs(edge)  

dfs(x)
cnt = 0
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    cnt += 1
if cnt == 0:
  print(-1)