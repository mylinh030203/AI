# Hàm kiểm tra xem bảng cờ đã kết thúc hay chưa
def is_game_over(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return True

    for col in range(3):
        if len(set(board[row][col] for row in range(3))) == 1 and board[0][col] != ' ':
            return True

    if len(set(board[i][i] for i in range(3))) == 1 and board[0][0] != ' ':
        return True

    if len(set(board[i][2 - i] for i in range(3))) == 1 and board[0][2] != ' ':
        return True

    return all(cell != ' ' for row in board for cell in row)

# Hàm hiển thị bảng cờ
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

# Hàm đánh giá điểm cho bảng cờ
def evaluate(board):
    for row in board:
        if row.count('X') == 3:
            return 1
        elif row.count('O') == 3:
            return -1

    for col in range(3):
        if [board[row][col] for row in range(3)].count('X') == 3:
            return 1
        elif [board[row][col] for row in range(3)].count('O') == 3:
            return -12
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1:
        return score

    if score == -1:
        return score

    if is_game_over(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Hàm tìm nước đi tốt nhất cho máy tính
def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Hàm chơi Tic Tac Toe
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False

    while not game_over:
        print_board(board)

        # Người chơi
        row = int(input("Nhập số hàng (0, 1, 2): "))
        col = int(input("Nhập số cột (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            print("Ô này đã được chọn. Chọn ô khác.")
            continue

        # Kiểm tra kết thúc trò chơi
        if is_game_over(board):
            print_board(board)
            print("Người chơi thắng!")
            break

        # Máy tính
        print("Đến lượt máy tính...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'

        # Kiểm tra kết thúc trò chơi
        if is_game_over(board):
            print_board(board)
            print("Máy tính thắng!")
            break

    print("Trò chơi kết thúc.")

# Chơi Tic Tac Toe
play_tic_tac_toe()
