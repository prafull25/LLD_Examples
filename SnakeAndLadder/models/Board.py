
from models.MovingEntity import MovingEntity
class BoardI:
    def __init__(self,size):
        if size < 10: # let assume minimum size should be 100 
            raise ValueError("size should be more than or equal to 10!")
        self.size = size
        self.board = [MovingEntity(i) for i in range(0,size + 1)] # adding 1 as we will not consider 0th index

    def get_size(self):
        return self.size
    
    def set_moving_entity(self,pos,moving_entity):
        self.board[pos] = moving_entity


    def get_next_position(self,player_pos):
        if player_pos > self.size:
            return player_pos
        if not self.board[player_pos].get_desc():
            return player_pos
        print(f'{self.board[player_pos].get_desc()} at {player_pos}')
        return self.board[player_pos].get_end_position()
    
    def is_at_end_position(self,pos):
        return pos==self.size
    
