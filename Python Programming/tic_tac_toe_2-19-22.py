import random

theBoard = {'7': '.' , '8': '.' , '9': '.' ,
            '4': '.' , '5': '.' , '6': '.' ,
            '1': '.' , '2': '.' , '3': '.' }

# print the board
def printBoard(board): 
    print('Current Board:')
    print('~~~~~~~~~~~~~~~~~~~~')
    print('  ' + '0' + '  ' + '1' + '  ' + '2')
    print('0' + ' ' + board['7'] + '  ' + board['8'] + '  ' + board['9'])
    print('1' + ' ' + board['4'] + '  ' + board['5'] + '  ' + board['6'])
    print('2' + ' ' + board['1'] + '  ' + board['2'] + '  ' + board['3'])
    print('~~~~~~~~~~~~~~~~~~~~~')

# user input row and column
def place(x,y):
    if x == '0' and y == '0':
        return '7'
    elif x == '0' and y == '1':
        return '8'
    elif x == '0'and y == '2':
        return '9'
    elif x == '1' and y == '0':
        return '4'
    elif x == '1' and y == '1':
        return '5'
    elif x == '1' and y == '2':
        return '6'
    elif x == '2' and y == '0':
        return '1'
    elif x == '2' and y == '1':
        return '2'
    elif x == '2' and y == '2':
        return '3'
    else:
        print('Invalid selection. Choose 0,1,2 for row and columns')
        
def check_win():
    
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != '.': # top           
        print(theBoard['7'] + " wins!!") 
        return 'break'
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '.': # middle
        print(theBoard['4'] + " wins!!")
        return 'break'
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != '.': # bottom
        print(theBoard['1'] + " wins!!")
        return 'break'
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != '.': # left side
        print(theBoard['7'] + " wins!!")
        return 'break'
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != '.': # down the middle
        print(theBoard['2'] + " wins!!")
        return 'break'
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != '.': # right side
        print(theBoard['3'] + " wins!!")
        return 'break'
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != '.': # diagonal
        print(theBoard['7'] + " wins!!")
        return 'break'
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != '.': # diagonal
        print(theBoard['1'] + " wins!!")
        return 'break'

def get_user_input():
    row = input('What row? ')
    col = input('What column? ')
    while row == '' or col == '' or row not in '012' or col not in '012':
        print('Invalid selection. Choose 0, 1, or 2 for row and column.')
        row = input('What row? ')
        col = input('What column? ')
    return row, col
    
        
def game():
    turn = input("X or O? ")
    while turn == '' or turn not in 'XO':
        print('Invalid response. Choose X or O')
        turn = input("X or O? ")
        
    if turn == 'X':
        count = 0       
        while '.' in theBoard.values():                
            print('##################')
            print('######' + 'Round #' + str(count+1) + '######')
            print('##################')
            printBoard(theBoard)

            #user's turn
            print("Player " + turn +"'s turn:")
            row, col = get_user_input()            
            ans = input('Place ' + turn + ' at row ' + row + ' column '+ col + "?" + '[y/n] ')
            while ans == '' or ans not in 'yY':
                row, col = get_user_input()                
                ans = input('Place ' + turn + ' at row ' + row + ' column '+ col + "?" + '[y/n] ')            
            move = place(row,col)      

            if theBoard[move] == '.':
                theBoard[move] = turn
                count += 1
                print('Move placed!')
                printBoard(theBoard)
            else:
                print("That place is already filled. Move to which place?")
                continue
                
            #see who wins or ties
            if count >= 2:
                if check_win() == 'break':
                    break
            
            if count > 3 and ('.' not in theBoard.values()):
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                break

            #computer's move

            print("Player O's turn")
            computer = str(random.randint(1,9))
            while theBoard[computer] != '.':
                computer = str(random.randint(1,9))                
            theBoard[computer] = 'O'
            print('Computer move registers')
            printBoard(theBoard)
            
            #see who wins or ties
            if count >= 2:
                if check_win() == 'break':
                    break
            
            if count > 3 and ('.' not in theBoard.values()):
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                break        
            
                
    else:
        count = 1       
        while '.' in theBoard.values():                  
            print('##################')
            print('######' + 'Round #' + str(count) + '######')
            print('##################')
            printBoard(theBoard)      
                
            #computer move
            print("Player X's turn")
            computer = str(random.randint(1,9))
            while theBoard[computer] != '.':
                computer = str(random.randint(1,9))                
            theBoard[computer] = 'X'
            print('Computer move registers')
            printBoard(theBoard)
            
            #see who wins or ties
            if count >= 2:
                if check_win() == 'break':
                    break
            
            if count > 3 and ('.' not in theBoard.values()):
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                break

            #user's turn
            while True: #################
                print("Player O's turn:")

                row, col = get_user_input()            
                ans = input('Place ' + turn + ' at row ' + row + ' column '+ col + "?" + '[y/n] ')
                while ans == '' or ans not in 'yY':
                    row, col = get_user_input()                
                    ans = input('Place ' + turn + ' at row ' + row + ' column '+ col + "?" + '[y/n] ')            

                move = place(row,col)      

                if theBoard[move] == '.':
                    theBoard[move] = 'O'
                    count += 1
                    print('Move placed!')
                    printBoard(theBoard)
                    break
                else:
                    print("That place is already filled. Move to which place?")
                    continue
                
            #see who wins or ties
            if count >= 2:
                if check_win() == 'break':
                    break
            
            if count > 3 and ('.' not in theBoard.values()):
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                break
            
if __name__ == "__main__":
    game()
            