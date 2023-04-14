n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

first = lst[0]
second = lst[1]

sum = 0
for i in range(m):
  if (i + 1) % (k + 1) == 0:
    sum += second
    continue
  sum += first

print(sum)
