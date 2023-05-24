def findParent(parent, x):
  if parent[x] != x:
    parent[x] = findParent(parent, parent[x])
  return parent[x]

def unionParent(parent, a, b):
  a = findParent(parent, a)
  b = findParent(parent, b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a
    
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

edges = []
result = 0
max_cost = 0

for i in range(m):
  # a와 b를 연결하는 길의 유지비가 c라는 뜻
  a, b, c = map(int, input().split())
  edges.append((c, a, b))  
edges.sort()

for edge in edges:
  cost, a, b = edge
  if findParent(parent, a) != findParent(parent, b):
    unionParent(parent, a, b)
    result += cost
    max_cost = cost

print(result - max_cost)