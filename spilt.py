# Example array
arr = [1, 2, 3, 4, 5]

# Enter the position at which you want to split the array
split_position = int(input("Enter the position at which to split the array: "))

if split_position >= 0 and split_position < len(arr):
    # Split the array into two parts
    first_part = arr[:split_position]
    second_part = arr[split_position:]

    # Concatenate the parts in reverse order
    result_arr = second_part + first_part

    # Print the result
    print("Original Array:", arr)
    print("Result Array:", result_arr)
else:
    print("Invalid split position.")
