#n, m 공백 구분해서 일력받기 
n, m = map(int, input().split())

# 방문한 위치 저장을 위한 맵 생성 후 0 으로 초기화 
d = [[0] * m for _ in range(n)]
print(d)

#현재 캐릭터의 x , y좌표 방향 입력받기 
x, y, direction =  map(int, input().split())
d[x][y] = 1 #현재 좌표 방문처리 

# 전체 맵정보 입력받기 
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

print(array)
# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0 , 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 시물레이션 시작
count = 1
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  #회전 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우 
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dx[direction]

    #뒤로 갈 수 있다면 이동
    if array[nx][ny] == 0:
      x = nx
      y = ny
    
    # 뒤로 바다가 막혀있는 경우
    else:
      break
    turn_time = 0

print(count)