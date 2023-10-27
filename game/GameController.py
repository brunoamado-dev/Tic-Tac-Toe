from components.translator import Translator
from machine.GameMachine import GameMachine
from components.events import EventManagerComponent
from components.window import WindowComponent
from components.update import UpdateComponent
from machine.GameStates import States as State
from objects.Board import Board
from options.board_options import BoardOptions
from options.default import WindowDefault as WD
class GameController:
    def __init__(self):
        self.machine = GameMachine()
        self.window = WindowComponent(isDefault=True)
        self.events = EventManagerComponent()
        self.update = UpdateComponent()
        self.isRunning = True
        self.board_options = BoardOptions(win_w=WD.WIDTH, win_h=WD.HEIGHT)
        self.board= Board(self.board_options) 
        self.translator = Translator(board=self.board)


    def load_game():
        pass

    def run(self):
        while self.isRunning:
            if self.machine.state == State.IN_GAME:
                self.run_in_game()
    
    def run_in_main_menu(self):
        pass

    def run_in_game (self):
        while self.isRunning:
            self.window.run(self.machine.state, self.board, translator=self.translator)
            self.isRunning = self.events.run(current_state=self.machine.state,  translator=self.translator, board=self.board)
            self.update.run(current_state=self.machine.state, board= self.board, machine=self.machine)