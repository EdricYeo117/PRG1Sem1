import random


### TicTacToe class ###
class TicTacToe:
    ## initialising self.board = []
    '''To do: initialise self.board = []'''
    def __init__(self):
        self.board = []
    
    ## creating the board
    def create_board(self):         # have a list for each row, and append the list into self.board
        for rowNo in range(3):
            row = []
            for colNo in range(3):
                row.append('-')
            '''To do: append the list for each row into self.board'''
            self.board.append(row)
            
    
    ## randomising the first player
    def get_random_first_player(self):
        '''To do: get a random integer, either 0 or 1'''
        randomNum = random.randint(0, 1)
        if randomNum == 1:
            return "X"
        else:
            return "O"

    ## adding player spot onto the board
    def fix_spot(self, row, col, player):
        '''To do: set the desired position to be the player icon'''
        self.board[row][col] = player


    ## checking if player wins
    def player_win(self, player):
        win = None

        # checking for wins in a row
        # O O O
        for rowNo in range(3):
            win = True
            for colNo in range(3):
                '''To do: conditional check for a false row win'''
                if self.board[rowNo][colNo] != player:
                    win = False
                    break
            if win:            # if not a row win, continue checking for other wins
                return win
    
        # checking for wins in a column
        # O
        # O
        # O
        for colNo in range(3):
            win = True
            for rowNo in range(3):
                '''To do: conditional check for a false column win'''
                if self.board[rowNo][colNo] != player:
                    win = False
                    break
            if win:            # if not a column win, continue checking for other wins
                return win
        
        # checking for wins in decreasing diagonal
        # O
        #   O
        #     O
        win = True
        for index in range(3):
            '''To do: conditional check for a false first diagonal win'''
            # <hint: what is the correlation between the diagonal win row number and column number?>
            if self.board[index][index] != player:
                win = False
                break
        if win:        # if not a first diagonal win, continue checking for other wins
            return win
        
        # checking for wins in increasing diagonal
        #     O
        #   O
        # O
        win = True
        for index in range(3):
            '''To do: conditional check for a false second diagonal win'''
            # <hint: what is the correlation between the diagonal win row number and column number?>
            if self.board[index][2 - index] != player:
                win = False
                break
        if win:     # if not a second diagonal win, continue checking for other wins
            return win


    ## checking if the board is filled (match draw)
    def board_filled(self):
        for row in self.board:
            for item in row:
                if item == "-":
                    return False
        return True
    
    ## changing the player every turn
    def swap_player(self, player):
        if player == "O":
            '''To do: return next player icon'''
            return "X"
            
        else:
            '''To do: return next player icon'''
            return "O"


    ## printing the board
    def show_board(self):
        for row in self.board:
            for item in row:
                '''To do: print the item, do end with a space'''
                print(item, end = " ")
            print()
    
    ## starting the program
    def start(self):
        '''To do: call out the method to create a board'''
        self.create_board()
        player = self.get_random_first_player()
        while True:
            '''To do: print out current player's turn. Syntax: Player X turn'''
            # <hint: use .format()!>
            print("Player {} turn".format(player))

            self.show_board()           # printing out board
            userInput = input("Enter row and column number separated by a space: ").split()
            '''To do: assign values of row and col from userInput'''
            # <hint: a, b = 0, 1>
            row, col = int(userInput[0]), int(userInput[1])
            if self.board[row - 1][col - 1] != "-":             # fixing spot only if the spot is empty
                print("The spot is already taken. ")
                continue
            else: 
                self.fix_spot(row - 1, col - 1, player)
            if self.player_win(player):             # checking if the current player has won the game
                print("Player {} wins the game!".format(player))
                '''To do: insert a break statement to break out of the while loop when the player wins'''
                break

            if self.board_filled():             # checking if a draw is made by the players
                print("Match draw!")
                '''To do: insert a break statement to break out of the while loop when it is a draw'''
                break

            player = self.swap_player(player)           #swapping to the next player
        print()
        self.show_board()           # printing the final view of the board before ending

### starting the game ###
ticTacToe = TicTacToe()
ticTacToe.start()
