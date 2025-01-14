from models.MovingEntity import MovingEntity

class Ladder(MovingEntity):
    def __init__(self,end_pos=None):
        super(Ladder,self).__init__(end_pos,"climbed on ladder!")
        
        