# 이진탐색을 쉽게 구현할 수 있는 bisect 라이브러리 제공 
# 정렬된 배열에서 특정 원소 찾기에 매우 효과적 
# bisect_left() , bisect_right() 중요, 시간복잡도 : O(logN)에 동작 
# left(a,x) 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드 

from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

#left, right 함수들은 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할때도 효율적

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

#리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4 , 8, 9]
#값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))