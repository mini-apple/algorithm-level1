n, m = map(int, input().split())

min_lst = list(range(n))

for i in range(n):
  data = list(map(int, input().split()))
  min_lst[i] = min(data)

ans = max(min_lst)
print(ans)