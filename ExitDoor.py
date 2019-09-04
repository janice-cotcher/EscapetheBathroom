from door import Door


class ExitDoor(Door):
    def Use(self, Plyr, instances):
        if self.locked != False:
            print(self.name + " is locked.")
            return 1
        else:
            print("You've escaped the bathroom!, game over.")
            exit()
