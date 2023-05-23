def findParent(parent, x):
  if parent[x] != x:
    parent[x] = findParent(parent, parent[x])
  return parent[x]

def unionParent(parent, a, b):
  a = findParent(parent, a)
  b = findParent(parent, b)
  if a < b:
    parent[a] = b
  else:
    parent[b] = a

n, m = map(int, input().split())

# 부모테이블
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

result = []

for i in range(m):
  oper, a, b = map(int, input().split())
  if oper == 0:
    unionParent(parent, a, b)
  elif oper == 1:
    if findParent(parent, a) == findParent(parent, b):
      result.append("YES")
    else:
      result.append("NO")

for i in result:
  print(i)