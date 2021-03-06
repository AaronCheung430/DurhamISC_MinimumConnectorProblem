# start.py
# menu() functions for main program and allow user to enter choice

import util.config as cfg

# to show menu options
def menu():

    option = -1 # used to store the user's choice

	# while option is less than 1 or greater than 7, loop
	# used to validate user input
    while option < 1 or option > len(cfg.menu_options):

        # call clear_screen()
        cfg.clear_screen()

        # print the messages
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
                cfg.invalid_message = f"\nPlease trying again by entering a number between 1-{len(cfg.menu_options)}. \n"

        # handle the error if an exception occurs, to prevent the program from being terminating
        except ValueError:
            cfg.invalid_message = f"\n{cfg.valueError_message}"

    return option   # return user's choice

