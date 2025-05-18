def knapsack(W, weights, values, n):
    # Create a 2D DP array with (n+1) rows and (W+1) columns
    # dp[i][w] will store the maximum value for first i items with capacity w
    dp = [[0 for x in range(W + 1)] for y in range(n + 1)]  # (a) n+1 rows for all items including 0

    # Loop through each item (including 0 for base case)
    for i in range(n + 1):  # (b) loop from 0 to n (including n)
        # Loop through all possible weights from 0 to W
        for w in range(W + 1):
            # Base case: if no items or capacity is 0, max value is 0
            if i == 0 or w == 0:
                dp[i][w] = 0
            # If weight of the current item is less than or equal to current capacity
            elif weights[i - 1] <= w:
                # Take max of including or excluding the current item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # (c) include current item's value + best of remaining capacity
                    dp[i - 1][w]  # exclude current item
                )
            else:
                # If current item can't fit, take value without it
                dp[i][w] = dp[i - 1][w]  # (d) value excluding current item

    # Return max value for n items with capacity W
    return dp[n][W]


# Example usage:
weights = [2, 3, 4, 5]        # Weights of items
values = [3, 4, 5, 6]         # Corresponding values of items
capacity = 5                  # Maximum weight capacity of knapsack
n = len(weights)              # Number of items

max_value = knapsack(capacity, weights, values, n)
print("Maximum value in Knapsack =", max_value)
