'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    checked_index = 0
    while checked_index < len(arr):
        removed = arr.pop(arr[checked_index])
        if removed in arr:
            arr.insert(checked_index, removed)
            checked_index += 1
        else:
            return removed


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

# print(single_number([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))