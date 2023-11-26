import os
def getAlldirInDiGui(path,resultList):
    filesList=os.listdir(path)
    for fileName in filesList:
        fileAbpath=os.path.join(path,fileName)
        if os.path.isdir(fileAbpath):
            getAlldirInDiGui(fileAbpath,resultList)
        else:
            if fileName=='tv.sas7bdat':
                resultList.append(fileAbpath)
resultList = []
PATH = ""
getAlldirInDiGui(PATH,resultList)
