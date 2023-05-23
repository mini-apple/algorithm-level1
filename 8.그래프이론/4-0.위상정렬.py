from collections import deque

# 노드개수, 간선개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대해 진입차수를 0으로 초기화
indegree = [0] * (v+1)
# 그래프 정보를 담기위한 연결리스트 초기화
graph = [[] for i in range(v+1)]

# 방향그래프의 모든 간선정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)  # 정점 A에서 B로 이동 
  indegree[b] += 1    # 진입차수 1증가

# 위상정렬 함수
def topologySort():
  result = []   # 알고리즘 수행 결과를 담을 리스트
  q = deque()   

  # 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌 때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 위상정렬 수행결과 출력
  for i in result:
    print(i, end=" ")

topologySort()