n = 1260
count = 0

coin_types = [500, 100, 50 , 10]

for coin in coin_types:
  count += n 
  n %= coin
print(count) 
# 결과 1590 (1260 + 260 + 60 + 10)


# for coin in coin_types:
#   count = n // coin
#   print(count, end=' ')
#   n %= coin
#   print(n)

#결과  2 260 \n 2 60 \n 1 10 \n 1 0