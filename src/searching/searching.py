def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    startIdx = 0
    stopIdx = len(arr) - 1
    while startIdx <= stopIdx:
        centerIdx = startIdx + (stopIdx - startIdx) // 2
        centerVal = arr[centerIdx]
        if target == centerVal:
            return centerIdx
        elif target > centerVal:
            startIdx = centerIdx + 1
        else:
            stopIdx = centerIdx - 1 
    return -1  # not found