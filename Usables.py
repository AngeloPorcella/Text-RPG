"""Classes for items"""
import random


class Weapon:

    def __init__(self, weaponID: str, name: str, damageRange: list):
        self.name = name
        self.damageRange = damageRange
        self.weaponID = weaponID

    def printWeaponStats(self) -> None:
        print(self.name + " Damage: " + str(self.damageRange[0]) + "-" + str(self.damageRange[1]))

    def weaponDamage(self) -> int:
        damageNum = random.randint(self.damageRange[0], self.damageRange[1])
        print("You did " + str(damageNum) + " damage!")
        return damageNum


class Item:

    def __init__(self, itemName: str, description: str):
        self.itemName = itemName
        self.description = description

    def printItemDescription(self):
        print(self.itemName + ": " + self.description)

"""    def useItem(self, useApp: str) -> str:
        itemName = self.itemName
        print("You use the " + self.itemName + " on the " + useApp + ".")
        return itemName"""

class UseApp:

    def __init__(self, useAppName: str, key: str):
        self.useAppName = useAppName
        self.key = key

    def getUseKey(self) -> str:
        thisKey = self.key
        return thisKey

    def getUseName(self) -> str:
        return self.useAppName


if __name__ == "__main__":
    sword1 = Weapon("Sword", "Big Ass Sword", [69, 420])
    item1 = Item("Book", "Look at all these fucking words!")
    sword1.printWeaponStats()
    sword1.weaponDamage()
    item1.printItemDescription()
