n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:
  # 현재 그룹에 해당 모험가를 포함시키고
  count += 1  
  # 그룹에 포함된 모험가의 수가 현재 공포도 이상이면 그룹 결성
  if count >= i:  
    result += 1
    count = 0

print(count)