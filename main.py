from string import ascii_uppercase
from random import randint
# from time import sleep
# import os


# number of squares of a n*n playing board is 4*n-4
# it's used a lot throughout the script


def print_board(board, *players):
    '''
    prints the board nicely
    *players are put on the board, each gets a letter assigned based on it's index 
    '''

    board = board[:]

    # putting *players on the board
    for i, player in enumerate(players):
        board[player % (4 * n - 4)] = ascii_uppercase[i]

    home = 'D'
    rows = []
    for y in range(n):
        current_row = []
        for x in range(n):
            if y < n // 2 - 1:  # top arm of the cross
                if x < n // 2 - 1 or x > n // 2 + 1:  # blank space
                    current_row.append(' ')
                elif x == n // 2 + 1:  # top right part
                    current_row.append(board[y])
                elif x == n // 2 - 1:  # top left part
                    current_row.append(board[4*n - 6 - y])
                elif x == n // 2 and y == 0:  # top middle
                    current_row.append(board[-1])
                else:
                    current_row.append(home)
            elif y > n // 2 + 1:  # bottom part of the cross
                if x < n // 2 - 1 or x > n // 2 + 1:  # blank space
                    current_row.append(' ')
                elif x == n // 2 + 1:  # bottom right part
                    current_row.append(board[y + 2 * (n // 2 - 1)])
                elif x == n // 2 - 1:  # bottom left part
                    current_row.append(board[n + 2 * (n // 2 - 1) + n - y])
                elif x == n // 2 and y == n - 1:  # bottom middle
                    current_row.append(board[n + 2 * (n // 2 - 1)])
                else:
                    current_row.append(home)
            elif x > n // 2:  # right arm of the cross
                if y == n // 2 - 1:  # top layer
                    current_row.append(board[y + x - n // 2 - 1])
                elif y == n // 2 + 1:  # bottom layer
                    current_row.append(board[n - 2 + n - x])
                elif y == n // 2 and x == n - 1:  # right middle
                    current_row.append(board[n - 2])
                else:
                    current_row.append(home)
            elif x < n // 2:  # left arm of the cross
                if y == n // 2 + 1:  # bottom layer
                    current_row.append(board[(4 * n - 4) // 4 * 3 - 2 - x])
                elif y == n // 2 - 1:  # top layer
                    current_row.append(board[(4 * n - 4) // 4 * 3 + x])
                elif y == n // 2 and x == 0:
                    current_row.append(board[(4 * n - 4) // 4 * 3 - 1])
                else:
                    current_row.append(home)
            elif y == n // 2 and x == n // 2:
                current_row.append('X')
            else:
                current_row.append(home)
        rows.append(current_row)

    print('  ' + ' '.join([str(i % 10) for i in range(n)]))
    for i, row in enumerate(rows):
        print(f'{i % 10} ' + ' '.join(row))
    # sleep(0.5)


def throw_dice():
    '''
    returns random number - like throwing a dice
    if you throw a 6, you can have another go
    '''
    sum = randint(1, 6)
    if sum == 6:
        return sum + throw_dice()
    else:
        return sum


n = ''
# user input - size of the board nxn
# must be odd and at least 5 (3x3 board has no home squares, 1x1 makes no sense)
while isinstance(n, str):
    try:
        n = int(input('Enter board size: '))
        if n % 2 == 0 or n < 5:
            n = ''
            raise ValueError
    except ValueError:
        print('It must be an odd number >= 5.')


board_template = ['-' for _ in range(4*n - 4)]


def one_player():
    # position of the current pawn on board
    playerA = 0

    print_board(board_template, playerA)
    while True:
        move = throw_dice()
        print('thrown: ' + str(move))

        if move + playerA + 1 > 4 * n - 4 + n // 2 - 1:  # invalid move
            print('A can not step that far into their house.')
            continue

        if playerA + move >= 4 * n - 4:
            print('A successfully reached their home.')
            break

        playerA += move

        print_board(board_template, playerA)
        # os.system('cls')


def two_player():
    # position of the current pawns on board
    playerA = 0
    playerB = (4*n - 4) // 2

    # pawns left
    Aleft = (n - 3)//2
    Bleft = (n - 3)//2

    print_board(board_template, playerA, playerB)
    while True:
        # player A
        move = throw_dice()
        print('A\'s throw: ' + str(move))

        if move + playerA + 1 > 4 * n - 4 + n // 2 - 1:  # invalid move
            print('A can not step that far into their house.')
            move = 0

        if playerA + move == playerB:
            print('A has taken out B')
            playerB = (4*n - 4) // 2

        if playerA + move >= 4 * n - 4:
            print('A successfully reached their home.')
            move = 0
            playerA = 0
            Aleft -= 1

            if Aleft == 0:
                print('Player A has won.')
                break

        playerA += move

        print_board(board_template, playerA, playerB)
        # os.system('cls')

        # player B
        move = throw_dice()
        print('B\'s throw: ' + str(move))

        if move + playerB > 3 * (4 * n - 4) // 2 - 1 + n // 2 - 1:  # invalid move
            print('B can not step that far into their house.')
            move = 0

        if playerB + move == playerA:
            print('B has taken out A')
            playerA = 0

        if playerB + move >= 3 * (4 * n - 4) // 2:
            print('B successfully reached their home.')
            move = 0
            playerB = (4*n - 4) // 2
            Bleft -= 1

            if Bleft == 0:
                print('Player B has won.')
                break

        playerB += move

        print_board(board_template, playerA, playerB)
        # os.system('cls')


one_player()

two_player()
