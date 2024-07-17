# Time Complexity: O(n^2)
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

    return array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [3, 4, 8, 10, 1, 2, 1, 20, 15, 7]
    print(bubble_sort(numbers))
