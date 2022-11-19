#Lab7
def bubbleSort(arr):
    
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        value = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = value

def selection_sort(arr):
    
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)-1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        
def insertion_sort(arr):

    for index in range(1, len(arr)):
        currentValue = arr[index]
        currentPosition = index

        while currentPosition > 0 and arr[currentPosition - 1] > currentValue:
            arr[currentPosition] = arr[currentPosition -1]
            currentPosition = currentPosition - 1

        arr[currentPosition] = currentValue

print("array")
arr = [11, 4, 7, 5, 9, 13, ]
print(arr)

bubbleSort(arr)
selection_sort(arr)
insertion_sort(arr)


print("\nbubbleSort array:" + str(arr)) 
print("\nselectionSort array :" + str(arr))
print("\ninsertionSort array: " + str(arr))

#2.2.1 From all above method which one is the best in term of performance?
    #Selection Sort
    
#2.2.2 From all above method which one is the best in term of resource management?
    #Bubble Sort
    
#2.2.3 From all above method which one is the best in your opinion?
    #Bubble Sort

