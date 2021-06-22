
#a 부터 입력한 문자까지출력
n = ord(input())
a = ord('a')
while a<=n:
  print(chr(a), end=' ')
  a+=1


n = int(input())
while n!=0:
  print(n-1)
  n -=1

k = []
a,b,c = map(int, input().split())
k.extend([a,b,c])
print(k)

a, b = map(int, input().split())
print(a&b)

# 비트단위 ~n = -n-1
a = int(input())
print(~a)

a,b = map(int, input().split())
print(bool(a) and bool(b))

# 파이썬 0은 false 를 의미 
n = int(input())
print(not bool(n))


# a를 2^b배 만큼 곱한 값 
a,b = map(int, input().split())
print(a << b)

a = int(input())
print(a<<1)

a,b,c = map(int, input().split())
#print('%d %.2f ' %int((a+b+c)) %((a+b+c)/3))
print('%.2f' %((a+b+c)/3))


# 아스키 -> 다음문자 
a = ord(input())
b = chr(a+1)
print(b)

a = int(input())
print(-a)

# 정수 -> 아스키코드 
a = int(input())
n = chr(a)
print(n)

# 아스키 -> 정수 
a = input()
n = ord(a)
print(n)
