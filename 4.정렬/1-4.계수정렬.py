array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)  # 0부터 max값까지 카운트할 배열 초기화

for i in range(len(array)):
  count[array[i]] += 1

# 출력
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=" ")
