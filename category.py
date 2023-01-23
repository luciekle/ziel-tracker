import tracker, json
from datetime import datetime

class category:
    """Methods for handeling everything related to tracking a single category"""

    def __init__(self, name):
        #TODO: make sure name is a string
        self.name = name
        self.t = tracker()
        
    
    def start(self):
        print(f"Hallo!\n")
        go = input("Möchtest du eine neue Kategorie tracken? [y/n]")
        if (go == "y"):
            #TODO: Prüfen, ob Kategorie schon existiert
            cat_name = input("Was möchtest du tracken?")
            cat = category(cat_name)
    
        go = input("Möchtest du für heute etwas tracken? [y/n]")
        if (go == "y"):
            #TODO: cat_list printen mit Zahlen
            #for (i in cat_list) print(f"[\i] \cat_list[i]")
            cat_number = input("Bitte wähle deine Kategorie:")
            #cat = cat_list[cat_number]
            cat.add_today()

        go = input("Möchtest du deine Gewohnheiten analysieren? [y/n]")
        if (go == "y"):
            print("[1] Graph")
            vis = input("Wie möchtest du deine Daten darstellen?")
            # TODO: Go Nicole!
        
        print("byeee <3")

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