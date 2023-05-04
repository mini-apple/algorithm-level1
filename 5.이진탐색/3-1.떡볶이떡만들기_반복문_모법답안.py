n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)  # 전체 array를 정렬할 필요는 없다. 최댓값만 알면 됨

result = 0
# 이진탐색, start가 end 보다 크면 탐색이 끝났다.
while start <= end:
  total = 0  # 잘린 떡의 길이
  mid = (start + end) // 2
  # 잘린 떡의 길이 구하기
  for x in array:
    if x > mid:
      total += x - mid

  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total < m:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid  # 최대한 덜 잘랐을 때가 정답이므로 여기에 result 기록
    start = mid + 1
  print(start, end)

print(result)