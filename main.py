# Course: CS 30
# Student example of a text-based adventure game
from room import Room
from player import Player
from storage import Storage
from key import Key
from door import Door
from ExitDoor import ExitDoor
import os


Plyr = Player("Null")  # Init Plyr Object

instances = []  # List Of Objects


def rec():
    """ handles user input """
    global instances
    splitt = input().split(" ")  # User Input split
    if splitt[0].lower() == "exit":
        exit()
    if len(splitt) < 2:
        return 1
    instances_names = []  # The names of all the instances
    for i in instances:
        instances_names.append(i.name.lower())
    alt1 = None  # The Object That The Method Will Be Used On
    if splitt[1].lower() in instances_names:
        for i in instances:
            if i.name.lower() == splitt[1].lower():
                alt1 = i
    else:
        # All Instance Names That Match The User Input
        matching = [s for s in instances_names if splitt[1].lower() in s]
        print("Did not find '" + splitt[1] +
              "' did you mean: " + str(matching)+"?")
        return 1
    methods = []  # List Of usable methods
    for i in alt1.open_methods:
        methods.append(i.lower())
    if splitt[0].lower() in methods:
        for i in alt1.open_methods:
            if i.lower() == splitt[0].lower():
                alt2 = i  # The Method That Will Be Used
        return [alt1, alt2]
    else:
        print("Did not find '" + splitt[0] +
              "' did you mean: " + str(alt1.open_methods))
        return 1


def Start():
    """ Start of game || Sets the room up """
    global Plyr, instances
    print("Objective: Escape the room")
    print("Commands:")
    print("       search, take, use, examine, exit")
    print("       Try 'examine player'")
    Plyr = Player("Player")  # Player Obj
    Exit = ExitDoor("Door_Exit")  # Door_Exit Obj
    instances.append(Plyr)
    instances.append(Exit)
    Bathroom = Room("Bathroom")  # Room Obj
    Plyr.moveTo(Bathroom)
    instances.append(Bathroom)

    Cupboard_1 = Storage("Left_Cupboard")  # Storage Obj
    instances.append(Cupboard_1)
    Cupboard_2 = Storage("Right_Cupboard")  # Storage Obj
    instances.append(Cupboard_2)

    Cupboard_1.locked = True  # Whether its locked or not
    Cupboard_1.lock_id = 61  # The Id to unlock it
    Cupboard_2.lock_id = 312  # The Id to unlock it
    Cupboard_2.locked = True  # Whether its locked or not

    Key_1 = Key("Silver_Key", Cupboard_1.lock_id)  # Key Obj
    instances.append(Key_1)
    Plyr.inventory.append(Key_1)
    Key_1.parent = Plyr  # The Parent Of The Key
    Exit.lock_id = 31  # The id to unlock it
    Exit.locked = True  # Whether its locked or not
    Key_2 = Key("Gold_Key", Exit.lock_id)  # Key Obj
    instances.append(Key_2)
    Cupboard_1.AddContent(Key_2)

    Bathroom.AddContent(Cupboard_1)
    Bathroom.AddContent(Cupboard_2)
    Bathroom.AddContent(Exit)
    while True:
        op = rec()  # Output from rec() function
        if isinstance(op, list):
            if len(op) >= 2:
                # String to be executed
                strng = ("op[0]" + "." + op[1] + "(Plyr, instances)")
                exec(strng)
Start()
