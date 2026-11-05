from enum import Enum, auto

class GameState(Enum):
    INTRO = auto()
    START = auto()
    PLAYING = auto()
    GAME_OVER = auto()
    QUIT = auto()