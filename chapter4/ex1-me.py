n = int(input())
data = list(input().split())
x,y = 1,1
#L(0,-1) R(0,+1) U(-1,0) D(+1,0)
routin = ['L', 'R', 'U', 'D']
ax = [0,0,-1,+1]
ay = [-1,+1,0,0]

for i in range(len(data)):
 for j in range(len(routin)):
   if(data[i] == routin[j]):
     x += ax[j]
     if(x < 1 or x > n):
       x-= ax[j]
     y += ay[j]
     if(y <1 or y > n):
       y-= ay[j]
print(x, y) 
