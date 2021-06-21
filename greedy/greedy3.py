# 숫자 카드 게임 
# n x m 에서 하나의 행을 선택하여 가장 낮은 숫자중 가장 큰 숫자를 찾는 게임 

n, m = map(int, input('n, m의 값 공백을 이용해 입력 :').split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기 
  min_value = min(data)
  # 가장 작은 수 중에서 가장 큰 수 찾기 
  result = max(result, min_value)
  print('result: ',result)
print(result) 

