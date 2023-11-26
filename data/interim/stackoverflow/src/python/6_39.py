def checkRange(number):

   count = 0
   while int(number):
      number /= 10
      count += 1

   round_off = count - 1
   for i in range(count - round_off):
      number *= 10

   number = int(number)

   return int((10**(count - 1)) * (number))
