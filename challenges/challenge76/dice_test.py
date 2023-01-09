#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from morecheats.py (this is in the local directory)
from morecheats import Player
from morecheats import Cheat_Swapper
from morecheats import Cheat_Loaded_Dice
from morecheats import Cheat_Mulligan
from morecheats import Cheat_Extra_Die
from morecheats import Cheat_Lucky_Die
from morecheats import Cheat_Saboteur

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Mulligan() # if total dice is under 9, get a re-roll
    cheater2 = Cheat_Lucky_Die() # first die roll is lucky and can't roll under 3

    # both players take turns
    cheater1.roll()
    cheater2.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()

