def re_function(i):
  # 100번째 출력시에 종료되도록 종료 명시 
  if i == 100:
    return 
  print(i)
  re_function(i+1)
re_function(1)