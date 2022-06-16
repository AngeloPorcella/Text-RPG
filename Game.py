from Character import *

charName = str(input("What is your name?"))
print(charName)
CharacterHP = 100
player = Character(charName)

def repl():
    print("---List of Commands---")
    print("?\t\tRe-Print Commands")
    print("inspect\t\tInspect Item")
    print("use\t\tUse Item on Object")
    print("pick up\t\t Pick up Item")
    print("look\t\t Observes Environment")
    print("items\t\tGet Description of inventory Item")
    print("exit\t\tExit the Game")

# Template for REPL
x = True
while x is True:
    action = input("What do you do?")
    if action == "?":
        repl()
    elif action == "inspect":
        inspect = input("What would you like to inspect?")
        if inspect == "INSERT INSPECTABLE":
            print("Give Description of inspect")
        else:
            print("Nothing of note")
    elif action == "use":
        itemName = input("What item would you like to use?")
        useCase = input("What would you like to use the item on?")
        player.useItem(itemName, useCase, puzzleAnswer)
        if player.useItem(itemName, useCase, puzzleAnswer) is True:
            print("INSERT FLAVOR TEXT TO MOVE ON TO NEXT LOOP")
            openDoor = True
            # BREAK LOOP
        else:
            continue
    elif action == "pick up":
        itPick = input("What do you want to pick up?")
        if itPick == "INSERT ITEM IN ROOM":
            itDescript = "INSERT ITEM DESCRIPTION"
            player.pickUpItem(itPick, itDescript)
        elif itPick == "INSERT WEAPON IN ROOM":
            damage = []
            player.pickUpWeapon("Sword", itPick, damage)
        else:
            print("You can't pick that up!")
    elif action == "look":
        print("INSERT FLAVOR TEXT FOR ROOM")
    elif action == "items":
        readItem = input("Which item do you want to know about?")
        if readItem in player.inventory:
            itemObj = player.inventory[readItem]
            itemObj.printItemDescription()
        else:
            print("You don't have a(n) " + readItem + "!")
    elif action == "exit":
        raise SystemExit
    else:
        print("Please enter a valid command...")
# Template for REPL

def room1():
    print("You awaken in a prison cell.")
    puzzleAnswer = {"Guard": ["Hook"]}
    openDoor = False
    while not openDoor:
        action = input("What do you do?")
        if action == 3:
            pass
