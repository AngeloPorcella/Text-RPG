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

    def useItem(self, useApp: str) -> str:
        itemName = self.itemName
        print("You use the " + self.itemName + " on the " + useApp + ".")
        return itemName


"""sword1 = Weapon("Long Sword", [5, 10])
sword1.printWeaponStats()
sword1.weaponDamage()"""
