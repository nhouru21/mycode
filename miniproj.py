#!/usr/bin/python3
'''mini project description'''
import random

def main():

    #user gets to pick the range of numbers to guess from
    print("Welcome to the number guessing game where you get to pick the range of numbers you can guess from!")

    #validation that user enters an int and is at least 2 or greater
    while True:
        try:
            num_range = int(input("Please enter the ending number of your number range (e.g. if you pick 1000, the range is from 1-1000)")) 
            if num_range > 1:
               break
            else:
                print("Invalid number, please try again")
        except:
            print("Please enter an integer, try again")
            

    num = random.randrange(1,num_range)
    guess = int(input("Please enter a number inclusive of your min and max range values: "))
    #simple counter for number of guesses
    i=0

    #loop keeps running until user gets the guess correct
    while num!=guess:
        i+=1
        print(i)
        if guess>num:
            #if the guess is to high
            print("You are too high!")
            guess = int(input(f"You have made {i} guesses, please guess again: "))
        elif guess<num:
            #if the guess is to low
            print("You are too low!")
            guess = int(input(f"You have made {i} guesses, please guess again: "))
        else:
            break
    print("Your guess is correct!")

'''
I was wanting to add more vaildation here for the guesses but ran out of time
def guess_val(i,guess):
    while True:
        try:
            guess = int(input(f"You have made {i} guesses, please guess again"))
            if guess >= 1:
                break
            else:
                print("Invalid number, please try again")
        except:
            print("Please enter an integer, try again")
'''

main()


