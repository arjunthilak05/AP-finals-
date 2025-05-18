def rod_cutting(n, prices):
    # Create DP table S with (length of prices + 1) rows and (n + 1) columns
    # S[i][j] represents the maximum profit using pieces up to length i for rod length j
    S = [[0] * (n + 1) for _ in range(len(prices) + 1)]

    # Fill the DP table
    for i in range(1, len(prices) + 1):  # For each piece length i (1 to length of prices)
        for j in range(n + 1):           # For each rod length j (0 to n)
            if i <= j:
                # Max of:
                # 1) Not taking piece i (value from previous row)
                # 2) Taking piece i (price[i-1]) + value of remaining rod length (j - i)
                S[i][j] = max(S[i - 1][j], prices[i - 1] + S[i][j - i])
            else:
                # Cannot take piece i because it is longer than rod length j
                S[i][j] = S[i - 1][j]

    # Maximum profit is at bottom right corner of the DP table
    max_value = S[len(prices)][n]

    # To find which pieces were taken, backtrack through the table
    pieces = []
    col = n
    row = len(prices)

    while col > 0 and row > 0:
        # If value comes from the row above, piece not taken
        if S[row][col] == S[row - 1][col]:
            row -= 1
        else:
            # Piece was taken, add piece length
            pieces.append(row)
            col -= row  # Reduce rod length by piece length

    return max_value, pieces


def main():
    n = 6
    prices = [0, 2, 5, 7, 3, 9]  # Prices for pieces of length 1 to 6
    max_profit, taken_pieces = rod_cutting(n, prices)

    print("The maximum value is", max_profit)
    print("Pieces to take are:", taken_pieces)


if __name__ == "__main__":
    main()
