# TO-DO: Complete the selection_sort() function below 
import random
myList = []
for i in range(0, 20):
    myList.append(random.randint(0, 20))
print(myList, 'original list')

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i 
        # isn't the  current index the palcement in which the smallest index will
        # be put? 
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        while cur_index < len(arr):
            if(arr[smallest_index] > arr[cur_index]):
                smallest_index = cur_index
            cur_index += 1

        # TO-DO: swap
        cur_smol = arr[smallest_index]
        swap_me = arr[i]

        arr[smallest_index] = swap_me
        arr[i] = cur_smol

    return arr
print(selection_sort(myList), 'selection sorted list')
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #BubbleLogic
    # Write an iterative loop starting at 0
    # Ending at the second last index
    # : because last index would have nothing to compare with anyway
    swap_counter = 1
    while(swap_counter):
        #How do I calculate this in terms of Big(O)
        swap_counter = 0
        for i in range(0, len(arr)-1):
            if(arr[i] > arr[i + 1]):
                #SwapLogic
                cur_item = arr[i]
                swap_item = arr[i + 1]

                arr[i] = swap_item
                arr[i + 1] = cur_item

                swap_counter += 1

    return arr



print(bubble_sort(myList), 'bubble sorted list')


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    k = 0
    for i in arr:
        if(i > k):
            k = i
  
    occur = []
    for i in range(0, k + 1):
        occur.append(0)

    for i in arr:
        occur[i] += 1

    accumulation = []
    acc = 0

    for i in occur:
        acc += i
        accumulation.append(acc)

    shift = []
    shift.append(0)
    for i in range(0, len(accumulation) - 1):
        shift.append(accumulation[i])

    newList = []
    for i in arr:
        newList.append(0)

    for i in arr:
        newList[shift[i]] = i
        shift[i] += 1
    return newList

print(count_sort(myList), 'count sorted list')

#Count sort determines the number of objects with distinct values

#Then we do some arithmetic to dtermine the position of each object in the output sequence (On what basis?)