class Player():
    def __init__(self, name):
        self.name = name  # Name
        self.open_methods = ["Search", "Examine"]  # Methods to be used by Plyr
        self.current_room = None  # The Current Room
        self.inventory = []  # The Inventory Of The Player

    def moveTo(self, room):
        self.current_room = room

    def Search(self, Plyr, instances):
        print("You search " + self.name)
        strng = ""   # Init String Variable To Hold Output
        indx = 0   # Index of Loop
        for i in self.inventory:
            indx = indx + 1
            strng = strng + i.name
            if indx != len(self.inventory):
                strng = strng + ", "
        if indx == 0:
            print("You Found Nothing!")
        else:
            print("You find: " + strng)

    def Examine(self, Plyr, instances):
        print(self.name + " is in the " + self.current_room.name)
        fs = ""  # Init string var
        if len(self.inventory) > 1:
            fs = "s"
        else:
            fs = ""
        print(self.name + " has an inventory containing " +
              str(len(self.inventory)) +
              " item" + fs + " ('search " + self.name + "')")
