'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here

    new_arr = []
    sum_total = arr[1]
    next_index = 1

    while len(new_arr) < len(arr):
        if len(arr) > 2:
            for num in arr[2:]:
                sum_total *= num
            new_arr.append(sum_total)
            removed = arr.pop(next_index)
            arr.insert(0, removed)
            removed = arr.pop(next_index)
            arr.append(removed)
            sum_total = arr[1]
        elif len(arr) == 2:
            sum_total = arr[1] * 1
            new_arr.append(sum_total)
            removed = arr.pop(next_index)
            arr.insert(0, removed)
            sum_total = arr[1]
        else:
            return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
