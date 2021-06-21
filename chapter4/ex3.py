#ord : 아스키코드 숫자변환, 입력값 좌표화 

# 나이트 입력위치 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
print(row,",",column)

#나이트 이동 방향 
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2,1)]

# 8가지 방향 이동 가능 여부 확인 
result = 0
for step in steps:
  # 이동 위치 확인
  next_row = row+step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <=8 and next_column >=1 and next_column<=8:
    result += 1

print(result)