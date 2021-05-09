# DUISC IFY Computer Science with Extended Research (CSER)
# Summative 2 - Minimum Connector Problem

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_CSCPR

# ------------------------------- Imported Packages -------------------------------

from util import config as cfg
from util import start as strt
from util.adj_list import open_csv_file, output_adj_list_table
from util import alg_kruskal, alg_prim
# from util import compare
# import matplotlib.pyplot as plt


# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program
    adjac_list = {}

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = strt.menu()

        if option == 1: # import a graph from csv
            adjac_list = open_csv_file(cfg.read_file_path)
            cfg.clear_screen()
            # cfg.time_animation(3, "CSV file imported successfully.")
            print(adjac_list)
            # cfg.countdown(4)

        elif option == 2: # output the adjacency list as a table
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                output_adj_list, output_adj_matrix = output_adj_list_table(adjac_list)
                cfg.clear_screen()
                print(f"Here is your adjacency list for your graph: \n{output_adj_list}")
                input("\nEnter to show the adjacency matrix") # pause the program
                cfg.clear_screen()
                print(f"Here is your adjacency matrix for your graph: \n{output_adj_matrix}")
                input("\nEnter to return to menu...") # pause the program
                cfg.countdown(4)

        elif option == 3: # find MST using kruskal's algorithm
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                k_alg_dict = alg_kruskal.kruskal(adjac_list)    # call function, and return a dict
                print(f"Here are the results using {k_alg_dict['Algorithm']}:") # print information about the algorithm
                print(f"The MST is {k_alg_dict['Path Found']}")
                print(f"Weight of MST is {k_alg_dict['Minimal Weight']}")
                print(f"Computation time is {k_alg_dict['Computation Time']}")
                input("\nEnter to return to menu...") # pause the program

        elif option == 4: # find MST using prim's algorithm
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                p_alg_dict = alg_prim.prim(adjac_list)  # call function, and return a dict
                print(f"Here are the results using {p_alg_dict['Algorithm']}:") # print information about the algorithm
                print(f"The MST is {p_alg_dict['Path Found']}")
                print(f"Weight of MST is {p_alg_dict['Minimal Weight']}")
                print(f"Computation time is {p_alg_dict['Computation Time']}")
                input("\nEnter to return to menu...") # pause the program

        elif option == 5: # compare algorithm running time

            print("option 5")

        elif option == 6: # save data to csv file

            print("option 6")

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
