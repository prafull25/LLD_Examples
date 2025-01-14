from models.Board import BoardI
from models.Player import Player
from models.OPiece import OPiece
from models.XPiece import XPiece
from typing import List

class Game:
    # _instance = None
    # def __new__(cls,*args,**kwargs):
    #     if cls._isinstance is None:
    #         cls._instance = super(Game,cls)__new__(cls,*args,**kwargs)
    #     return cls._instance
    
    def __init__(self,size,players : List[Player]):
        if size < 3:
            raise ValueError("size must be atleast 3")
        
        self.size = size
        self.board = BoardI(size=size)

        if len(players)<2:
            raise ValueError("Player must be more than 1 !")
        self.players = players
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index +1)% len(self.players)
    
    def play(self):
        print("Game starting .....")
        self.board.display()
        while True:
            current_player = self.players[self.current_player_index]
            move_made = False

            while not move_made:
                try:
                    row, col = current_player.get_move()
                    move_made = self.board.make_move(row,col,current_player.piece.piece_type)
                    if not move_made:
                        print("cell is already occupied try again!")
                except ValueError:
                    print("Invalid Input!")

            self.board.display()

            winner = self.board.check_winner()

            if winner:
                print(f"WOW! {current_player.name} ({winner.value})won the match! ")
                break

            if self.board.is_full():
                print("oops! It's a draw!!")
                break

            self.switch_player()


