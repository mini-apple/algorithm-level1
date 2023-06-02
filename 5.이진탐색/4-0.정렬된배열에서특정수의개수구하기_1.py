from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

def countNum(left, right):
  left_idx = bisect_left(data, left)
  right_idx = bisect_right(data, right)
  return right_idx - left_idx

num = countNum(x, x)
if num == 0:
  print(-1)
else:
  print(num)