# 열 행 구조 
n = input()
x = n[1]
y = int(ord(n[0])) - int(ord('a')) +1
print(x,y)
count = 0
#열행
dy = ['a','b','c','d','e','f','g','h']
dx = [1,2,3,4,5,6,7,8]

# 나이트 구조 경우의수 총 8개
# y+1,x+2 or y+2,x+1 or y+2 x-1 or y+1 x-2
# y-1 x+2 or y-2 x+1 or y-1 x-2 or y-2 x-1 

# ex) c2 일때 6 가지 


