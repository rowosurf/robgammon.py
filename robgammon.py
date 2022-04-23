import time
import random

board = {'A1': ' ', 'B1': ' ', 'C1': ' ', 'D1': ' ', 'E1': ' ',
         'A2': ' ', 'B2': ' ', 'C2': ' ', 'D2': ' ', 'E2': ' ',
         'A3': ' ', 'B3': ' ', 'C3': ' ', 'D3': ' ', 'E3': ' ',
         'A4': ' ', 'B4': ' ', 'C4': ' ', 'D4': ' ', 'E4': ' ',
         'A5': ' ', 'B5': ' ', 'C5': ' ', 'D5': ' ', 'E5': ' '}

def print_board(board):
    print("  A B C D E")
    print(' +---------+')
    print('1' + '|' + board['A1'] + '|' + board['B1'] + '|' + board['C1'] + '|' + board['D1'] + '|' + board['E1'] + '|' + '1')
    print(' +---------+')
    print('2' + '|' + board['A2'] + '|' + board['B2'] + '|' + board['C2'] + '|' + board['D2'] + '|' + board['E2'] + '|' + '2')
    print(' +---------+')
    print('3' + '|' + board['A3'] + '|' + board['B3'] + '|' + board['C3'] + '|' + board['D3'] + '|' + board['E3'] + '|' + '3')
    print(' +---------+')
    print('4' + '|' + board['A4'] + '|' + board['B4'] + '|' + board['C4'] + '|' + board['D4'] + '|' + board['E4'] + '|' + '4')
    print(' +---------+')
    print('5' + '|' + board['A5'] + '|' + board['B5'] + '|' + board['C5'] + '|' + board['D5'] + '|' + board['E5'] + '|' + '5')
    print(' +---------+')
    print("  A B C D E")
    time.sleep(1)

def setup_board(board):
    board['A5'] = 'X'
    board['B5'] = 'X'
    board['C5'] = 'X'
    board['D5'] = 'X'
    board['E5'] = 'X'
    board['A1'] = 'Y'
    board['B1'] = 'Y'
    board['C1'] = 'Y'
    board['D1'] = 'Y'
    board['E1'] = 'Y'

def clear_board(board):
    board['A1'] = ' '
    board['B1'] = ' '
    board['C1'] = ' '
    board['D1'] = ' '
    board['E1'] = ' '
    board['A2'] = ' '
    board['B2'] = ' '
    board['C2'] = ' '
    board['D2'] = ' '
    board['E2'] = ' '
    board['A3'] = ' '
    board['B3'] = ' '
    board['C3'] = ' '
    board['D3'] = ' '
    board['E3'] = ' '
    board['A4'] = ' '
    board['B4'] = ' '
    board['C4'] = ' '
    board['D4'] = ' '
    board['E4'] = ' '
    board['A5'] = ' '
    board['B5'] = ' '
    board['C5'] = ' '
    board['D5'] = ' '
    board['E5'] = ' '

turn = 'X'
victory = 0

def move_piece(position,newposition,turn):
    board[position] = ' '
    board[newposition] = turn
    print_board(board)
    if turn == 'X':
        turn = 'Y'
    else:
        turn = 'X'
    return turn

def position_check(position):
    if position == 'A1':
        pass
    elif position == 'B1':
        pass
    elif position == 'C1':
        pass
    elif position == 'D1':
        pass
    elif position == 'E1':
        pass
    elif position == 'A2':
        pass
    elif position == 'B2':
        pass
    elif position == 'C2':
        pass
    elif position == 'D2':
        pass
    elif position == 'E2':
        pass
    elif position == 'A3':
        pass
    elif position == 'B3':
        pass
    elif position == 'C3':
        pass
    elif position == 'D3':
        pass
    elif position == 'E3':
        pass
    elif position == 'A4':
        pass
    elif position == 'B4':
        pass
    elif position == 'C4':
        pass
    elif position == 'D4':
        pass
    elif position == 'E4':
        pass
    elif position == 'A5':
        pass
    elif position == 'B5':
        pass
    elif position == 'C5':
        pass
    elif position == 'D5':
        pass
    elif position == 'E5':
        pass
    else:
        position = ''
    return position

def move_up(position,newposition):
    if position == 'A5':
        newposition = 'A4'
    elif position == 'A4':
        newposition = 'A3'
    elif position == 'A3':
        newposition = 'A2'
    elif position == 'A2':
        newposition = 'A1'
    elif position == 'A1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'B5':
        newposition = 'B4'
    elif position == 'B4':
        newposition = 'B3'
    elif position == 'B3':
        newposition = 'B2'
    elif position == 'B2':
        newposition = 'B1'
    elif position == 'B1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'C5':
        newposition = 'C4'
    elif position == 'C4':
        newposition = 'C3'
    elif position == 'C3':
        newposition = 'C2'
    elif position == 'C2':
        newposition = 'C1'
    elif position == 'C1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'D5':
        newposition = 'D4'
    elif position == 'D4':
        newposition = 'D3'
    elif position == 'D3':
        newposition = 'D2'
    elif position == 'D2':
        newposition = 'D1'
    elif position == 'D1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'E5':
        newposition = 'E4'
    elif position == 'E4':
        newposition = 'E3'
    elif position == 'E3':
        newposition = 'E2'
    elif position == 'E2':
        newposition = 'E1'
    elif position == 'E1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    else:
        pass
    return newposition

def move_down(position,newposition):
    if position == 'A1':
        newposition = 'A2'
    elif position == 'A2':
        newposition = 'A3'
    elif position == 'A3':
        newposition = 'A4'
    elif position == 'A4':
        newposition = 'A5'
    elif position == 'A5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'B1':
        newposition = 'B2'
    elif position == 'B2':
        newposition = 'B3'
    elif position == 'B3':
        newposition = 'B4'
    elif position == 'B4':
        newposition = 'B5'
    elif position == 'B5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'C1':
        newposition = 'C2'
    elif position == 'C2':
        newposition = 'C3'
    elif position == 'C3':
        newposition = 'C4'
    elif position == 'C4':
        newposition = 'C5'
    elif position == 'C5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'D1':
        newposition = 'D2'
    elif position == 'D2':
        newposition = 'D3'
    elif position == 'D3':
        newposition = 'D4'
    elif position == 'D4':
        newposition = 'D5'
    elif position == 'D5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'E1':
        newposition = 'E2'
    elif position == 'E2':
        newposition = 'E3'
    elif position == 'E3':
        newposition = 'E4'
    elif position == 'E4':
        newposition = 'E5'
    elif position == 'E5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    else:
        pass
    return newposition

def move_right(position,newposition):
    if position == 'A1':
        newposition = 'B1'
    elif position == 'B1':
        newposition = 'C1'
    elif position == 'C1':
        newposition = 'D1'
    elif position == 'D1':
        newposition = 'E1'
    elif position == 'E1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'A2':
        newposition = 'B2'
    elif position == 'B2':
        newposition = 'C2'
    elif position == 'C2':
        newposition = 'D2'
    elif position == 'D2':
        newposition = 'E2'
    elif position == 'E2':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'A3':
        newposition = 'B3'
    elif position == 'B3':
        newposition = 'C3'
    elif position == 'C3':
        newposition = 'D3'
    elif position == 'D3':
        newposition = 'E3'
    elif position == 'E3':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'A4':
        newposition = 'B4'
    elif position == 'B4':
        newposition = 'C4'
    elif position == 'C4':
        newposition = 'D4'
    elif position == 'D4':
        newposition = 'E4'
    elif position == 'E4':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'A5':
        newposition = 'B5'
    elif position == 'B5':
        newposition = 'C5'
    elif position == 'C5':
        newposition = 'D5'
    elif position == 'D5':
        newposition = 'E5'
    elif position == 'E5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    else:
        pass
    return newposition

def move_left(position,newposition):
    if position == 'E1':
        newposition = 'D1'
    elif position == 'D1':
        newposition = 'C1'
    elif position == 'C1':
        newposition = 'B1'
    elif position == 'B1':
        newposition = 'A1'
    elif position == 'A1':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'E2':
        newposition = 'D2'
    elif position == 'D2':
        newposition = 'C2'
    elif position == 'C2':
        newposition = 'B2'
    elif position == 'B2':
        newposition = 'A2'
    elif position == 'A2':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'E3':
        newposition = 'D3'
    elif position == 'D3':
        newposition = 'C3'
    elif position == 'C3':
        newposition = 'B3'
    elif position == 'B3':
        newposition = 'A3'
    elif position == 'A3':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'E4':
        newposition = 'D4'
    elif position == 'D4':
        newposition = 'C4'
    elif position == 'C4':
        newposition = 'B4'
    elif position == 'B4':
        newposition = 'A4'
    elif position == 'A4':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    elif position == 'E5':
        newposition = 'D5'
    elif position == 'D5':
        newposition = 'C5'
    elif position == 'C5':
        newposition = 'B5'
    elif position == 'B5':
        newposition = 'A5'
    elif position == 'A5':
        print("Can't move that direction, edge of board...")
        time.sleep(1)
        newposition = ''
    else:
        pass
    return newposition

def move_left_right_up_down(position,newposition):
    if newposition == 'w':
        newposition = move_up(position,newposition)
    elif newposition == 's':
        newposition = move_down(position,newposition)
    elif newposition == 'a':
        newposition = move_left(position,newposition)
    elif newposition == 'd':
        newposition = move_right(position,newposition)
    elif newposition == '8':
        newposition = move_up(position,newposition)
    elif newposition == '2':
        newposition = move_down(position,newposition)
    elif newposition == '4':
        newposition = move_left(position,newposition)
    elif newposition == '6':
        newposition = move_right(position,newposition)
    else:
        newposition = ''
    return newposition

def print_winner_statement(turn):
    if turn == 'X':
        turn = 'Y'
    else:
        turn = 'X'
    print('')
    print(f'{turn} wins!')
    time.sleep(1)

def play_the_game(board):
    global victory
    global turn
    while victory == 0:
        print('')
        print(f"It's {turn}'s turn'")
        time.sleep(1)
        position = ''
        newposition = ''
        while position == '':
            position = input('Which piece will you move? [ex: A5] ')
            position = position_check(position)
        if board[position] != turn:
            print(f'No piece there...')
            time.sleep(1)
            position = ''
        else:
            while newposition == '':
                newposition = input('Where will you move to? [w = up, s = down, a = left, d = right] ')
                newposition = move_left_right_up_down(position,newposition)
            if board[newposition] == turn:
                print('Your piece is in that position')
                time.sleep(1)
                newposition = ''
                play_the_game(board)
            else:
                pass
            turn = move_piece(position,newposition,turn)
            if board['A1'] == 'X':
                victory = 1
            elif board['B1'] == 'X':
                victory = 1
            elif board['C1'] == 'X':
                victory = 1
            elif board['D1'] == 'X':
                victory = 1
            elif board['E1'] == 'X':
                victory = 1
            elif board['A5'] == 'Y':
                victory = 1
            elif board['B5'] == 'Y':
                victory = 1
            elif board['C5'] == 'Y':
                victory = 1
            elif board['D5'] == 'Y':
                victory = 1
            elif board['E5'] == 'Y':
                victory = 1
            else:
                pass
            if victory == 1:
                print_winner_statement(turn)
            else:
                pass
    play_again = ''
    while play_again == '':
        play_again = input('Play again? [y = yes, no = no] ')
        if play_again == 'y':
            clear_board(board)
            victory = 0
            setup_board(board)
            print_board(board)
            play_the_game(board)
        elif play_again == 'n':
            pass
        else:
            play_again = ''

setup_board(board)
print_board(board)
play_the_game(board)
