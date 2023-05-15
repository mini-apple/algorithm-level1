import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

# n: 노드개수, m: 간선개수, c: 시작도시
n, m, c = map(int, input().split())

distance = [INF] * (n+1)  # 최단거리 테이블
graph = [[] for _ in range(n+1)]  # 그래프

# 간선 정보 입력받기
for _ in range(m):
  # x->y로 가는 데 걸리는 시간이 z
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:  # 큐가 비어있지 않다면
    dist, now = heapq.heappop(q)  # 최단거리가 가장 짧은 노드의 정보를 꺼내고
    # 최단거리 테이블에서 현재 큐에서 꺼낸 노드의 거리보다 짧은건 이미 처리된 노드이다.
    if distance[now] < dist:  
      continue
    # 현재 노드와 연결된 인접한 노드들을 확인
    for i in graph[now]: 
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
max = 0
for i in distance:
  if i < INF:
    cnt += 1
    if i > max:
      max = i

print(cnt-1, max)