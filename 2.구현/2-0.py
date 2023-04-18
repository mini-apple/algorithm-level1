n = int(input())

count=0
h, m, s = 0, 0, 0

while True:
  if h==n and m==59 and s==59:
    break
  s+=1
  if s==60:
    s-=60
    m+=1
  if m==60:
    m-=60
    h+=1
  if "3" in str(h)+str(m)+str(s):
    count+=1
print(count)
  