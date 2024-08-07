def mergeSort(array):
    if len(array) <= 1:
        return

    midpoint = len(array) // 2
    left = array[:midpoint]
    right = array[midpoint:]

    mergeSort(left)
    mergeSort(right)

    # merge

    i = 0   # left array index
    j = 0   # right array index
    k = 0   # merged array index

    # Until we reach either end of either left or right,
    # pick larger among elements left and right and place
    # them in the correct position at A[p..midpoint]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    # When we run out of elements in either left or right,
    # pick up the remaining elements and put in A[p..midpoint]
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


# Driver program
if __name__ == '__main__':
    numbers = [6, 5, 12, 5, 10, 9, 1]

    mergeSort(numbers)

    print(numbers)
