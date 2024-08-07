def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    left = array[:midpoint]
    right = array[midpoint:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    # If the first array is empty, then
    # nothing needs to be merged, and you
    # can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty,
    # then nothing needs to be merged, and you
    # can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the
    # elements make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to
        # get the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


if __name__ == '__main__':
    # numbers = [19, 3, 4, 8, 10, 1, 2, 1, 20, 15, 7]
    numbers = [4, 3, 8, 1, 7]
    print(merge_sort(numbers))
