# DUISC IFY Computer Science with Extended Research (CSER)
# Summative 2 - Minimum Connector Problem

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_CSCPR

# ------------------------------- Imported Packages -------------------------------

from util import config as cfg
from util import start as strt
from util.adj_list import open_csv_file, output_adj_list_table
from util import alg_kruskal
# , alg_prim
# import numpy
# import pandas
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
            cfg.time_animation(3, "CSV file imported successfully.")
            print(adjac_list)
            cfg.countdown(4)

        elif option == 2: # output the adjacency list as a table
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                output_adj = output_adj_list_table(adjac_list)
                print(output_adj)

        elif option == 3: # find MST using kruskal's algorithm
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                k_mst, k_weight, k_time = alg_kruskal.kruskal(adjac_list)
                print("Here are the results using kruskal's Algorithm:")
                print("The MST is", k_mst)
                print("Weight of MST is", k_weight)
                print("Computation time is", k_time)
                input("\nEnter to return to menu...") # pause the program to show graph

        elif option == 4: # find MST using prim's algorithm
            if adjac_list == {}:
                cfg.check_adjact_list()
                continue
            else:
                print("option 4")

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
