def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]  # swap


numbers = [2, 6, 5, 1, 2, 3, 4]
selection_sort(numbers)
print(numbers)
