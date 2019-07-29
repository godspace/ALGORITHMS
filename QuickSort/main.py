file = open('Sort_num.txt','w')
count = 0
NumList = []
for line in open("Telephone_num.txt").readlines():
  NumList.append(int(line))

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)

NewArr = quicksort(NumList)
for i in NewArr:
  file.write(str(i))
  file.write('\n')
file.close()
