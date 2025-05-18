def selection_sort(arr):
    # Selection Sort selects the minimum element and puts it in the correct position
    # It repeatedly selects the smallest remaining element and swaps it to the front.

    # Best & Worst Time Complexity: O(n^2) — regardless of the initial order.

    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current index is the smallest

        # Find the actual smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update index of the smallest element

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main_selection():
    print("Enter 5 elements for the array:")
    arr = []
    for i in range(5):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)

    result = selection_sort(arr)
    print("The sorted array using Selection Sort is:", result)


if __name__ == "__main__":
    main_selection()
