# import modules
import os
import time
import csv
import numpy


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

        # show menu options in console
        print("1: Set parameters")
        print("2: Calculate data")
        print("3: Display data in table")
        print("4: Display data as graph")
        print("q: quit program")

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