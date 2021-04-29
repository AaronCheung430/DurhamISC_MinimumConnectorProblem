# DUISC IFY Computer Science with Extended Research (CSER)
# Summative 2 - Minimum Connector Problem

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_CSCPR

# ------------------------------- Imported Packages -------------------------------
import os
import sys
import time
import csv
from util import config as cfg
# from util import alg_kruskal, alg_prim
# import numpy
# import pandas
import matplotlib.pyplot as plt

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


# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = menu()

        if option == 1: # import data from csv
            # adj_list = open_csv_file(read_file_path)
            # print(adj_list)

            print("CSV file imported successfully.")

        elif option == 2: # Calculate total sales for each employee
            print("option 2")

        elif option == 3: # Calculate mean sales for each employee
            print("option 3")

        elif option == 4: # Create graph of monthly sales
            print("option 4")

        elif option == 5: # Create graph of monthly sales
            print("option 5")

        elif option == 6: # Create graph of monthly sales
            print("option 6")

        else: # option 7 - exit in controlled manner

            # set end_program Boolean to True
            end_program = True

            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()
