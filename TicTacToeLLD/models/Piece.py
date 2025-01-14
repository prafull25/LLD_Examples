from enum import Enum

class PieceType(Enum):
    EMPTY = " "
    X = "X"
    O = "O"

class Piece:
    def __init__(self,piece_type: PieceType):
        if not isinstance(piece_type,PieceType):
            raise ValueError("InValid PieceType. Please assign something else!")
        self.piece_type = piece_type

    def __str__(self):
        return self.piece_type.value
    
    def is_empty(self):
        return self.piece_type == PieceType.EMPTY