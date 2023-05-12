INF = int(1e9)

n = int(input())  # 노드 개수
m = int(input())  # 간선 개수

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자신에서 자신으로 가는 노드의 거리(비용)은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a==b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # a에서 b로 가는 비용을 c라고 설정
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행, k를 거쳐 a -> b로 이동
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    # 도달할 수 없는 경우 무한(INFINITY)을 출력
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    # 도달할 수 있는 경우 거리를 출력
    else:
      print(graph[a][b], end=" ")
  print()