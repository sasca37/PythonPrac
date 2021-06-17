# 큰 수의 법칙 93p -> 입력값이 커지면 시간초과 가능성이 있다. 

# N M K 를 공백으로 구분하여 입력받기 
n, m, k = map(int, input().split('/'))

# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split())) 

data.sort() # 입력받은 수 정렬 
first = data[n-1] #가장 큰수 
second = data[n-2] #두 번째로 큰 수 

result = 0 

while True: 
  for i in range(k): 
    if m == 0:  
      break
    result += first 
    m -=1
  if m == 0:
    break
  result += second
  m -= 1
print(result)   