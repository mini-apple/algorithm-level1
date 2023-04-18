n = input()
x, y = ord(n[0]), int(n[1])

# a=97
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0
for i in range(8):
  mx = x + dx[i]
  my = y + dy[i]
  if mx<97 or mx>104 or my<1 or my>8:
    continue  
  count+=1
print(count)