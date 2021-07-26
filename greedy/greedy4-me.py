n, k = map(int, input().split())

count = n % k 
result = 0 
result += count

while True:
  if (n == 1) :
    break

  if(n < k):
    result = n-1
    break
  
  else :
    n /= k 
    result +=1

print(result)