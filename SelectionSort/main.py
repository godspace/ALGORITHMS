NumList = []
for line in open("Numbers.txt", "r").readlines():
    NumList.append(int(line.strip()))
#print NumList

def FindSmallest(arr):
  #print arr
  smallest = arr[0]
  smallest_index = 0
  for i in range(0, len(arr)):
    if arr[i]<smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index
  
def SelectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = FindSmallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr

SortList = SelectionSort(NumList)
#print (SortList)


def BinarySearch (list, item):
  low = 0
  high = len(list) - 1
  
  while low <= high:
    mid = (low + high)//2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

search_num = 380965488372
print (str("Index of searching number ") + str(search_num) + ": " + str(BinarySearch (SortList, search_num)))

  
