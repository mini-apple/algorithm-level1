# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0]*100

def fibo(x):
  if x==1 or x==2:
    return 1
  # 메모이제이션: 이미 계산한 적이 있다면 저장된 값을 가져온다
  if d[x] != 0:
    return d[x]
    
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))