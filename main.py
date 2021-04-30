# DUISC IFY Computer Science with Extended Research (CSER)
# Summative 2 - Minimum Connector Problem

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_CSCPR

# ------------------------------- Imported Packages -------------------------------
# import os
# import time
# import csv
from util import config as cfg
from util import start as strt
from util.adj_list import open_csv_file, output_adj_list_table
# from util import alg_kruskal, alg_prim
# import numpy
# import pandas
# import matplotlib.pyplot as plt


# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = strt.menu()

        if option == 1: # import data from csv
            adjac_list = open_csv_file(cfg.read_file_path)
            cfg.time_animation(3, "CSV file imported successfully.")

        elif option == 2: # Calculate total sales for each employee
            print("option 2")
            output_adj = output_adj_list_table(adjac_list)
            print(output_adj)


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
