# import modules
import os
import time
import csv
import numpy


# set up the lists for the text of numbers in English and the menu options
EngNum = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
menu_options = ["Import a new graph via csv file", "Output the adjacency list as a table", "Find MST usint algorithm 1", "Find MST usint algorithm 2", "Compare algorithms", "Save data to file in csv format", "Quit the Program"] 


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



def main():
    # code to be added soon
    #### MAIN PROGRAM

    # declare variables
    program_info = "DUISC Python Example \nBasic Menu\n"
    user_command = "nothing"
    print(user_command, "testing")
    print("hello")
    # main loop: get input command from users and jump to required option
    # code in this loop is repeated after every user command, until the user enters 'quit'

    while (user_command != 'q'):
        
        
        # clear the console using the system terminal command 'clear'
        # note: this only works for Linux and macOS; a different command would be required for Windows
        # os.system('clear')

        # show the welcome message/program information
        print(program_info)

        # print the menu through the list "menu_options" using for loop
        for i in range(0,7):
            print([i+1], menu_options[i])

        # get command from user
        user_command = input("\nenter command: ")
        
        # check user command
        if user_command=='1':
            set_parameters()
            
        elif user_command=='2':
            calculate_data()
            
        elif user_command == "3":
            display_table()
            
        elif user_command == "4":
            display_graph()
        
        else:
            if user_command != "q":
                print("Invalid command")
                time.sleep(1)	

    # end of main loop: user has quit
    print("quitting...");
    print("program ended");
    print("goodbye");

    #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()