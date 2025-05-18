def minimax(is_maximizing):
    # Base case: check for winner or draw
    winner = check_winner()
    if winner == 'X':
        return 1  # AI wins
    elif winner == 'O':
        return -1  # Opponent wins
    elif is_full():
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf  # Maximize the score
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  # Try empty cells
                    board[i][j] = 'X'  # AI tries a move
                    score = minimax(False)  # Recur as opponent
                    board[i][j] = ' '  # 🔁 Backtrack (undo move)
                    best_score = max(score, best_score)  # Track best score
        return best_score

    else:
        best_score = math.inf  # Minimize the score
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  # Try empty cells
                    board[i][j] = 'O'  # Opponent tries a move
                    score = minimax(True)  # Recur as AI
                    board[i][j] = ' '  # 🔁 Backtrack (undo move)
                    best_score = min(score, best_score)  # Track worst score for AI
        return best_score


def best_move():
    best_score = -math.inf
    move = (-1, -1)  # Default invalid move

    # Check every cell to find best move for AI
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  # Try move
                score = minimax(False)  # See result after opponent plays
                board[i][j] = ' '  # 🔁 Backtrack

                if score > best_score:
                    best_score = score  # Keep best score
                    move = (i, j)  # Store best move

    return move
