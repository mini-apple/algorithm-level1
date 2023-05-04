def parametric_search(data, target, start, end):
  rest = 0
  mid = (start + end) // 2
  for i in data:
    if i > mid:
      rest += i-mid
  if rest == target:
    return mid
  elif rest < target:
    return parametric_search(data, target, start, mid-1)
  elif rest > target:
    return parametric_search(data, target, mid+1, end)  

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = parametric_search(data, m, data[0], data[-1])
print(result)