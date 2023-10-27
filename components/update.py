from machine.GameMachine import GameMachine
from objects.Board import Board
from resources.common_libraries import *
from machine.GameStates import States as State

class UpdateComponent:
    def __init__(self):
        pass
    
    def run(self, current_state=State.MAIN_MENU, board:Board=None, machine:GameMachine = None):
        if current_state == State.IN_GAME:
            s = board.check_for_winner() if board != None else None
            if s:
                machine.endGameWin()
                print("Winner")

            else:
                isGameOver = board.check_game_over()
                if isGameOver:
                    machine.endGameDraw()
                    print("No winnder a dRaw")
                

                    
                    

        py.display.update()
    
