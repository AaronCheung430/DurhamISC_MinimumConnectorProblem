# config.py
# initialise most variable I needed in the project

import os
from time import sleep

# set up the lists for the menu options
menu_options = ["Import a new graph via csv file", "Output the adjacency list as a table", "Find MST using Kruskal's Algorithm", "Find MST using Prim's Algorithm", "Compare algorithms", "Save data to file in csv format", "Quit the Program"]

# declare variables and
valueError_message = "Oops! That was a text. Please try again with a valid number... \n"
welcome_message = "Welcome to the Minimum Connector Problem. \nPlease type the number below."
invalid_message = ""

read_file_path = "data/test_graph.csv" # file path for file to be read
# read_file_path = "data/C1_V5_E8.csv"

# to display invalid message, after check is graph exist in the main program
def check_adjact_list():
    global invalid_message
    clear_screen()
    invalid_message = f"\nPlease select '[1] {menu_options[0]}' to import a new graph first. \n"
    print(f"Your graph is empty. \nPlease return to the main menu and choose '[1] {menu_options[0]}' to import a new graph and come back later. \n")
    countdown(5)

# to check which operation system is the user running this program on and clear the screen in the cell prompt
def clear_screen():

    # to check is the user using linux or mac. The os.name for lunux and mac is "posix".
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # for other operation system, e.g. window.
        _ = os.system("cls")

# to preform the time delay animation
def time_animation(t, message="Done!      "):

    for i in range(t):
        for frame in r'-\|/-\|/':
            # back up one character then print our next frame in the animation
            print('\rloading ', frame, sep='', end='', flush=True)
            sleep(0.125)

    print("\r" + message)

# to countdown, get parameters about how many seconds is the countdown going to run, and the message that will show.
def countdown(s, message = "Returning to main menu in"):

    # print countdown on the same line, until s is 0
    while s:
        timer = "{:01d}".format(s)
        print(message, timer, end="\r")
        sleep(1)
        s -= 1