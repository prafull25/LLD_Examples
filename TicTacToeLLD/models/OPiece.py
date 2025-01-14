from .Piece import Piece, PieceType

class OPiece(Piece):
    def __init__(self):
        super().__init__(piece_type=PieceType.O)