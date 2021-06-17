#itertools 라이브러리 - 반복되는 데이터를 처리하는 라이브러리 
#코테에서 가장 유용한 클래스는 permutations, combinations

#permutations: iterable 객체에서 r개의 데이터를 뽑아 나열하는 모든 경우 계산 
from itertools import permutations 
data = ['A', 'B', 'C'] # 데이터 준비 
result = list(permutations(data, 3)) #모든 순열 구하기 
print(result)
# 결과 : ABC ACB BAC BCA CAB CBA

#combinations : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 경우 계산 
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
# 결과 : AB AC BC

#product : permutations와 동일하나 원소를 중복하여 뽑는다. 
#prdocut 객체를 초기화 할때는 뽑고자하는 데이터수를 repeat 속성값으로 넣어준다. 

from itertools import product
data = ['A', 'B', 'C'] 
result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기 (중복허용)
print(result) 
# 결과 : AA AB AC BA BB BC CA CB CC 

#combinations_with_replacement : combinations에서 원소를 중복해서 뽑는 기능 추가 
#클래스이므로 객체 초기화 이후에는 리스트 자료형으로 반환하여 사용해야 한다. 

from itertools import combinations_with_replacement
data = ['A', 'B', 'C'] 
result = list(combinations_with_replacement(data, 2)) #2개를 뽑는 모든 조합 구하기 중복허용
print(result) 

# 결과 : AA AB AC BB BC CC 

