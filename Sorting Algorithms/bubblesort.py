def bubble_sort(arr):
    # It repeatedly steps through the list, compares adjacent elements
    # and swaps them if they are in the wrong order.
    # Best Case Time Complexity: O(n) — when the array is already sorted.
    # Worst Case Time Complexity: O(n^2) — when the array is sorted in reverse.

    n = len(arr)  # Get the length of the array

    # Outer loop for each pass
    for i in range(n):
        # Inner loop for comparing adjacent elements
        # Reduce the range by i because the last i elements are already sorted
        for j in range(0, n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr  # Return the sorted array

# Define the main function to take input and display output
def main():
    print("Enter 5 elements for the array:")
    arr = []

    # Take 5 integer inputs from the user and store them in a list
    for i in range(5):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)

    # Call the bubble_sort function to sort the list
    result = bubble_sort(arr)

    # Print the sorted list
    print("The sorted array is:", result)

# Run the main function if this file is executed
if __name__ == "__main__":
    main()
