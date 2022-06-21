from Game import *


def main():
    hp = 100
    hp = room1(hp)
    print("\n\n")
    hp = room2(hp)
    print("\n\nYou leap down into the royal courtyard just in time to see a ghostly figure flying towards you!\n\n")
    time.sleep(1)
    combatLoop(115, hp, "Evil Ghost", 20, 35)
    print("\n\nYou did it! The day is saved! Thanks for playing!")
    raise SystemExit


main()
