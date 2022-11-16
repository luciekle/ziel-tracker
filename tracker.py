class tracker:
    """This tracker (for now) works with a list. 
    If the date is in the list, the habit is considered 'tracked'"""
    
    def __init__(self):
          self.t = []
    
    """add any date to the tracker"""
    #TODO: don't allow days in the future to be added
    def add_new(self, date): 
        self.t.append(date)
    
    """remove any date from the tracker"""
    def delete(self, date):
        self.t.remove(date)