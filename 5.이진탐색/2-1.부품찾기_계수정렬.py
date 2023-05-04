# n - 가게의 부품 개수를 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] = 1

# m - 손님이 확인 요청한 부품 개수를  입력받기
m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print("yes", end=" ")
  else:
    print("no", end=" ")