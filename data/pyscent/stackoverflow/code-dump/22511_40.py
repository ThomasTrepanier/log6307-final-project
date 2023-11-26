def listOfLists(n):
   if n:
     yield []
     yield from listOfLists(n-1)

print(list(listOfLists(4)))
