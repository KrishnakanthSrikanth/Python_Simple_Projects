# Tic Tac Toe Game

# Step 1: Draw a board

board = {
    'K7': ' ', 'K8': ' ', 'K9': ' ',
    'K4': ' ', 'K5': ' ', 'K6': ' ',
    'K1': ' ', 'K2': ' ', 'K3': ' '
}

player = 1
totalmoves = 0
won = 0

# Winner Check
def winning_rule():
    # Check for player 1
    # HorizontalCheck
    if board['K1'] == 'X' and board['K2'] == 'X' and board['K3'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    if board['K4'] == 'X' and board['K5'] == 'X' and board['K6'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    if board['K7'] == 'X' and board['K8'] == 'X' and board['K9'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    # DiagonalCheck
    if board['K1'] == 'X' and board['K5'] == 'X' and board['K9'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    if board['K3'] == 'X' and board['K5'] == 'X' and board['K7'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    # VerticalCheck
    if board['K1'] == 'X' and board['K4'] == 'X' and board['K7'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    if board['K2'] == 'X' and board['K8'] == 'X' and board['K'] == 'X':
        print("Player 1 wins..!!!")
        return 1
    if board['K3'] == 'X' and board['K6'] == 'X' and board['K9'] == 'X':
        print("Player 1 wins..!!!")
        return 1

    # Check for player 2
    # HorizontalCheck
    if board['K1'] == 'O' and board['K2'] == 'O' and board['K3'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    if board['K4'] == 'O' and board['K5'] == 'O' and board['K6'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    if board['K7'] == 'O' and board['K8'] == 'O' and board['K9'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    # DiagonalCheck
    if board['K1'] == 'O' and board['K5'] == 'O' and board['K9'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    if board['K3'] == 'O' and board['K5'] == 'O' and board['K7'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    # VerticalCheck
    if board['K1'] == 'O' and board['K4'] == 'O' and board['K7'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    if board['K2'] == 'O' and board['K8'] == 'O' and board['K5'] == 'O':
        print("Player 2 wins..!!!")
        return 1
    if board['K3'] == 'O' and board['K6'] == 'O' and board['K9'] == 'O':
        print("Player 2 wins..!!!")
        return 1

    return 0


print('K7|K8|K9')
print('+-+-+-+')
print('K4|K5|K6')
print('+-+-+-+')
print('K1|K2|K3')
print('------------------')

while True:
    print(board['K7'] + '|' + board['K8'] + '|' + board['K9'])
    print('-+-+-')
    print(board['K4'] + '|' + board['K5'] + '|' + board['K6'])
    print('-+-+-')
    print(board['K1'] + '|' + board['K2'] + '|' + board['K3'])
    print('--------------------------------------')
    won=winning_rule()
    if totalmoves == 9 and won == 1:
        break

    # Input from players
    while True:
        if player == 1:
            player1input = (input("P1 Input:"))
            if player1input.upper() in board and board[player1input.upper()] == ' ':
                board[player1input.upper()] = 'X'
                player = 2
                break
            else:
                print("Invalid Input..Please try again!")
                continue
        else:
            player2input = (input("P2 Input:"))
            if player2input.upper() in board and board[player2input.upper()] == ' ':
                board[player2input.upper()] = 'O'
                player = 1
                break
            else:
                print("Invalid Input..Please try again!")
                continue
    totalmoves += 1
    print('*******************************')