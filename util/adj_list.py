# adj_list.py
# open csv file and convert it to nested dict
# convert nested dict to edge list

import csv
import util.config as cfg
import pandas as pd

# function which will open the csv file and read in its values and return a list containing each record as a dictionary
def open_csv_file(file_path):

	database = {} # create empty dict

	with open(file_path,"r") as csv_file: # open file in read mode
		csv_reader = csv.reader(csv_file)

		# add each line, as a dictionary, to the list
		for line in csv_reader:

			# to return a nested dict, with node as key, and weight as value, without the start node
			def nested(line_pop):
				line_pop.pop(0)	# remove the first element of the list
				it = iter(line_pop)	# create an iterator, and initialize it to variable ‘it’
				nested_dict = dict(zip(it, it))	# use zip method, to zip keys and values together, then typecast it to dict type
				return nested_dict

			new_dict = nested(line.copy())	# call nested function to return a dict with keys and values

			start_node = line[0]	#
			database[start_node] = new_dict	# store new_dict as value of the outer dict corresponding to the key (start node)

	return database

def output_adj_list_table(database):
    dict_df = pd.DataFrame({key:pd.Series(value) for key, value in database.items()}).fillna(0)
    return 	dict_df

	# for key, value in database.items():
	# 	end_node, weight = value
	# 	print("{:<8} {:<15} {:<10}".format(key, end_node, weight))



# to save data to file in csv format
def save_csv():


	pass