# TO-DO: Complete the selection_sort() function below 
import random
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

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #BubbleLogic
    # Write an iterative loop starting at 0
    # Ending at the second last index
    # : because last index would have nothing to compare with anyway
    swap_counter = 1
    while(swap_counter):
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

myList = []
for i in range(0, 20):
    myList.append(random.randint(0, 20))
print(myList)

print(bubble_sort(myList))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr