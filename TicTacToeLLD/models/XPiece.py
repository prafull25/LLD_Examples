from .Piece import Piece, PieceType

class XPiece(Piece):
    def __init__(self):
        super().__init__(piece_type=PieceType.X)