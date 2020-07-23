'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    largest_values = []
    start_index = 0
    last_index = k

    while last_index - 1 < len(nums):
        current_test_values = nums[start_index:last_index]
        largest_values.append(max(current_test_values))

        start_index += 1
        last_index += 1

    return largest_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
