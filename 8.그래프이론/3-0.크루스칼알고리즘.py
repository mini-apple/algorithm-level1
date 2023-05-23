# 특정 원소가 속한 집합을 찾기
def findParent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = findParent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def unionParent(parent, a, b):
  a = findParent(parent, a)
  b = findParent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선의 개수(union 연산) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종비용을 담을 변수
edges = []
result = 0

# 부모테이블을 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# 간선 정보 입력받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정 
  # 파이썬에선 튜플의 첫번째 원소를 기준으로 정렬한다.
  edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하니씩 확인하며
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if findParent(parent, a) != findParent(parent, b):
    unionParent(parent, a, b)
    result += cost

print(result)