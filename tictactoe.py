from functools import reduce
from random import randint

BOARD = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
win_comb = [[1,5,9],[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7]]

def shape_board(result,key):
    result += '|'
    result += BOARD[key]
    if int(key) % 3 == 0:
        result += '|'
        result += '\n'
    return result


def print_board(board):
    return reduce(shape_board,board,'\n')

def player1():
    print('Player1 chance')
    new_board = {}
    user_player = int(input('Enter your position from 1-9'))
    if BOARD[user_player]==' ':
        BOARD[user_player]='x'
        BOARD.update(new_board)
        print(f'printing board:\n{print_board(BOARD)}')
        win = check_testing('x')
        if win:
            print('Player1 won the game')
            exit()
    else:
        print('Invalid: Try again')   #if the player played in the same location giving chance to play again
        player1()
    player2()



def player2():
    print('Player2 chance')
    new_board = {}
    user_player = int(input('Enter your position from 1-9'))
    if BOARD[user_player]==' ':
        BOARD[user_player] = 'o'
        BOARD.update(new_board)
        print(f'printing board:\n{print_board(BOARD)}')
        win = check_testing('o')
        if win:
            print('Player2 won the game')
            exit()
    else:
        print('Invalid: Try again')
        player2()
    player1()


def check_testing(player):
    check = list(map(lambda list1:list(map(lambda x1: BOARD[x1] == player, list1)),win_comb))
    win_check = list(filter(lambda i:all(check[i])==True,range(len(check))))
    #test1 = list(map(lambda x1: BOARD[x1] == player, list1))
    if len(win_check):
        return True or False

def selection_player():
    if randint(0,1)==0:
        player1()
    else:
        player2()


print('Play Tictactou game')
print(f'printing of empty board:\n{print_board(BOARD)}')

selection_player()





