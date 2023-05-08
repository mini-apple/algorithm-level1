n, m = map(int(input().split()))

array = []
for i in range(n):
  array.append(int(input()))

# dp테이블
d = [10001] * (m + 1)

d[0] = 0
# i는 화폐의 종류 (2, 3, 5 등)
for i in range(n):
  for j in range(array[i], m + 1):
    # (i-k)원을 만드는 방법이 존재하는 경우
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])
