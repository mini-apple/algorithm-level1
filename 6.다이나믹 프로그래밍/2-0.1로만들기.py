x = int(input())

# 앞서 계산된 결과를 저장하기 위한 dp테이블 초기화
d = [0]*30001

# dp - 바텀업
for i in range(2, x+1):
  # 현재 수에서 1을 빼는 경우
  d[i] = d[i-1] + 1
  if i%2==0:
    d[i] = min(d[i], d[i//2]+1)
  if i%3==0:
    d[i] = min(d[i], d[i//3]+1)
  if i%5==0:
    d[i] = min(d[i], d[i//5]+1)
  print(d[i])

print(d[x])
