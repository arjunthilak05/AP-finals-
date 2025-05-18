def insertion_sort(arr):
    # Insertion Sort is like sorting playing cards in your hand.
    # It builds the sorted array one element at a time by comparing and shifting.

    # Best Time Complexity: O(n) — when the array is already sorted.
    # Worst Time Complexity: O(n^2) — when the array is sorted in reverse.

    for i in range(1, len(arr)):
        key = arr[i]  # Current element to insert in sorted part
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1

        arr[j + 1] = key  # Place the key in the correct position

    return arr


def main_insertion():
    print("Enter 5 elements for the array:")
    arr = []
    for i in range(5):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)

    result = insertion_sort(arr)
    print("The sorted array using Insertion Sort is:", result)


if __name__ == "__main__":
    main_insertion()
