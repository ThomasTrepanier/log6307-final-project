def sorted_elements(numbers):
    return sorted(set(numbers))

testcase = int(input())
while testcase > 0:
   numbers = map(int, input().split())
   l = sorted_elements(numbers)

   for x in l:
      print (x, end = ' ')

   print ()
   testcase -= 1
