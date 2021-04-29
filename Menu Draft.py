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
from util import alg_kruskal, alg_prim
# import numpy
# import pandas
import matplotlib.pyplot as plt

# set up the lists for the text of numbers in English and the menu options
# EngNum = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
menu_options = ["Import a new graph via csv file", "Output the adjacency list as a table", "Find MST usint algorithm 1", "Find MST usint algorithm 2", "Compare algorithms", "Save data to file in csv format", "Quit the Program"] 

# declare variables
welcome_message = "Welcome to the Minimum Connector Problem. \nPlease type the number below."
invalid_message = ""

def menu(invalid_message=invalid_message):

    # call clear_screen()
    clear_screen()

    # print the welcome message
    print(welcome_message)
    print(invalid_message)

    # print the menu through the list "menu_options" using for loop
    for i in range(len(menu_options)):
        print([i+1], menu_options[i])
	
    option = -1 # used to store the user's choice
	
	# while option is less than 1 or greater than 7, loop
	# used to validate user input
    while option < 1 or option > 7:	
		# get user's choice
        option = int(input("\nEnter your choice: "))
	
    
    return option


# to check which operation system is the user running this program on and clear the screen in the cell prompt
def clear_screen():

    # to check is the user using linux or mac. The os.name for lunux and mac is "posix".
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for other operation system, e.g. window.
        _ = os.system("cls")



#### FUNCTIONS MUST BE DEFINED FIRST

def set_parameters():
	print("1. This does not do anything yet")
	time.sleep(1)
# end of set_paramaters()


def calculate_data():
	print("2. This does not do anything yet")
	time.sleep(1)
# end of calculate_data()

def display_table():
	print("3. This does not do anything yet")
	time.sleep(1)
# end of display_data()

def display_graph():
	print("4. This does not do anything yet")
	time.sleep(1)
# end of display_graph


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
            # total_sales = calc_total_sales(sales_data)
            
            # show total sales
            print("Total Sales:",total_sales)
            
        elif option == 3: # Calculate mean sales for each employee
            # mean_sales = calc_mean_sales(total_sales)

            # show mean sales
            print("Mean Sales:", [round(mean, 2) for mean in mean_sales])
            
        elif option == 4: # Create graph of monthly sales
            print("option 4")

        elif option == 5: # Create graph of monthly sales
            print("option 5")

        elif option == 6: # Create graph of monthly sales
            print("option 6")
            
        else: # option 7 - exit in controlled manner

            # check if option is not 7 and update the variable
            if option != 7:
                invalid_message = "\nPlease trying again by entering a number between 1-7. \n"

                # go back to the start of the loop, instead of running the following program
                continue

            # set end_program Boolean to True
            end_program = True
            
            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()