INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 길이 = 0
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0
      
# 간선정보 입력받기, 문제조건 a->b, b->a 둘 다 이동시간은 1이다.
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜
for i in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
  print(-1)
else: 
  print(distance)