# adj_list.py
# open csv file and convert it to nested dict
# output adjacency list as a table
# save data to csv file

import csv
import pandas as pd

# function which will open the csv file and read in its values and return a dictionary containing each record as a dictionary
def open_csv_file(file_path):

	database = {} # create empty dict

	with open(file_path,"r") as csv_file: # open file in read mode
		csv_reader = csv.reader(csv_file)

		# add each line, as a dictionary, to the list
		for line in csv_reader:

			# to return a dict, with end node as key, and weight as value, without the start node
			def nested(line_pop):
				line_pop.pop(0)	# remove the first element of the list
				it = iter(line_pop)	# create an iterator, and initialize it to variable ‘it’
				nested_dict = dict(zip(it, it))	# use zip method, to zip keys and values together, then typecast it to dict type
				return nested_dict

			new_dict = nested(line.copy())	# call nested function to return a dict with keys and values

			start_node = line[0]	# set start_node to the first element of the list
			database[start_node] = new_dict	# store new_dict as value of the outer dict corresponding to the key (start node)

	return database	# return a nested dict

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

	adj_matrix = pd.DataFrame({key:pd.Series(value) for key, value in database.items()}).fillna(0)	# create dataframe using database
	adj_matrix = adj_matrix.astype(int)	# convert everything to integers

	return 	adj_list, adj_matrix	# return both adj_list, adj_matrix

# to save data to file in csv format
def save_csv(file_path, save_csv_list):

	fieldnames = save_csv_list[0].keys()	# get fieldnames from the key of the first element (dict) inside the list

	with open(file_path, 'w') as csv_file:	# open file in write mode
		writer = csv.DictWriter(csv_file, fieldnames)
		writer.writeheader()	# write fieldnames as first row
		writer.writerows(save_csv_list)	# iterate through the list and write
