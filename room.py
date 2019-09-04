class Room():
    def __init__(self, name):
        self.name = name  # Name Variable
        self.contents = []  # The contents of the room
        self.open_methods = ["Examine", "Search"]
        # The Methods to be used by Plyr

    def Examine(self, Plyr, instances):
        print("You examine: " + self.name)
        if len(self.contents) > 1:
            print("The " + self.name +
                  " has stuff in it ('search " + self.name + "')")

    def Search(self, Plyr, instances):
        print("You search: " + self.name)
        Found = []  # Instances Found By Search
        for i in instances:
            if hasattr(i, "parent"):
                if i.parent == self:
                    Found.append(i.name)
        print("You found " + str(Found))

    def RemoveContent(self, content):
        for i in range(0, len(self.contents)):
            if self.contents[i] == content:
                del self.contents[i]
        if content.parent == self:
            content.parent = None

    def AddContent(self, content):
        self.contents.append(content)
        if hasattr(content, "parent"):
            content.parent = self
