class Door():
    def __init__(self, name, passthrough=None):
        self.passthrough = passthrough  # The Room To Be Moved Into
        self.open_methods = ["Use"]  # The Allowed Plyr Methods
        self.name = name  # The Name
        self.lock_id = None  # The Id To Unlock It
        self.locked = False  # Whether its locked or not
        self.parent = None  # Its Parent

    def Use(self, Plyr, instances):
        if self.locked != False:
            print(self.name + " is locked.")
            return 1
        else:
            if self.passthrough == None:
                print("This door leads nowhere")
                return 0
            else:
                Plyr.current_room = passthrough
                print("You walk through the door into the " + passthrough.name)
                return 0

    def UseKey(self, key):
        if key.id == self.lock_id:
            self.locked = not (self.locked)
            if self.locked == True:
                print("Correct key, locking.")
            else:
                print("Correct key, unlocking.")
        else:
            print("Wrong Key!")
