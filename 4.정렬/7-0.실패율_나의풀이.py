def solution(N, stages):
  answer = []
  data = [0] * (N+2)
  for i in stages:
      data[i] += 1
  
  result = []
  total = len(stages)
  for i in range(1, N+1):
      total -= data[i-1]
      if data[i] == 0:
          fail = 0
      else:
          fail = data[i] / total
      result.append((fail, i))
  result.sort(key = lambda x: (-float(x[0]), int(x[1])))
  
  for i in result:
      answer.append(i[1])
  return answer