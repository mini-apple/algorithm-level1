from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
# 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]
# 강의 시간 리스트
time = [0] * (v+1)

# 방향그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
  # 강의시간, 선수 강의 노드 순서로 입력됨, 마지막은 -1로 구분
  data = list(map(int, input().split()))
  time[i] = data[0]
  for x in data[1:-1]:  # 선수강의들에 대해서
    indegree[i] += 1    # 진입차수를 1 증가시키고
    graph[x].append(i)  # 방향성을 고려하여 그래프에 추가

# 위상정렬 함수
def topology_sort():
  result = copy.deepcopy(time)  # 알고리즘 수행 결과를 담을 리스트
  q = deque()

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 위상정렬 수행 결과를 출력
  for i in range(1, v+1):
    print(result[i])

topology_sort()
