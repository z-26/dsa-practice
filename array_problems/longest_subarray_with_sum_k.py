def longest_subarray_with_sum_k(arr, k):
    prefix_sum = {}
    current_sum = 0
    max_length = 0

    for i, num in enumerate(arr):
        current_sum += num

        # Check if the entire subarray from the start has the sum k
        if current_sum == k:
            max_length = i + 1

        # Check if (current_sum - k) exists in the map
        if (current_sum - k) in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])

        # Store the current sum in the map if it is not already present
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return max_length

arr = [1, 2, 3, 7, 5]
k = 12
print(longest_subarray_with_sum_k(arr, k))