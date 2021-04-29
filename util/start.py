# menu.py

import os
import util.config as cfg


def menu():

    option = -1 # used to store the user's choice

	# while option is less than 1 or greater than 7, loop
	# used to validate user input
    while option < 1 or option > len(cfg.menu_options):

        # call clear_screen()
        # clear_screen()

        # print the welcome message
        print(cfg.welcome_message)
        print(cfg.invalid_message)

        # print the menu through the list "menu_options" using for loop
        for i in range(len(cfg.menu_options)):
            print([i+1], cfg.menu_options[i])

        try:
            # get user's choice
            option = int(input("\nEnter your choice: "))

            # check if option is not 7 and update the variable
            if option < 1 or option > len(cfg.menu_options):
                cfg.invalid_message = "\nPlease trying again by entering a number between 1-7. \n"

        except ValueError:
            cfg.invalid_message = f"\n{cfg.valueError_message}"

    return option


# to check which operation system is the user running this program on and clear the screen in the cell prompt
def clear_screen():

    # to check is the user using linux or mac. The os.name for lunux and mac is "posix".
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for other operation system, e.g. window.
        _ = os.system("cls")