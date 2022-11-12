#!/usr/bin/env python3
# Created By: Nolan Shami
# Date: November 12th, 2022
# This program gets the user's positive integer,
# It then uses a for loop to calculate and display
# the square, power of 2, from 0 to the user's positive integer.


def main():

    # gets the user's positive integer
    user_number_as_string = input("Enter a positive integer: ")

    # turns input into an integer
    try:
        user_number_as_int = int(user_number_as_string)

        # if statement to check if user's input is less than 0
        if user_number_as_int < 0:
            print("")
            print("This is not positive...please enter a positive integer!")

        # process
        # if user number is more than 0 then the program will progress to the for loop
        elif user_number_as_int >= 0:
            # Loops and lists the program and multiplies 
            # the counter time to the power of 2 from 0 to the user input
            for counter in range(user_number_as_int + 1):
                power_of_two = counter**2
                print()
                print("{}^2 = {}.".format(counter, power_of_two))
    # exception for any other erroneous input
    except Exception:
        print()
        print("I feel like that might be a decimal or a text...please enter a positive integer!")
    finally:
        print()
        print("Thanks for playing this wonderful, math related, game!")


if __name__ == "__main__":
    main()
