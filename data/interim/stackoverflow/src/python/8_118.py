import itertools #Generates all permutations
import sys       #Allows us to get the current module

#Returns the index of the actionList we should execute
def evaluateActionIndex(varList): 
    allcombinations = itertools.product([False, True], repeat=len(varList))
    i = 0
    for subset in allcombinations: #for each of the possible combinations...
        if list(subset) == varList: #Check to see if we want to execute this index.
            return i
        i = i + 1                  #Increment the target index
    return -1                      #Execute default method (-1 index)

def performAction(index):
    actionList = [action1.__name__, action2.__name__, action3.__name__, action4.__name__, 
                  action5.__name__, action6.__name__, action7.__name__, action8.__name__,
                  action9.__name__, action10.__name__, action11.__name__, action12.__name__,
                  action13.__name__, action14.__name__, action15.__name__, action16.__name__,
                  actionDefault.__name__]
    method = getattr(sys.modules[__name__], actionList[index])  #Get method by name
    method()                                                    #Execute Method
