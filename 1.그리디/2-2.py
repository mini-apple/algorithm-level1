# 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬해서 첫번째로 큰 수와 두번째로 큰 수 찾아내기
data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  # first를 k번 더하고 second를 더함, m == 0이면 탈출
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)