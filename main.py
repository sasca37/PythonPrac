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
