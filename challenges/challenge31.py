#!/usr/bin/env python3
import random

def main():
    num = random.randrange(1,21)
    wordbank= ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)
    choice= int(input("Pick a student number!"))
    student_name= tlgstudents[choice]

    print(f"{tlgstudents[num - 1]} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
