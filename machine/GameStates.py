from enum import Enum

class States(Enum):
    MAIN_MENU = "00a"
    
    OPTIONS_MENU = "01a"
    CREDITS_MENU = "01b"
    LOAD_GAME_MENU = "01c"

    WINDOW_OPTIONS_MENU = "02a"
    SOUND_OPTIONS_MENU = "02b"
    GAMEPLAY_OPTIONS_MENU = "02c"

    IN_GAME = "03a"
    GAME_OVER_WINNER = "03b"
    GAME_OVER_DRAW = "03c"
