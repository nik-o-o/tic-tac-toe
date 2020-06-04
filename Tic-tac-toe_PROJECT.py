import random
#GLOBAL
board = [' ']*10
available = [str(num) for num in range(10)]
players = [0, 'X', 'O'] # player[1] == 'X' and player[-1] == 'O'

def display_board(a,b):
    print("AVAILABLE        TIC_TAC_TOE\n" +
        "  MOVES\n\n" +
        a[7] + '|' + a[8] + '|' + a[9] + '          ' + b[7] + '|' + b[8] + '|' + b[9] + '\n' +
        '-----          -----\n' +
        a[4] + '|' + a[5] + '|' + a[6] + '          ' + b[4] + '|' + b[5] + '|' + b[6] + '\n' +
        '-----          -----\n' +
        a[1] + '|' + a[2] + '|' + a[3] + '          ' + b[1] + '|' + b[2] + '|' + b[3] + '\n')

display_board(available, board)

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def space_check(board, position):
    return board[position] == ' '

def player_choice(board, player):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        try:
            position = int(input("Player {}, choose your next position : (1-9) ".format(player)))
        except:
            print("I'm sorry, please try again.\n")
    return position

def full_board_check(board):
    return (' ' not in board[1:])

def play_again():
    return(input('Do you want to play again? : (Y/N)  ').lower().startswith('y'))

def place_marker(available, board, marker, position):
    board[position] = marker
    available[position] = " "

while(True):
    print("WELCOME TO TIC-TAC-TOE ! \n")
    toggle = random.choice([-1,1])
    player = players[toggle]
    print("For this round, Player {} will go first!\n".format(player))

    game_on = True
    input('Hit ENTER to continue... ')

    while(game_on):
        display_board(available, board)
        position = player_choice(board, player)
        place_marker(available, board, player, position)
        if win_check(board, player):
            display_board(available, board)
            print("CONGRATS! Player {} WINS\n".format(player))
            game_on = False
        else:
            if full_board_check(board):
                display_board(available, board)
                print("MATCH TIED\n")
                break;
            else:
                toggle*= -1
                player = players[toggle]

    #resetting board

    board = [' ']*10
    available = [str(num) for num in range (10)]

    if not play_again():
        break

print("THANKS FOR PLAYING! \n")
    
    
