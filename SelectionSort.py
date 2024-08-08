def selection_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        cur_min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j

        swap(arr, cur_min_idx, i)


def swap(arr, cur_min_idx, i):
    arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]


numbers = [2, 6, 5, 1, 2, 3, 4]
selection_sort(numbers)
print(numbers)
