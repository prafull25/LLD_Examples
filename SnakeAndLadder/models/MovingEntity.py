class MovingEntity:
    def __init__(self,endpos=None,desc = ""):
        self.endpos = endpos
        self.desc = desc

    def get_desc(self):
        return self.desc
    
    def get_end_position(self):
        return self.endpos


