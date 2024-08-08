# Time Complexity: O(n^2)
def bubble_sort(array):
    n = len(array)

    # range(1, n) will start
    # from 1 and end at n - 1
    for i in range(1, n):
        already_sorted = True

        # range(n - i) will start
        # from 0 and stop at n - i - 1
        for j in range(n - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array


if __name__ == '__main__':
    numbers = [3, 4, 8, 10, 1, 2, 1, 20, 15, 7]
    print(bubble_sort(numbers))
