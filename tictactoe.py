from tkinter import *
import random

# Hàm kiểm tra trạng thái chiến thắng
def check_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Hàm kiểm tra trạng thái hòa
def is_full(board):
    for row in board:
        if '' in row:
            return False
    return True

# Hàm đánh giá trạng thái hiện tại

def evaluate(board):
    if check_winner(board, 'o'):
        return 1
    elif check_winner(board, 'x'):
        return -1
    else:
        return 0

# Thuật toán Minimax
def minimax(board, depth, is_maximizing):
    #check 0 thắng
    if check_winner(board, 'o'):
        return 1
    #check x thắnng
    if check_winner(board, 'x'):
        return -1
    #check hòa
    if is_full(board):
        return 0

    if is_maximizing:
        # Nếu là lượt đi của máy tính thì tìm giá trị lớn nhất
        # giá trị lớn nhất sẽ là giá trị tốt nhất cho máy tính
        # //cretae giá trị max_eval
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'o'
                    # //get giá trị đánh giá trạng thái hiện tại cua may tinh va lay do sau+1
                    # //create tree search
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = ''
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        # Nếu là lượt đi của người chơi thì tìm giá trị nhỏ nhất
        # giá trị nhỏ nhất sẽ là giá trị tốt nhất cho người chơi
         # //cretae giá trị min_eval
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'x'
                    # đánh giá trạng thái hiện tại
                     # //get giá trị đánh giá trạng thái hiện tại cua may tinh va lay do sau+1
                    # //create tree search
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = ''
                    min_eval = min(min_eval, eval)
        return min_eval

# Tìm nước đi tốt nhất cho máy tính
def find_best_move(board):
    # thiết lập giá trị ban đầu cho best_eval là giá trị tìm thấy đầu tiên sẽ được coi là tốt nhất.
    # thiết lập giá trị ban đầu cho best_move là (-1, -1) tức là nước đi tốt nhất chưa được tìm thấy.   
    best_eval = -float('inf')
    best_move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'o'
                eval = minimax(board, 0, False)
                board[row][col] = ''
                #kiểm tra xem giá trị tìm thấy có tốt hơn giá trị tốt nhất hiện tại hay không
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Hàm xử lý nước đi của người chơi
def player_move(row, col):
    global board, player
    #check xem nước đi có hợp lệ hay không
    if board[row][col] == '' and not check_winner(board, 'o') and not check_winner(board, 'x'):
        board[row][col] = player
        buttons[row][col]['text'] = player

        if player == 'x':
            player = 'o'
            label.config(text="Turn của người chơi 'o'")
            # Nếu người chơi là 'x' và chưa thắng hoặc chưa hòa thì máy tính sẽ đánh    
            if not check_winner(board, 'o') and not is_full(board):
                row, col = find_best_move(board)
                board[row][col] = player
                buttons[row][col]['text'] = player
                player = 'x'
                label.config(text="Turn của người chơi 'x'")

        if check_winner(board, 'o'):
            label.config(text="Người chơi 'o' thắng!")
        elif check_winner(board, 'x'):
            label.config(text="Người chơi 'x' thắng!")
        elif is_full(board):
            label.config(text="Trò chơi hòa!")

# Hàm bắt đầu trò chơi mới
def new_game():
    global board, player
    player = random.choice(['x', 'o'])
    label.config(text="Turn của người chơi '{}'".format(player))
    for row in range(3):
        for col in range(3):
            board[row][col] = ''
            buttons[row][col]['text'] = ''

window = Tk()
window.title("Caro")
board = [['', '', ''], ['', '', ''], ['', '', '']]
player = random.choice(['x', 'o'])
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text="Turn của người chơi '{}'".format(player), font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Ván mới", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                  command=lambda row=row, col=col: player_move(row, col))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()
