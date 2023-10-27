from components.translator import Translator
from objects.Board import Board
from resources.common_libraries import *
from options.default import WindowDefault as WD
from machine.GameStates import States as State

class EventManagerComponent:
    def __init__(self):
        self.clock = py.time.Clock()

    def run(self, current_state = State.MAIN_MENU, translator: Translator = None, board: Board= None) -> bool:
        self.clock.tick(WD.FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                return False
            if event.type == py.MOUSEBUTTONDOWN and current_state == State.IN_GAME:
                if event.button == 1:
                    x, y = py.mouse.get_pos()
                    print(f"Left mouse button clicked at (x:{x}, y:{y})") 
                    cell = translator.translate(mouse_x=x, mouse_y=y)
                    # If cell is None then transmit to the user to click inside a possible square
                    if cell == None:
                        pass
                    else:
                        valid = board.validate_position(cell[0], cell[1])
                        print(f"validation: {valid}")
                        if valid:
                            board.board[cell[0]][cell[1]] = translator.turn
                            translator.turn = "X" if translator.turn == "O" else "O"
                            print(board.board)

                    
        return True
