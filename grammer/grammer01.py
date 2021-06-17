a = 100
print(a)

b = 1e9
print(b)

a2 = 0.3 + 0.6 
print(round(a2,4))
if round(a2,4) == 0.9:
  print(True)
else:
  print(False)

a3 = 7
b3 = 3

print(a3 / b3)
print(a3 % b3)
print(a3 // b3)

a4 = 5
b4 = 3
print(a4 ** b4)

#리스트
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[4])

#빈리스트 생성
a = list()
print(a)

#크기가 N이고 모든 값이 0인 1차원 리스트 초기화 
n = 10
a = [0] * n
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])
print(a[-3])
a[3] = 7
print(a)

#리스트 컴프리헨션 ( [] 안에 조건문과 반복문을 넣는 방식 )
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [ i * i for i in range(1, 10)]
print(array)

#n x m 크기의 2차원 리스트 초기화 
n = 3
m = 4 
array = [ [0] * m for _ in range(n)]
print(array)

a = [ 1, 4, 3]
print("기본 리스트 : ", a);

a.append(2)
print("삽입 : ", a)
a.sort()
print("오름차순 : ",a)
a.sort(reverse = True)
print("내림차순 : ",a)
# 리스트 원소 뒤집기 
a.reverse()
print("원소 뒤집기 :",a)

#특정 인덱스에 데이터 추가 
a.insert(2, 3)
print("인덱스 2에 3 추가", a)

#특정 값 데이터 삭제
a.remove(1)
print("값 1 삭제 : ",a)

a = [1,2,3,4,5,5,5]
remove_set = {3, 5}
#remove_set 에 포함되지 않은 값만을 저장 (not in 사용 removeall 제공하지않음)
result = [ i for i in a if i not in remove_set]
print(result)

#문자열 초기화 
data = 'Hello world'
print(data)

data = "Don't you know \"Python\"?"
print(data)

#문자열 연산 
a = "Hello"
b = "World"
print(a + " " + b)
a = "String"
print(a*3)

#튜플() : (선언 후 값 변경 x , 소괄호 사용 ) - 다익스트라 최단 경로에 우선순위 큐에 사용 
a = (1, 2, 3, 4)
print(a)

#딕셔너리 : 키-값 쌍으로 구성 
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

if '사과' in data :
  print("'사과'를 키로 가지는 데이터가 있습니다.")

#키 데이터만 담은 리스트
#key_list = list(data.keys())
key_list = data.keys()
#값 데이터만 담은 리스트 
value_list = data.values()
print(key_list)
print(value_list) 

#각 키에 따른 값을 하나씩 출력 
for key in key_list :
  print(data[key])

#set(집합) 자료형 - 중복 x , 순서x
data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,5,5}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a | b) #합집합 
print(a & b) #교집합
print(a - b) #차집합

data = set([1,2,3])
print(data)

data.add(4)
print(data)

#새로운 원소 여러개 추가
data.update([5,6])
print(data)

data.remove(3)
print(data)

#조건문 
x = 15
if x >= 10:
  print(x)

score = 85
result = "a"
if score >= 80: result = "Success"
print(result)
result = "Suc" if score>=80 else "Fail"
print(result)

a = [1,2,3,4,5,5,5]
remove_set = {3, 5}

result = []
for i in a:
  if i not in remove_set:
    result.append(i)

print(result)

a = [1,2,3,4,5,5,5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)