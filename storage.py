import random


class Storage():
    def __init__(self, name):
        self.parent = None  # The Parent
        self.name = name  # The Name
        self.open_methods = ["Search"]  # Methods to be used by Plyr
        self.inventory = []  # The inventory of the storage
        self.locked = False  # Whether its locked or not
        self.lock_id = random.randint(1, 1000)  # The Id To Lock/Unlock it

    def AddContent(self, content):
        self.inventory.append(content)
        if hasattr(content, "parent"):
            content.parent = self

    def RemoveContent(self, content):
        for i in range(0, len(self.inventory)):
            if self.inventory[i] == content:
                del self.inventory[i]

    def UseKey(self, key):
        if key.id == self.lock_id:
            self.locked = not (self.locked)
            if self.locked == True:
                print("Correct key, locking.")
            else:
                print("Correct key, unlocking.")
        else:
            print("Wrong Key!")

    def Search(self, Plyr, instances):
        if self.locked == True:
            print(self.name + " is locked, cannot search")
            return()
        else:
            pass
        print("You search " + self.name)
        strng = ""  # Init String To Hold Output
        indx = 0  # Index of loop
        for i in self.inventory:
            indx = indx + 1
            strng = strng + i.name
            if indx != len(self.inventory):
                strng = strng + ", "
        if indx == 0:
            print("You Found Nothing!")
        else:
            print("You find: " + strng)
