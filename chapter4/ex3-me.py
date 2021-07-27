# 열 행 구조 
n = input()
x = int(n[1])
y = int(ord(n[0])) - int(ord('a')) +1
count = 0
#열행
dx = [+2,-2,+1,-1,+2,-2,-1,+1]
dy = [+1,+1,+2,+2,-1,-1,-2,-2]

# 나이트 구조 경우의수 총 8개
# y+1,x+2 or y+2,x+1 or y+2 x-1 or y+1 x-2
# y-1 x+2 or y-2 x+1 or y-1 x-2 or y-2 x-1 

# ex) c2 일때 6 가지 
for i in range(len(dx)):
  xx = x + dx[i]
  yy = y + dy[i]
  print(xx,yy)
  if(xx <1 or xx >8 or yy < 1 or yy > 8):
    continue    
  count +=1 

print(count)



