# Time complexity O(n^2)
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        value = A[i]
        hole = i
        while hole > 0 and A[hole - 1] > value:
            A[hole] = A[hole - 1]
            hole = hole - 1
        A[hole] = value


numbers = [2, 6, 5, 1, 2, 3, 4]
insertion_sort(numbers)
print(numbers)
