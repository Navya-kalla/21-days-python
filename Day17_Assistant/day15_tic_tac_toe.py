def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, current_player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        if all(board[i] == current_player for i in condition):
            return True

    return False

def draw(board):
    for i in board:
        if i not in ['X', 'O']:
            return False
    return True

   
def play_game():
    board = [str(i) for i in range(1,10)]
    current_player = 'X'

    print("TIC-TAC-TOE")
    display_board(board)
    while True:
        try:
            choice = int(input(f"PLAYER {current_player} turn,choose (btw1-9): "))
            position = choice -1
            if position>8 or position<0:
                print("Invalid range choose between 1 to 9")
                continue
            if board[position] in ['X','O']:
                print("Huhh the cell is already occupied!!")
                continue
        except ValueError:
            print("Invalid input!!")
            continue
        board[position] = current_player
        display_board(board)

        if check_winner(board,current_player):
            print(f"Player{current_player} won!!")
            break
        if draw(board):
            print("It's a tie!!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == '__main__':
    play_game()