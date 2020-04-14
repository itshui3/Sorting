# TO-DO: complete the helpe function below to merge 2 sorted arrays

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

print(merge([1, 2], [5, 8]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Recurse Case : Continue to break up pieces into halves until each list only has 1 component item
    indie = []
    for i in arr:
        indie.append([i])
    # How do lists point to one anotehr for sorting? 
    
    # How do I track the 
    return arr


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
