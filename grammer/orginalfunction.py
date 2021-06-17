#기본 내장 함수 sum - list와 같은 iterable 객체 
result = sum([1,2,3,4,5])
print(result)

#2개 이상 파라미터가 들어 왔을 때 가장 작은 값을 반환 
result = min(7, 3, 5, 2)
print(result)

# 수학 수식이 문자열 형식으로 들어올 때 eval () 함수 사용 
result = eval("(3+5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result )

#두번 째 원소를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1],
reverse = True)
print(result)

#리스트와 같은 iterable 객체는 기본적으로 sort()함수 내장해서 사용 가능  
data = [9, 1, 8, 5, 4]
data.sort()
print(data)