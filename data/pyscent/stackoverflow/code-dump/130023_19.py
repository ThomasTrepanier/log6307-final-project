def listWithNumberOfStep(startNumber, endNumber, nbSteps):
   listNumber = []
   delta = endNumber - startNumber
   for i in range(nbSteps + 1):
      listNumber.append(startNumber + (delta/nbSteps * i))
   return listNumber
