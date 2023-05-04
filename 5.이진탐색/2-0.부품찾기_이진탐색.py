def binary_search(array, target, start, end):
  if start > end:
    print(target)
    return False
    
  mid = (start + end) // 2
  if array[mid] == target:
    return True
  elif array[mid] > target:
    end = mid - 1
    return binary_search(array, target, start, end)
  elif array[mid] < target:
    start = mid + 1
    return binary_search(array, target, start, end)

n = int(input())
product = list(map(int, input().split()))
product.sort()

m = int(input())
finding = list(map(int, input().split()))

result = []
for i in range(m):
  if binary_search(product, finding[i], 0, n-1):
    result.append("yes")
  else:
    result.append("no")

for i in result:
  print(i, end=" ")