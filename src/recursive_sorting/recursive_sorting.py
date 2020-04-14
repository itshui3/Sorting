# TO-DO: complete the helpe function below to merge 2 sorted arrays
import random
#Expects 2 sorted sub-lists as resources to produced a single merged and sorted list
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    # Iteratively pick out the smaller of the two leftmost values in the two given lists to populate a third return arr
    while(len(merged_arr) < elements):
        if(not len(arrA)):
            merged_arr.append(arrB.pop(0))
            continue
        if(not len(arrB)):
            merged_arr.append(arrA.pop(0))
            continue

        if(arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
myList = []
for i in range(0, 10):
    myList.append(random.randint(0, 10))
print(myList)

def merge_sort( arr ):
    # TO-DO
    arrA = []
    arrB = []

    if(len(arr) > 1):
        mid = len(arr) // 2
        arrA = arr[:mid]
        arrB = arr[mid:]
    else:
        return arr

    # if arrA or arrB has a length greater than 1, recurse merge_sort
    if(len(arrA) > 1):
        arrA = merge_sort(arrA)
    if(len(arrB) > 1):
        arrB = merge_sort(arrB)

    # The return of merge sort will necessarily be the calling of merge, which sorts
    return merge(arrA, arrB)
myList = []
for i in range(0, 10):
    myList.append(random.randint(0, 10))

print(merge_sort(myList))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
