from Character import *
import random
import time

player = Character("Hans")


def repl():
    print("_______________________")
    print("---List of Commands---")
    print("?\t\t\t\tRe-Print Commands")
    print("inspect\t\t\tInspect Item")
    print("use\t\t\t\tUse item on Object")
    print("pick up\t\t\tPick up Item")
    print("look\t\t\tObserves Environment")
    print("inventory\t\tGet list of inventory Items")
    print("items\t\t\tGet Description of inventory Item")
    print("exit\t\t\tExit the Game")
    print("_______________________")


# repl Template

def combatHeal(playerHealth: int) -> int:
    """Increases health in a range selected randomly returns updated health"""
    if playerHealth < 100:
        healAmt = random.randint(5, 15)
        playerHealth += healAmt
        if playerHealth > 100:
            playerHealth = 100
        print("You heal " + str(healAmt) + " health points. Your total health is now " + str(playerHealth))
        return playerHealth
    else:
        print("Your Health is Full!")


def combatLoop(enemyHP: int, playerHP: int, enemyName: str, enemyMinDmg: int, enemyMaxDmg: int) -> int:
    """A combat encounter. returns player health."""
    hp = playerHP
    print("The " + enemyName + " raises their weapon and charges you.")
    print("attack\t\t\tSwing Weapon at Enemy")
    print("heal\t\t\tDrink Health Potion")
    if "Sword" not in player.inventory:
        print("Without a weapon you are easily overpowered and killed quickly.")
        print("You DIED!")
        print("Please play again!")
        raise SystemExit
    while enemyHP > 0:
        if hp > 0:
            # player combat turn
            combatAction = input("What action do you take?\n-> ")
            if combatAction == "attack":
                damage = player.useWeapon("Sword")
                enemyHP -= damage
            if combatAction == "heal":
                hp = combatHeal(hp)
        else:
            print("You DIED!")
            print("Please play again!")
            raise SystemExit
        time.sleep(0.75)
        if enemyHP > 0:
            damageTaken = random.randint(enemyMinDmg, enemyMaxDmg)
            hp -= damageTaken
            print("The " + enemyName + " takes a swing at you.")
            print("You have taken " + str(damageTaken) + " damage. \nYour current health is " + str(hp))
            time.sleep(0.75)
    print("You have slayed the enemy. Sometimes violence is the answer...")
    return hp


def roomTemplate():
    puzzleAnswer = {"fill": "this"}
    openDoor = False
    while openDoor is not True:
        action = input("What do you do?\n-> ")
        if action == "?":
            repl()
        elif action == "inventory":
            player.printInventory()
        elif action == "inspect":
            inspect = input("What would you like to inspect?\n->")
            if inspect == "INSERT INSPECTABLE":
                print("Give Description of inspect")
            else:
                print("Nothing of note")
        elif action == "use":
            itemName = input("What item would you like to use?\n-> ")
            useCase = input("What would you like to use the item on?\n-> ")
            player.useItem(itemName, useCase, puzzleAnswer)
            if player.useItem(itemName, useCase, puzzleAnswer) is True:
                print("INSERT FLAVOR TEXT TO MOVE ON TO NEXT LOOP")
                openDoor = True
                # BREAK LOOP
            else:
                continue
        elif action == "pick up":
            itPick = input("What do you want to pick up?\n-> ")
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
            readItem = input("Which item do you want to know about?\n-> ")
            if readItem in player.inventory:
                itemObj = player.inventory[readItem]
                itemObj.printItemDescription()
            else:
                print("You don't have a(n) " + readItem + "!")
        elif action == "exit":
            raise SystemExit
        else:
            print("Please enter a valid command...")


def room1(playerHP: int) -> int:
    hp = playerHP
    repl()
    print("You awaken in a prison cell.")
    puzzleAnswer = {"guard": ["wire"]}
    puzzleAnswer2 = {"guard": ["bucket"]}
    openDoor = False
    while not openDoor:
        action = input("What do you do?\n-> ")
        if action == "?":
            repl()
        elif action == "inventory":
            player.printInventory()
        elif action == "inspect":
            inspect = input("What would you like to inspect?\n-> ")
            if inspect == "bed" or inspect == "lumpy bed":
                print("You rummage through the straw mattress. You discover a twisted piece of metal wire amongst "
                      "the "
                      "filling.\n No wonder you've had trouble sleeping...")
            elif inspect == "guard" or inspect == "sleeping guard":
                print("A guard in a drunken stupor sits on a wooden stool just out of arms reach. You notice a shiny\n "
                      "key barely visible in his pocket.")
            elif inspect == "bucket":
                print("A bucket for your 'waste'. pretty disgusting.")
            else:
                print("Nothing of interest.")
        elif action == "use":
            itemName = input("What item would you like to use?\n-> ")
            useCase = input("What would you like to use the item on?\n-> ")
            if itemName == "spoon":
                print("The guard is out of reach!")
                print("Nothing Happens...")
                continue
            if player.useItem(itemName, useCase, puzzleAnswer) is True:
                print("You manage to fish the key out of the guard's pocket.\n"
                      "It slides into the lock with ease.\n"
                      "As you turn the lock and open the door a loud squeak from the rusty hinges awakens the guard.\n"
                      "'Huh? We have an escapee!!'\n"
                      "The guard pulls out a wooden baton and rushes you.")
                hp = combatLoop(13, hp, "Drunken Guard", 3, 8)
                openDoor = True
                # BREAK LOOP
            elif player.useItem(itemName, useCase, puzzleAnswer2) is True:
                print("The guard lets out a bloodcurdling cry \n'what the hell?? I don't get paid enough for this!'\n"
                      "He stands up, and as he runs towards the door a key falls onto the floor within arms reach.\n"
                      "The key fits nicely into the cell door and you leave the room.")
                openDoor = True
                # BREAK LOOP
            else:
                print("Nothing happens...")
                continue
        elif action == "pick up":
            itPick = input("What do you want to pick up?\n-> ")
            if itPick == "bucket":
                itDescript = "Filled with your own waste. Absolutely disgusting."
                player.pickUpItem(itPick, itDescript)
            elif itPick == "wire" or itPick == "metal wire":
                print("You grab the wire and quickly twist it into a small hook before slipping it into your pocket.")
                itDescript = "A wire you have fashioned into a hook. Useful."
                player.pickUpItem("wire", itDescript)
            elif itPick == "spoon" or itPick == "rusty spoon":
                damage = [3, 5]
                print("You pick up the " + itPick + ". This could come in handy...")
                player.pickUpWeapon("Sword", "spoon", damage)
            else:
                print("You can't pick that up!")
        elif action == "look":
            print("You are within the confines of a rusty cell. A drunken, sleeping guard sits snoring outside of your "
                  "cell.\nA lumpy bed lies in a corner of the small confined space, while a bucket sits "
                  "opposite. \n"
                  "A rusty spoon you use to eat whatever slop they decide to feed you rests near "
                  "the bed on the floor. Not exactly luxury living.")
        elif action == "items":
            readItem = input("Which item do you want to know about?\n-> ")
            if readItem in player.inventory:
                itemObj = player.inventory[readItem]
                itemObj.printItemDescription()
            else:
                print("You don't have a(n) " + readItem + "!")
        elif action == "exit":
            raise SystemExit
        else:
            print("Please enter a valid command...")
    return hp


if __name__ == "__main__":
    room1(hp)
    print(str(hp))
