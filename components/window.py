from components.translator import Translator
from objects.Board import Board
from resources.common_libraries import *
from options.default import WindowDefault as WD
from resources.colors import ColorRGB as Color
from machine.GameStates import States as State

class WindowComponent:
    def __init__(self, isDefault, loaded_width = None, loaded_height = None):
        self.win = None
        py.display.set_caption(WD.TITLE)
        if isDefault:
            self.initAsDefault()
        else:
            if loaded_width == None or loaded_height == None:
                print("Couldnt load custom height and custom width from game files. ")
        self.sprite = Sp(loaded_width, loaded_height)
        self.old_board = None
        self.begin_game = True


    def initAsDefault(self):
        self.win = py.display.set_mode((WD.WIDTH, WD.HEIGHT))

    # Run function that allows to draw stuff in the window
    def run(self, current_state, board: Board = None, translator: Translator = None):
        if current_state == State.IN_GAME and board != None or current_state == State.GAME_OVER_DRAW or current_state == State.GAME_OVER_WINNER:
            self.win.fill(Color.BLACK)

            if board != None and self.begin_game:
                self.draw_board_start_game(board)
            if board != None and not self.begin_game and self.old_board != None:
                self.draw_board(board)
                self.draw_x_and_o(translator)
        if current_state == State.GAME_OVER_WINNER:
            line = board.winning_line
            if line != None:
                if "Line" in line:
                    l = line["Line"]
                    cell_beg, cell_end = translator.get_coors_cell((l,0),(l,2))
                
                if "Column" in line:
                    l = line["Column"]
                    cell_beg, cell_end = translator.get_coors_cell((0,l),(2,l))

                if "Diagonal" in line:
                    l = line["Diagonal"]
                    if l == 1:
                        cell_beg, cell_end = translator.get_coors_cell((0,0), (2,2))
                    if l == 2:
                        cell_beg, cell_end = translator.get_coors_cell((0,2), (2,0))

                self.draw_final_line(cell_beg, cell_end)

    def draw_x_and_o(self, translator):
        x = 0
                
        for lines in self.old_board:
            y = 0
            for column in lines:
                if column == "X":
                    coors = translator.translate_inverse_x(x,y) 
                    self.draw_x(coors[0],coors[1])
                if column == "O":
                    center, radius = translator.translate_inverse_o(x,y)
                    self.draw_circle(center[0],center[1],radius)
                y = y+1
            x = x+1

    def draw_board_start_game(self,board):
        self.begin_game = False
        for line in board.lines:
                if line == "TOP" or line == "DOWN":
                    #print(board.lines[line][0])
                    py.draw.line(self.win, Color.WHITE,(board.lines[line][0],board.lines[line][1]), (board.lines[line][0] + board.board_options.line_w, board.lines[line][1]), 1)
                if line == "LEFT" or line == "RIGHT":
                    py.draw.line(self.win, Color.WHITE,(board.lines[line][0],board.lines[line][1]), (board.lines[line][0] , board.lines[line][1] + board.board_options.line_h), 1)
        self.old_board = board.board

    def draw_board(self, board):
        for line in board.lines:
                if line == "TOP" or line == "DOWN":
                    #print(board.lines[line][0])
                    py.draw.line(self.win, Color.WHITE,(board.lines[line][0],board.lines[line][1]), (board.lines[line][0] + board.board_options.line_w, board.lines[line][1]), 1)
                if line == "LEFT" or line == "RIGHT":
                    py.draw.line(self.win, Color.WHITE,(board.lines[line][0],board.lines[line][1]), (board.lines[line][0] , board.lines[line][1] + board.board_options.line_h), 1)
        self.old_board = board.board
    
    def draw_x(self, line_beg, line_end):
        py.draw.line(self.win,Color.WHITE, line_beg, line_end)
        py.draw.line(self.win, Color.WHITE, (line_end[0], line_beg[1]),(line_beg[0],line_end[1]))

    def draw_circle(self,x,y, radius):
        py.draw.circle(self.win, Color.WHITE, (x,y), radius, width = 1)

    def draw_new_x(self,line_beg, line_end):
        pass
    def draw_new_circle(self,x,y,radius):
        pass

    def draw_final_line(self, pos_beg, pos_end):
        py.draw.line(self.win, Color.WHITE, pos_beg, pos_end)