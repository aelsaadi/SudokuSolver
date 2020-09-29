# Ahmad Elsaadi

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

"Function to print out board with lines for better visuals"

def print_board(s):
    for i in range(len(s)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - -")
        for j in range(len(s[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(s[i][j])
            else:
                print(str(s[i][j]) + " ", end="")


"function that checks each row and coloumn and square to see if a number is possible in that spot"

def possible(y, x, n):
    global board
    for i in range(0, 9):  # checks row
        if board[y][i] == n:
            return False
    for i in range(0, 9):  # checks column
        if board[i][x] == n:
            return False
    box_x = (x // 3) * 3  # checks square
    box_y = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[box_y + i][box_x + j] == n:
                return False
    return True


"this function checks if a slot is empty and while using backtracking " 
" and recursion with the above function to solve the sudoku board"

def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print_board(board)


solve()
