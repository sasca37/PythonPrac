box = [[0 for j in range(11)] for i in range(11)] # 0~11  11개 생성 

# 입력 박스 생성 
for i in range(1,11):
  k = list(map(int, input().split()))
  for j in range(1,11):
    box[i][j] = k[j-1]
    
# 개미집 입력 
box[2][2] = 9
x,y=2
# 개미 이동 
while True:
  if(box[x][y+1] == 0):
    y+=1
    box[x][y+1] = 9
  elif(box[x][y+1] == 1 and box[x+1][y] ==0):
    x+=1
    box[x][y+1] = 9
  else:
    break

for i in range(1,11):  #[1][1] ~ [10][10] 까지
  for j in range(1,11):
    print(box[i][j], end=' ')
  print()

print('a')




a,b = map(int, input().split())
tt = [[0 for j in range(b+1)] for i in range(a+1)]

n = int(input())
for i in range(n):
  l,d,x,y = map(int, input().split())
  if(d == 0): #가로일 경우
    for i in range(l): 
      tt[x][y+i] = 1
  else :
    for i in range(l):
      tt[x+i][y] = 1
    
for i in range(1, a+1):
  for j in range(1, b+1):
    print(tt[i][j], end=' ')
  print()


#LIST COMPREHENSIONS
d= [[0 for j in range(20)] for i in range(20)]
# print(d)

n = int(input())
for i in range(n):
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end=' ')
  print()


n = int(input())
a = list(map(int, input().split()))
result = []
for i in range(n):
  result.append(a[i])
print(min(result))


# range를 이용한 역순 정렬 
n = int(input())
a = list(map(int, input().split()))
a_list = []
for i in range(n):
  a_list.append(a[i])
for i in range(n-1,-1,-1):
  print(a_list[i], end=' ')



n = int(input()) 
a = list(map(int,input().split()))
a_list = []
for i in range(n):
  a_list.append(a[i])
k = []
for i in range(24):
  k.append(0)
for i in range(n):
  k[a[i]] +=1
for i in range(1, 24):
  print(k[i], end=' ')

n = int(input()) 
a = input().split()

for i in range(n):
  a[i] = int(a[i])
print(a)   
d = [] 
for i in range(24) : 
  d.append(0) 
for i in range(n) :
  d[a[i]] += 1 
for i in range(1, 24) :
  print(d[i], end=' ')


n = int(input())
a=list(map(int, input().split()))
print(a)
a_list = []
for i in range(n):
  a_list.append(a[i])
print(a_list)
# call = [for i in range(n) input(i)]

a,b,c = map(int, input().split())
result = 1
while result %a!=0 or result%b !=0 or result%c !=0:
  result +=1
print(result)

a, m, d,n = map(int,input().split())
result = a
for i in range(0, n-1):
  result = result * m +d
print(result)

# a: 시작값 d:등차값 n 몇번째 수 
a, d, n = map(int,input().split())
# k = []
# for i in range(a,100,d):
#   k.append(i)
# print(k)
total = a
for i in range(0, n-1):
  total +=d
print(total)


# 8비트 -> 1바이트 , 1024바이트 -> 키로바이트 , 1024KB - 1MB 이므로 8 1024 1024 
a,b,c,d = map(int, input().split())
result = a * b * c * d /8 /1024/ 1024 
print('%.1f'%result,'MB')
r,g,b = map(int, input().split())
result =0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i,j,k)
      result+=1
print(result )

a = int(input())
for i in range(1,a+1):
  if(i%10==3):
    print('X', end=' ')
  elif(i%10==6):
    print('X', end=' ')
  elif(i%10==9):
    print('X', end=' ')
  else: print(i, end=' ')

a = int(input(), 16)
for i in range(1,16):
  print('%X'%a,'*%X'%i, '=%X'%(a*i), sep='')

a,b = map(int, input().split())
for i in range(a):
  for j in range(b):
    print(i+1,j+1)

n = int(input())
result = 0
i =0
while result<n:
  i+=1
  result+=i

print(i)


