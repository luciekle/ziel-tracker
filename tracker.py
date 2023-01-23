from datetime import datetime


class tracker:
    """This tracker (for now) works with a list. 
    If the date is in the list, the habit is considered 'tracked'"""
    
    def __init__(self):
          self.t = []
    
    """add any date to the tracker"""
    #don't allow days in the future to be added
    def add_new(self, date): 
        if date <= datetime.today().strftime('%Y-%m-%d'):
            self.t.append(date)
    
    """remove any date from the tracker"""
    def delete(self, date):
        self.t.remove(date)
    

    def __(self):
        for i in self.t:
            print(self.t[i])