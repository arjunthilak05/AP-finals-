def binary_search_recursive(arr, target, left, right):
    """
    Binary Search (Recursive): Keep dividing the array recursively.
    """
    if left > right:
        return -1  # Base case: Not found

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
arr = [10, 20, 30, 40, 50]
target = 50
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print("Binary Search (Recursive) Result:", result)
