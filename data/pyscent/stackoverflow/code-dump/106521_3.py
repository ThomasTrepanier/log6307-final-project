import re
from parsec import *

spaces = regex(r'\s*', re.MULTILINE)

@generate
def getHeader():
  s1 = yield string ("DateGroup") 
  s2 = ''.join( (yield many1(digit())))
  return (s1 + s2)

@generate
def getDataLine():
  s1 = yield digit()
  s2 = ''.join((yield many1 (none_of ("\r\n"))))
  yield spaces
  return (s1 + s2)

@generate
def getChunk():
  yield spaces
  header = yield getHeader
  yield spaces
  dataList = yield many1 (getDataLine)
  return (header,dataList)

@generate
def getData():
  yield spaces
  parsedData = yield many1(getChunk)
  yield eof()
  return parsedData

inputText = """DateGroup1
20191129
20191127
20191126
DateGroup2
20191129
20191127
20191126
DateGroup3
2019-12-02
DateGroup4
2019-11-27
DateGroup5
2019-11-27"""


result = getData.parse(inputText)
for p in result:
  print(p)
