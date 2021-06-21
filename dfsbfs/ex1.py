stack = []

stack.append(5)
stack.append(4)
stack.append(4)
print(stack[::-1]) 

#큐를 쓰기위한 deque 라이브러리 사용 
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(6)
queue.popleft()
print(queue) 
queue.reverse()
print(queue)

  
def recursive_function(i):
    if i == 100:
      return
    print(i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)

recursive_function(5)

def factorial_iterative(n):
  result=1
  # 1부터 n까지의 수곱하기
  for i in range(1, n+1):
    result *= i
  return result

print(factorial_iterative(5))

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n-1)

print(factorial_recursive(6))
