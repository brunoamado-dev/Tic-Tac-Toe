from options.board_options import BoardOptions


class Board:
    def __init__(self, board_options:BoardOptions = None):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        print(self.board)
        self.board_options = board_options
        self.lines = self.board_options.build_lines()
        print(self.lines)
        self.winning_line = None
    
    def validate_position(self, cell_x,cell_y):
        return  (" " == self.board[cell_x][cell_y])
    
    def check_for_winner(self):
       # check for a line winner
        i = 0
        for line in self.board:
           
            if line[0] == line[1] and line[0] == line[2] and (line[0] == "X" or line[0] == "O"):
               self.winning_line = {
                   "Line":i
               }
               return True
            i = i+1
        i = 0
        for col in range(3):
            column_values = [self.board[row][col] for row in range(3)]
            if all(value == "X" for value in column_values) or all(value == "O" for value in column_values):
                self.winning_line = {
                    "Column": i
                    
                }

                return True            
            i = i + 1

        
        
        return self.check_diagonals(self.board)
    
    def check_diagonals(self, board):
        # Check the main diagonal (top-left to bottom-right)
        main_diagonal_values = [board[i][i] for i in range(3)]
        if all(value == "X" for value in main_diagonal_values) or all(value == "O" for value in main_diagonal_values):
            self.winning_line = {
                "Diagonal":1
            }
            return True
       

        # Check the other diagonal (top-right to bottom-left)
        other_diagonal_values = [board[i][2 - i] for i in range(3)]
        if all(value == "X" for value in other_diagonal_values) or all(value == "O" for value in other_diagonal_values):
            self.winning_line = {
                "Diagonal":2
            }
            return True
        return False
    
    def check_game_over (self):
        return " " not in [cell for row in self.board for cell in row] and self.winning_line == None

        
    