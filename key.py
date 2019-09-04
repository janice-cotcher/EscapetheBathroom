class Key():
    def __init__(self, name, id):
        self.open_methods = ["Take", "Use"]  # Methods  to be used by Plyr
        self.name = name  # The Name
        self.id = id  # The Id
        self.parent = None  # The Parent

    def Take(self, Plyr, instances):
        if self in Plyr.inventory:
            print("You already have " + self.name)
        else:
            print("You take " + self.name)
            if self.parent:
                if hasattr(self.parent, "inventory"):
                    for i in range(0, len(self.parent.inventory)):
                        if self.parent.inventory[i] == self:
                            del self.parent.inventory[i]
            self.parent = Plyr
            Plyr.inventory.append(self)

    def Use(self, Plyr, instances):
            if not self in Plyr.inventory:
                print("You do not have this key!")
                return 1
            # Split User Input
            splitt = input("What would you " +
                           "like to use the key on? ").split(" ")
            if splitt[0].lower() == "exit":
                exit()
            instances_names = []  # Names of all the instances
            for i in instances:
                instances_names.append(i.name.lower())
            alt1 = None  # The Obj that the key will be used on
            if splitt[0].lower() in instances_names:
                for i in instances:
                    if i.name.lower() == splitt[0].lower():
                        alt1 = i
            else:
                # All instances names that match the user input
                matching = [s for s in instances_names if
                            splitt[0].lower() in s]
                print("Did not find '" + splitt[0] + "' did you mean: " +
                      str(matching)+"?")
                return 1
            alt1.UseKey(self)
