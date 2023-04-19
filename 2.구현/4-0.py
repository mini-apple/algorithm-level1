# 잘못된 답임. 3번 조건 뒤로가기가 없다.

n, m = map(int, input().split())
a, b, d = map(int, input().split())  # 캐릭터가 있는 칸의 좌표: a, b, 바라보는방향: d
m = []
for i in range(n):
  data = list(map(int, input().split()))
  m.append(data)

direction = [0, 1, 2, 3]
da = [0, -1, 0, 1]
db = [-1, 0, 1, 0]
next_a, next_b = 0, 0
count = 1

while True:
  # 탈출
  if m[a+1][b]==1 and m[a-1][b]==1 and m[a][b-1]==1 and m[a][b+1]==1:
    break

  for i in range(len(direction)):
    if d == direction[i]:
      next_a = a + da[i]
      next_b = b + db[i]

  if m[next_a][next_b] == 1:
    d = (d + 1) % 4
  else:
    # 이동
    m[a][b] = 1
    a, b = next_a, next_b
    count += 1
print(count)