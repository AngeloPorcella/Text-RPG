from Usables import Weapon
from Usables import Item



class Character:

    def __init__(self, charName: str):
        self.charName = charName
        self.inventory = {}

    def pickUpWeapon(self, weaponID: str, name: str, damageRange: list):
        if name not in self.inventory:
            thisWeapon = Weapon(weaponID, name, damageRange)
            self.inventory["Sword"] = thisWeapon
            # print("You drop your newly useless weapon on the ground with a *thud* in favor of this glorious weapon.")
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

    def useItem(self, itemName: str, useCase: str, puzzleAns: dict) -> bool:
        if itemName == "Sword":
            print("Your weapon glances pitifully off of the " + useCase + ". Unfortunately violence can't solve every "
                                                                          "problem.")
            return False
        elif itemName in self.inventory:
            if itemName in puzzleAns[useCase]:
                return True
            else:
                return False
        else:
            print("You don't have a " + itemName + "!")
            return False

    def printInventory(self) -> None:
        inv = self.inventory.keys()
        for item in inv:
            print(item)

        # A spoon is a sword now!


if __name__ == "__main__":
    """puzzleAnswer = {"Wall": "Ladder"}
    angelo = Character("Angelo")
    angelo.pickUpWeapon("Sword", "Big Sword", [50, 75])
    angelo.pickUpWeapon("Sword", "Big Sword", [50, 75])
    print(angelo.inventory)
    print(200 - angelo.useWeapon("Sword"))
    angelo.pickUpItem("Ladder", "Good for climbing over walls")
    print(angelo.inventory)
    wall = UseApp("Wall", "Ladder")
    angelo.useItem("Sword", "Wall", puzzleAnswer)"""
