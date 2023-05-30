n = input()
sum1 = 0
sum2 = 0
for i in range(len(n)//2):
  sum1 += int(n[i])
  
for i in range(len(n)//2, len(n)):
  sum2 += int(n[i])

if sum1 == sum2:
  print("LUCKY")
else:
  print("READY")