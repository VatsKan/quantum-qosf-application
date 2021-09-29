# Classical implementation

def convertIntListToBinList(listOfIntegers):
  binListOfIntegers = []
  numOfBits = 0
  for i in range(len(listOfIntegers)):
    binReprOfInt = bin(listOfIntegers[i])[2:]
    if len(binReprOfInt) > numOfBits:
      numOfBits = len(binReprOfInt)
    binListOfIntegers.insert(i, binReprOfInt)
  for i in range(len(binListOfIntegers)):
    binListOfIntegers[i] = binListOfIntegers[i].zfill(numOfBits)  
  return binListOfIntegers

def checkIfBinReprHasAlternatingIndices(binRepr):
  _11adjacency = binRepr.find('11')
  _00adjacency = binRepr.find('00')
  if(_11adjacency==-1 and _00adjacency==-1):
    return True
  else:
    return False

def getArrayIndicesOfAlternatingBinReps(listOfBinaryStrings):
  indicesOfAlternatingBinReps = []
  for i in range(len(listOfBinaryStrings)):
    binStr = listOfBinaryStrings[i]
    if checkIfBinReprHasAlternatingIndices(binStr):
      indicesOfAlternatingBinReps.append(i)
  return indicesOfAlternatingBinReps

def mapDecimalIndicesToQubitSuperposition(indicesOfAlternatingBinReps):
  indicesBinRepList = convertIntListToBinList(indicesOfAlternatingBinReps)
  sumStr = ''
  for qubitState in indicesBinRepList:
    sumStr += '+|' + qubitState + '>'
  sumStr = sumStr.strip('+')
  superposition = '1/sqrt(' + str(len(indicesBinRepList)) + ')(' + sumStr + ')' 
  return superposition

def task1(listOfIntegers):
  binList = convertIntListToBinList(listOfIntegers)
  indicesOfAlternatingBinReps = getArrayIndicesOfAlternatingBinReps(binList)
  return mapDecimalIndicesToQubitSuperposition(indicesOfAlternatingBinReps)

print(task1([1,5,7,10]))

    

