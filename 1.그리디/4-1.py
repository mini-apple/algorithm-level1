n, k = map(int, input().split())

result = 0

while True:
  if n % k == 0:
    result += 1
    n = n // k
    if n == 1:
      break
  else:
    result += 1
    n -= 1
    if n == 1:
      break

print(result)