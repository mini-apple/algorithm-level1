n = int(input())
data = input().split()

y, x = [1, 1]
for i in data:
  if i=="L" and 1<=(x-1):
    x-=1
  elif i=="R" and (x+1)<=5:
    x+=1
  elif i=="U" and 1<=(y-1):
    y-=1
  elif i=="D" and (y+1)<=5:
    y+=1
print(y, x)