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

    while True:
        try:
            guess = int(input("Please enter a number inclusive of your min and max range values: "))
            if guess >= 1 and guess <=num_range:
                break
            else:
                print(f"Invalid number, please enter a number from 1 to {num_range}")
        except:
            print("Please enter an integer, try again")

   #simple counter for number of guesses
    i=0

    #loop keeps running until user gets the guess correct
    while num!=guess:
        i+=1
        if guess>num:
            #if the guess is to high
            print("You are too high!")
            guess = guess_val(i,num_range)
        
        elif guess<num:
            #if the guess is to low
            print("You are too low!")
            guess = guess_val(i,num_range)
        else:
            break
    print("Your guess is correct!")

def guess_val(x,y):
    while True:
        try:
            new_guess = int(input(f"You have made {x} guesses, please guess again: "))
            if new_guess >= 1 and new_guess <= y:
                return new_guess
            else:
                print("Invalid number, please try again: ")
        except:
            print("Please enter an integer, try again: ")


main()


