''' python programmme for array rotation '''
# Example array
arr = [1, 2, 3, 4, 5]

if len(arr) <= 1:
    # No rotation needed for arrays with 0 or 1 element
    print(arr)
else:
    # Save the first element
    first_element = arr[0]

    # Shift all elements to the left by one position
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    # Place the first element at the end
    arr[-1] = first_element

    # Print the rotated array
    print(arr)
