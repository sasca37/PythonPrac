# while
i = 1
result  = 0 
while  i <= 9:
  result += i
  i += 1
print(result)

i = 1
result = 0
while i<=9:
  if i %2 ==1:
    result += i
  i += 1
print(result)

result = 0
for i in range(1,11):
  result += i
print(result)

#for i in range(2, 10):
  #for j in range(1, 10):
    #print(i, "X",j, "=", i * j, end="")

print()
def add(a, b):
  return a + b
print(add(3,6))

#함수 밖 데이터 변경시 global 사용 
a = 0

def func():
  global a
  a += 1

for i in range(10):
  func()
print(a)

#파이썬 람다식 
def add (a, b):
  return a+b

print((lambda a,b: a+b)(3,7))

# 입출력 
#n = int(input())
# 각 데이터를 공백으로 구분하여 입력 
#data = list(map(int, input().split()))

#data.sort(reverse = True)
#print(data)

#n, m, k를 공백으로 구분하여 입력  
#n, m, k = map(int, input().split())
#print(n, m, k)

#import sys
#sys.stdin.readline().rstrip()

#data = sys.stdin.readline().rstrip()
#print(data)

#출력할변수등
answer = 7 
print("정답은" + str(answer)+ "입니다")

# 파이썬 3.6이상 
answer = 7
print(f"정답은 {answer}입니다.")