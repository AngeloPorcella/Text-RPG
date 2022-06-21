from Character import *
import random
import time
from HangmanMiniGame import *

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
    print("exit\t\t\tExit the Game")
    print("_______________________")


# repl Template

def combatHeal(playerHealth: int) -> int:
    """Increases health in a range selected randomly returns updated health"""
    if playerHealth < 100:
        healAmt = random.randint(25, 50)
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
    print("You have slain the enemy. Sometimes violence is the answer...")
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
                print("\n\nYou manage to fish the key out of the guard's pocket.\n"
                      "It slides into the lock with ease.\n"
                      "As you turn the lock and open the door a loud squeak from the rusty hinges awakens the guard.\n"
                      "'Huh? We have an escapee!!'\n"
                      "The guard pulls out a wooden baton and rushes you.")
                hp = combatLoop(13, hp, "Drunken Guard", 3, 8)
                openDoor = True
                # BREAK LOOP
            elif player.useItem(itemName, useCase, puzzleAnswer2) is True:
                print("\n\nThe guard lets out a bloodcurdling cry \n'what the hell?? I don't get paid enough for this!'\n"
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
            print("\n\nYou are within the confines of a rusty cell. A drunken, sleeping guard sits snoring outside of your "
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


def room2(playerHP: int) -> int:
    hp = playerHP
    puzzleAnswer = {"cannon": ["candle"]}
    print("You enter what appears to be a guard barrack.")
    openDoor = False
    while not openDoor:
        action = input("What do you do?\n-> ")
        if action == "?":
            repl()
        elif action == "inventory":
            player.printInventory()
        elif action == "inspect":
            inspect = input("What would you like to inspect?\n-> ")
            if inspect == "cannon":
                print("A cannon curiously pointed directly at a wall...\nEven curiouser, the cannon appears to be "
                      "loaded!")
            elif inspect == "chalkboard" or inspect == "chalk board" or inspect == "board":
                play = input("\n\nA set of lines appear on the board along with a crudely drawn hangman's platform.\n"
                             "Would you like to play? (y/n)")
                if play == "n":
                    print("The board clears.\nThe words 'Whatever man, You do you...' write themselves before your "
                          "eyes.")
                    continue
                if play == "y":
                    print("Let's Play!")
                    result = playHangMan(wordPick())
                    if result == "winner":
                        print("Congratulations! Here is your prize.")
                        player.pickUpWeapon("Sword", "Lightsaber", [9998, 9999])
                    elif result == "loser":
                        print("'Bummer!'")
                        print("The board wipes itself clean.")
            elif inspect == "candle" or inspect == "candle stick":
                print("A lit candle sits upon the table.")
            elif inspect == "sword" or inspect == "long sword":
                print("A shiny sword... Looks sharp!")
            else:
                print("Nothing of interest.")
        elif action == "use":
            itemName = input("What item would you like to use?\n-> ")
            useCase = input("What would you like to use the item on?\n-> ")
            if itemName == "long sword":
                print("Nothing Happens...")
                continue
            if player.useItem(itemName, useCase, puzzleAnswer) is True:
                print("Sparks fly from the fuze as it is lit with the candle. The cannon fires through the wall\n"
                      "in an explosion of brick and wooden shrapnel. Coincidentally the cannon ball flies across\n"
                      "a courtyard and directly into the big bad evil guy's lair.\n\n")
                time.sleep(8)
                print("****")
                print("Meanwhile in the evil king's castle...")
                print("****\n\n")
                time.sleep(3)
                print("The evil king lies in his evil royal bathtub thinking evil thoughts")
                print("'Maybe i'll enslave some children today, that sounds fun' he muses to himself, in an evil "
                      "tone...\n")
                time.sleep(8)
                print("suddenly...\n")
                time.sleep(3)
                print("The wall explodes in a violent crash and the evil king is instantly vaporized.")
                print("You have saved the day!\n\n")
                time.sleep(10)
                print("What's this? The evil king's ghost rises from the fleshy pile of remains and flies out into\n"
                      "the courtyard!")
                print("'Myahh!' The ghost yells, evil in it's voice.")
                time.sleep(5)
                openDoor = True
                # BREAK LOOP
            else:
                print("Nothing happens...")
                continue
        elif action == "pick up":
            itPick = input("What do you want to pick up?\n-> ")
            if itPick == "candle" or itPick == "candle stick":
                itDescript = "A lit candle."
                player.pickUpItem(itPick, itDescript)
            elif itPick == "sword" or itPick == "long sword":
                damage = [20, 30]
                print("You pick up the " + itPick + ". This could come in handy...")
                player.pickUpWeapon("Sword", "long sword", damage)
            else:
                print("You can't pick that up!")
        elif action == "look":
            print("You appear to be in some sort of guard barrack. There is a table in the center of the room with a "
                  "long sword "
                  "resting on top next to a lit candlestick,\nthe other guards here must have just left.\n"
                  "A cannon sits nearby.\nA magical chalkboard hangs on a wall.")
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
