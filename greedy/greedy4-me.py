n,k = map(int, input().split())

count = 0

while True:
  if (n == 1):
    break

  elif((n % k) != 0):
    while ((n%k)!=0):
      n -= 1 
      count += 1
      if(n == 1):
        break
  else :
    while (n!=1):
      n /= k
      count += 1 
      break

print(count)