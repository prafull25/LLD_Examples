from models.MovingEntity import MovingEntity

class Snake(MovingEntity):
    def __init__(self,end_pos=None):
        super(Snake,self).__init__(end_pos,"Bit by Snake!")
        
        