import time
n, k = map(int, input().split())

start_time = time.time()
result = 0

# if (n >= k) :
#   while(True):
#     if (n == 1):
#       break
#     elif (n % k == 0):
#       n = n / k
#       result += 1
#     else :
#       n -= 1
#       result +=1
# else :
#   while(n != 1):
#     n-=1
#     result+=1
while True:
  # (n == k 로 나누어 떨어지는 수가 될때까지 1씩 빼기)
  target = (n // k ) * k
  result += (n - target)
  n = target 

  if n < k :
    break
  result += 1
  n //= k

result += (n - 1)
print(result)
end_time = time.time()
print('소요시간 : ', end_time - start_time)