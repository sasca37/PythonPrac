#heapq : heap 기능을 사용하기위해 heapq 라이브러리를 제공한다. 
#다익스트라 최단 경로 알고리즘을 포함한 다양한 알고리즘에서 우선순위 큐 구현시 사용한다.
#PriorityQueue 라이브러리도 있지만 heapq가 더빠르게 동작한다. 
# heapq.heappush(), heapq.heappop() 

import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입 
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) 

#결과 0~9 정렬 : 파이썬은 최소힙으로 구성되어서 넣었다 빼기만해도 NlogN의 시간복잡도로 오름차순 #정렬이 완료된다. 


# 파이썬은 최대 힙을 제공하지 않아서 원소의 부호를 임시로 변경하는 방식 사용 
# 원소 넣기 전에 반대로 넣고나서 원래대로 

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)   #내림차순 정렬완료 

