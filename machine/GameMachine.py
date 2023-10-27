from machine.GameStates import States as State


class GameMachine:
    def __init__(self) -> None:
        self.state = State.IN_GAME

    def isPlaying(self):
        self.state = State.IN_GAME  if self.state == State.MAIN_MENU else self.state
        
    def goOptions(self):
        self.state = State.OPTIONS_MENU  if self.state == State.MAIN_MENU else self.state

    def goMainMenu(self):
        self.state = State.MAIN_MENU
    
   
    def endGameDraw(self):
        self.state = State.GAME_OVER_DRAW if self.state == State.IN_GAME else self.state
    
    def endGameWin(self):
        self.state = State.GAME_OVER_WINNER if self.state == State.IN_GAME else self.state