# Created by 2595161 from Durham University Interntaional Study Centre
# Last editied on 2021/05/20 18:00 GMT
# Copyright © 2021 2595161. All rights reserved.
# DUISC IFY Computer Science with Extended Research (CSER)
# Summative 2 - Minimum Connector Problem v1.0

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_CSCPR

# ------------------------------- Imported Packages -------------------------------

from util import config as cfg
from util.start import menu
from util.adj_list import open_csv_file, output_adj_list_table, save_csv
from util import alg_kruskal, alg_prim
from util import compare

# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program
    adjac_list = {} # set up variables to store adjac_list
    save_csv_list = []  # set up variables to store info about all adjac_list

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = menu()

        if option == 1: # import a graph from csv
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            adjac_list = open_csv_file(cfg.read_file_path)
            cfg.time_animation(3, "CSV file imported successfully. \n")
            cfg.countdown(4)

        elif option == 2: # output the adjacency list as a table
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                output_adj_list, output_adj_matrix = output_adj_list_table(adjac_list)
                print(f"Here is your adjacency list for your graph: \n{output_adj_list}")
                input("\nEnter to show the adjacency matrix") # pause the program
                cfg.clear_screen()
                print(f"Here is your adjacency matrix for your graph: \n{output_adj_matrix}")
                input("\nEnter to return to menu...") # pause the program
                cfg.countdown(4)

        elif option == 3: # find MST using kruskal's algorithm
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue

            k_alg_dict = alg_kruskal.kruskal(adjac_list)    # call function, and return a dict
            save_csv_list.append(k_alg_dict)    # append returned dict to list
            cfg.time_animation(3)
            print(f"Here are the results using {k_alg_dict['Algorithm']}:") # print information about the algorithm
            print(f"The MST is {k_alg_dict['Path Found']}")
            print(f"Weight of MST is {k_alg_dict['Minimal Weight']}")
            print(f"Computation time is {k_alg_dict['Computation Time']}s")
            input("\nEnter to return to menu...") # pause the program

        elif option == 4: # find MST using prim's algorithm
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue

            p_alg_dict = alg_prim.prim(adjac_list)  # call function, and return a dict
            save_csv_list.append(p_alg_dict)    # append returned dict to list
            cfg.time_animation(3)
            print(f"Here are the results using {p_alg_dict['Algorithm']}:") # print information about the algorithm
            print(f"The MST is {p_alg_dict['Path Found']}")
            print(f"Weight of MST is {p_alg_dict['Minimal Weight']}")
            print(f"Computation time is {p_alg_dict['Computation Time']}s")
            input("\nEnter to return to menu...") # pause the program

        elif option == 5: # compare algorithm running time
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            compared_csv = compare.compare()    # call function, and return a list
            save_csv_list = save_csv_list + compared_csv    # extend returned list to list

        elif option == 6: # save data to csv file
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            if save_csv_list == []:
                cfg.check_adjact_list("[3-5] to find MST of the graph", "MST")
                continue

            save_csv(cfg.write_file_path, save_csv_list)    # call function to save csv
            cfg.time_animation(3, "CSV file created successfully. \n")
            cfg.countdown(4)

        else: # option 7 - exit in controlled manner

            # set end_program Boolean to True
            end_program = True

            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        cfg.invalid_message = ""    # reset variable, to avoid invalid message in the next loop

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()
