def digit(n):
   even = 0
   odd = 0
   while (n != 0):
       r = n % 10
       if r % 2 == 0:
          even = even + r
       else:
          odd = odd + r
       n //= 10

   return even - odd


n = 412
print(digit(int(n)))
