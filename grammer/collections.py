# 유용한 자료구조 라이브러리지원 collections
# deque, Counter 2가지 자주 쓰인다. 

from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


from collections import Counter
counter = Counter(['red', 'blue', 'red','green', 'blue' ,'blue'])
print((counter['blue'])) #blue가 등장한 횟수
print((counter['green']))
print((counter['green']))
print(dict(counter)) #사전자료형으로 변환

