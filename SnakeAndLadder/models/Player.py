
class Player:
    def __init__(self,_id,name):
        self._id= _id
        self.name = name
        self.rank = -1 # initial rank as dummy -1
        self.position = 1 

    def set_position(self,pos):
        self.position = pos

    def set_rank(self,rank):
        self.rank = rank

    def get_position(self):
        return self.position
    
    def get_rank(self):
        return self.rank
    
