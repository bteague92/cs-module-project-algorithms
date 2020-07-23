'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    current_index = 0
    last_index = len(arr) - 1

    while current_index < last_index:
        if arr[last_index] == 0:
            last_index -= 1
        if arr[current_index] != 0:
            current_index += 1
        else:
            removed = arr.pop(current_index)
            arr.insert(last_index, removed)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# print(moving_zeroes([0, 0, 0, 0, 3, 2, 1]))