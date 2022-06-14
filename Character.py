from Usables import Weapon
from Usables import Item
from Usables import UseApp


class Character:

    def __init__(self):
        self.inventory = {}

    def pickUpWeapon(self, weaponID: str, name: str, damageRange: list):
        if weaponID not in self.inventory:
            thisWeapon = Weapon(weaponID, name, damageRange)
            self.inventory[weaponID] = thisWeapon
            print("You drop your newly useless weapon on the ground with a *thud* in favor of this glorious weapon.")
            print(name + " has been added to your inventory.")
        else:
            print("You look down to see your dropped weapon disintegrate into dust.")
            print("'Ye gods! What devilry is this?!'")

    def useWeapon(self, weaponID: str) -> int:
        sword = self.inventory[weaponID]
        print("You swing your weapon with righteous fury!")
        return sword.weaponDamage()

    def pickUpItem(self, name: str, description: str):
        if name in self.inventory:
            print("You already picked that up!")
        else:
            thisItem = Item(name, description)
            self.inventory[name] = thisItem
            print("You pick up the " + name)
            thisItem.printItemDescription()

    def useItem(self, itemName: str, useCase: str, puzzleAns: dict) -> bool:
        if itemName == "Sword":
            print("Your weapon glances pitifully off of the " + useCase + ". Unfortunately violence can't solve every "
                                                                          "problem.")
            return False
        if itemName in self.inventory:
            item = self.inventory[itemName]
            myItem = item.useItem(useCase)
            if useCase in puzzleAns:
                myKey = puzzleAns[useCase]
                if myItem == myKey:
                    return True
            else:
                print("Nothing Happens...")
        else:
            print("You don't have a " + itemName + "!")


if __name__ == "__main__":
    puzzleAnswer = {"Wall": "Ladder"}
    angelo = Character()
    angelo.pickUpWeapon("Sword", "Big Sword", [50, 75])
    angelo.pickUpWeapon("Sword", "Big Sword", [50, 75])
    print(angelo.inventory)
    print(200 - angelo.useWeapon("Sword"))
    angelo.pickUpItem("Ladder", "Good for climbing over walls")
    print(angelo.inventory)
    wall = UseApp("Wall", "Ladder")
    angelo.useItem("Sword", "Wall", puzzleAnswer)
