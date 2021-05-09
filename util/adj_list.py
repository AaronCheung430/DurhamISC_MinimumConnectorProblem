# adj_list.py
# open csv file and convert it to nested dict
# convert nested dict to edge list

import csv
# import util.config as cfg
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

# to output both adjacency list and adjacency matrix as a table
def output_adj_list_table(database):

	graph = {}	# set up dict
	# change database to graph (dict list)
	for key in database.keys():	# get the key of outer dict
		end_nodes_list = []	# set up list
		for end_node, weight in database[key].items():	# get both key and value in the inner dict of the corresponding key of the outer dict
			end_nodes_list.append(end_node)	# append end_node to the list
			end_nodes_list.append(weight)	# append weight to the list

		graph[key] = end_nodes_list	# store list as value of the outer dict corresponding to the key

	adj_list = pd.DataFrame({key:pd.Series(value) for key, value in graph.items()}).fillna("")	# create dataframe using graph
	adj_list = adj_list.transpose()	# transpose index and columns
	adj_list = adj_list.to_string(header=False)	# show dataframe without index

	print(adj_list)

	adj_matrix = pd.DataFrame({key:pd.Series(value) for key, value in database.items()}).fillna(0)	# create dataframe using database
	adj_matrix = adj_matrix.astype(int)	# convert everything to integers

	print(adj_matrix)

	return 	adj_matrix, adj_list	# return both adj_matrix, adj_list

# to save data to file in csv format
def save_csv(file_path):

	fieldnames = ["Algorithm", "Numbers of Nodes", "Numbers of Edges", "Computation Time", "Path Found", "Minimal Weight"]

	with open(file_path, 'w') as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		writer.writeheader()

		# writer.writerow({})


# save_csv("../data/test_final.csv")




# database = {
#             "A": {"B": 7, "C": 9},
#             "B": {"A": 7, "C": 6, "D": 19, "F": 14},
#             "C": {"A": 9, "B": 6, "D": 11, "E": 14},
#             "D": {"B": 19, "C": 11, "E": 10, "F": 13, "G": 27, "I": 23},
#             "E": {"C": 14, "D": 10, "I": 15},
#             "F": {"B": 14, "D": 13, "G": 25, "H": 16},
#             "G": {"D": 27, "F": 25, "H": 20, "I": 28},
#             "H": {"F": 16, "G": 20, "I": 17},
#             "I": {"D": 23, "E": 15, "G": 28, "H": 17}
#         }
# output_adj_list_table(database)