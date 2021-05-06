# compare.py
#

import numpy as np

def create_completed_graph(nodes):

    new_complete_graph = {}
    nodes_list = [node for node in range(nodes)]

    for starting_node in nodes_list:
        # if starting_node in nodes_list:
        end_nodes_dict = {} # create a dict for all end_nodes
        end_nodes_list = nodes_list.copy()  # copy from the nodes_list
        end_nodes_list.pop(starting_node)   # remove the self value in the list

        for end_node in end_nodes_list: # iterate through each elements in the list
            weight = np.random.randint(1, 101)  # random generate an integer for weight
            if new_complete_graph == {}:    # check is this the first starting_node
                end_nodes_dict[end_node] = weight   # put key as end_node, and value as weight into dict
            else:
                if end_node in new_complete_graph: # iterate through each element in dict
                    if starting_node in new_complete_graph[end_node].keys():    # check is starting node exist in previous nodes
                        end_nodes_dict[end_node] = new_complete_graph[end_node][starting_node]  # add the same weight to the corresponding end_node
                else:
                    end_nodes_dict[end_node] = weight   # add the random weight to the end_node

        new_complete_graph[starting_node] = end_nodes_dict

    print(new_complete_graph)


create_completed_graph(5)
create_completed_graph(10)
# create_completed_graph(100)
# create_completed_graph(500)