from models.Piece import Piece
class Player:
    def __init__(self,name:str, piece:Piece):
        if not isinstance(piece,Piece):
            raise ValueError("Player must having a valid Pice")
        self.name = name
        self.piece = piece

    def get_move(self):
        try:
            row, col = map(int,input(f"{self.name} Enter your move (row and col): ").split())
            return row, col
        except ValueError:
            print("Invalid input for col, row!")
            return self.get_move()