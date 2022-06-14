from Usables import Weapon
from Usables import Item


class Character:

    def __init__(self, hp: int):
        self.hp = hp
        self.inventory = {}

    def pickUpWeapon(self, weaponID: str, name: str, damageRange: list):
        thisWeapon = Weapon(weaponID, name, damageRange)
        self.inventory[weaponID] = thisWeapon

    def useWeapon(self, weaponID: str) -> int:
        sword = self.inventory[weaponID]
        return sword.weaponDamage()

    def pickUpItem(self, name: str, description: str):
        thisItem = Item(name, description)
        self.inventory[name] = thisItem

    def useItem(self, itemName: str, useCase: str) -> None:
        myItem = self.inventory[itemName]
        return myItem.useItem(useCase)


if __name__ == "__main__":
    angelo = Character(100)
    angelo.pickUpWeapon("Sword", "Big Sword", [50, 75])
    print(angelo.inventory)
    print(200 - angelo.useWeapon("Sword"))
    angelo.pickUpItem("Ladder", "Good for climbing over walls")
    print(angelo.inventory)
    angelo.useItem("Ladder", "Wall")
