# compare.py
#

import numpy as np
import config as cfg
from alg_kruskal import kruskal

maximum_weight = 1001

def create_completed_graph(nodes):

    new_complete_graph = {}
    nodes_list = [node for node in range(nodes)]

    for starting_node in nodes_list:

        end_nodes_dict = {} # create a dict for all end_nodes
        end_nodes_list = nodes_list.copy()  # copy from the nodes_list
        end_nodes_list.pop(starting_node)   # remove the self value in the list

        for end_node in end_nodes_list: # iterate through each elements in the list
            weight = np.random.randint(1, maximum_weight)  # random generate an integer for weight
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
    return new_complete_graph

# cfg.time_animation(3)
# create_completed_graph(5)
k_mst, k_weight, k_time = kruskal(create_completed_graph(5))
print("Here are the results using kruskal's Algorithm:")
print("The MST is", k_mst)
print("Weight of MST is", k_weight)
print("Computation time is", k_time)
create_completed_graph(10)
# create_completed_graph(100)
# create_completed_graph(500)
# create_completed_graph(1000)
# print("hi")

def compare_nodes():


    k_mst, k_weight, k_time = alg_kruskal.kruskal(create_completed_graph(10))

    pass