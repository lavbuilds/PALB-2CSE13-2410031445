def min_length_subarray_sum(arr, x):
    n = len(arr)
    current_sum = 0
    start = 0
    min_length = float('inf')

    for end in range(n):
        current_sum += arr[end]

        # Shrink window while sum is greater than x
        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    if min_length == float('inf'):
        return 0

    return min_length