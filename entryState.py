from enum import Enum

class EntryState(Enum):
    EMPTY = 0
    OBSTACLE = 1
    START = 2
    TARGET = 3
    QUEUED = 4
    PROCESSED = 5
    PATH = 6