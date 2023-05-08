n = int(input())
data = list(map(int, input().split()))

d = [0]*n
d[0] = data[0]
d[1] = data[1]
d[2] = data[0] + data[2]

for i in range(3, n):
  d[i] = max(d[i-3], d[i-2]) + data[i]

print(d[n-1])