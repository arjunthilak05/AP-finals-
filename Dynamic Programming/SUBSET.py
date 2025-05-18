def subset_sum(arr, target_sum):
    n = len(arr)
    
    # Create a DP table with n rows and (target_sum + 1) columns
    dp = [[False] * (target_sum + 1) for _ in range(n)]
    
    # Base case: sum = 0 is always True (using empty subset)
    for i in range(n):
        dp[i][0] = True
    
    # First row handling: if first number <= target_sum
    if arr[0] <= target_sum:
        dp[0][arr[0]] = True
    
    # Fill the rest of the DP table
    for i in range(1, n):
        for j in range(1, target_sum + 1):
            if j < arr[i]:
                # If current number is greater than current sum, copy from above
                dp[i][j] = dp[i - 1][j]
            else:
                # Else, check both options: exclude or include the number
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]
    
    # Print the DP table
    print("DP Table:")
    for row in dp:
        print(row)
    
    # Final answer is in bottom-right cell
    return dp[n - 1][target_sum]

# Example test
arr = [0, 5, 2, 1, 2]
target_sum = 9
result = subset_sum(arr, target_sum)
print("\nSum exists:", result)
