import tracker
from datetime import datetime

class category:
    """Methods for handeling everything related to tracking a single category"""

    def __init__(self, name):
        #TODO: make sure name is a string
        self.name = name
        self.t = tracker()

# getters and setters for the category's name
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
    
# methods to handle data
    """add only the current date to the tracker"""
    def add_today(self):
        today = datetime.today().strftime('%Y-%m-%d')
        self.t.add_new(self, today)


    """change any date from checked to unchecked or vice-versa"""
    def change(self, date):
        if (date in self.t):
            self.t.delete(self, date)
        else: self.t.add_new(self, date)
    
    """check if a date was tracked"""
    def check(self, date):
        return True if (date in self.t) else False

# danger zone
    """clear all tracked data"""
    def clear_tracker(self):
        self.t = []
        
    """delete this entire tracker with all data"""
    def __del__(self):
        del self.t