from operator import attrgetter
class card:
    def __init__(self, x, y):
        self.name = x
        self.item_id = y
        
    def __repr__(self):
        return self.name + ":" + str(self.item_id)
            
 