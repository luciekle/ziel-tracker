class tracker:
    
    def __init__(self):
          self.t = []
    
    """add any date to the tracker"""
    def add_new(self, date): 
        self.t.append(date)
    
    """remove any date from the tracker"""
    def delete(self, date):
        self.t.remove(date)