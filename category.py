class category:
    """One individual trackable category: 
    
    this tracker (for now) works with a list. 
    If the date is in the list, the habit is considered 'tracked'"""

    import tracker
    from datetime import datetime
    
    def __init__(self, name):
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
        if (date in self.tracker):
            self.t.delete(self, date)
        else: self.t.add_new(self, date)
    

#TODO: add a method to check if a day was tracked
    