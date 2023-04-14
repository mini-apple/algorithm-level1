n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# first 더하는 횟수
count = (m // (k + 1)) * k
count += m % (k + 1)

# second 더하는 횟수: m - first
result = 0
result += count * first
result += (m - count) * second

print(result)
