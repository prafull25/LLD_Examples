from .Piece import Piece, PieceType

class BoardI:
    def __init__(self,size=3):
        if size<3:
            raise ValueError("Size must be greater or equal to 3!")
        self.size = size
        self.board = [[Piece(PieceType.EMPTY) for _ in range(size)] for _ in range(size)]

    def display(self):
        """Display the board for size X size """
        for row in self.board:
            print(" | ".join(str(cell) for cell in row))
            print(" _ "*self.size)

    def make_move(self,row,col,pice_type):
        if 0 <= row <self.size and 0 <= col < self.size and self.board[row][col].is_empty():
            self.board[row][col] = Piece(piece_type=pice_type)
            return True
        return False
    
    def check_winner(self):
        for i in range(self.size):
            if all(self.board[i][j].piece_type == self.board[i][0].piece_type and not self.board[i][0].is_empty() for j in range(self.size)):
                return self.board[i][0].piece_type
            
            if all(self.board[j][i].piece_type == self.board[0][i].piece_type and not self.board[0][i].is_empty() for j in range(self.size)):
                return self.board[0][i].piece_type
            
        if all(self.board[i][i].piece_type==self.board[0][0].piece_type and not self.board[0][0].is_empty()
                for i in range(self.size)):
            return self.board[0][0].piece_type
        
        if all(self.board[i][self.size-1-i].piece_type==self.board[0][self.size-1].piece_type and not self.board[0][self.size-1].is_empty()
                for i in range(self.size)):
            return self.board[0][self.size-1].piece_type
        
        return None

    def is_full(self):
        return all(not cell.is_empty() for row in self.board for cell in row)

        
        
            
