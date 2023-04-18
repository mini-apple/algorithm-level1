input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

# 8가지 방향으로 이동가능한지 확인
result = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  if 1<=next_row and next_row<=8 and 1<=next_col and next_col<=8:
    result+=1
print(result)