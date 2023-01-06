#!/usr/bin/env python3
""" range challenge """

def main():
    ending = 0
    while True:
        try:
            ending = int(input("Please enter an integer greater than 1 and less than 101: "))
            if ending < 101 and ending > 1:
                break
            else:
                print("Invalid number")
        except:
            print("You did not enter an integer, try again")
    
    for x in reversed(range(ending)):
        print(f"{x} bottles of beer on the wall!\n{x} bottles of beer on the wall!\n{x} bottles of beer!\nYou take one down, pass it around!\n")
main()
