def __removeElementsFromList(elementsList, elemetsToRemove):
  """Modify elementsList removing the elements found in elemetsToRemove.
     If there is an element in elemetsToRemove which does not belong to
     elementsList, that element will be ignored.
  """
  for ch in elemetsToRemove:
    if ch in elementsList:
      elementsList.remove(ch)

def numberOfCharsToBeChangedForHalfAnagram(strParam: str) -> int:
  """Split the string in two parts of equal size and return the number
     or characters that need to be changed in order to have the first half
     of the string the anagram of the second half. Returns -1 if this operation
     cannot be done (string with an odd number of characters).
  """
  strLen = len(strParam)
  
  if strLen % 2 != 0:
    return -1

  halfLen = strLen // 2
  firstCharList  = list(strParam[:halfLen])
  secondCharList = list(strParam[halfLen:])

  __removeElementsFromList(elementsList    = firstCharList,
                         elemetsToRemove = secondCharList)
  numberOfCharsToBeChanged = len(firstCharList)
  
  return numberOfCharsToBeChanged

if __name__ == "__main__":
  print(numberOfCharsToBeChangedForHalfAnagram(input()))