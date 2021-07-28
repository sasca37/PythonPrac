n,m = map(int, input().split())
x,y,direction = map(int, input().split())
a=[]
for i in range(m):
  a.append(list(map(int,input().split())))

a[x][y] = 1
count = 1
turn_time = 0
# 방향 지정 (반시계)
while True:
  direction -= 1 
  if direction == -1 :
    direction = 3
  turn_time +=1
  # 북 동 남 서 
  dx = [-1,0,1,0]
  dy = [0,1,0,-1]
  xx = x + dx[direction]
  yy = y + dy[direction]
  if(a[xx][yy] == 0):
    turn_time = 0
    count+=1
    x = xx 
    y = yy 
    a[x][y]=1
    continue
  if(turn_time == 4) :
    xx = x - dx[direction]
    yy = y - dy[direction]
    if(a[xx][yy] == 1):
      break
    x = xx
    y = yy 
    a[x][y]=1
    count+=1
    turn_time =0

print(count) 