# compare.py
# to create networks and compare it

import numpy as np
# import config as cfg
import util.config as cfg
from util.alg_kruskal import kruskal, kruskal_queue
from util.alg_prim import prim, prim_queue
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# create complete graph with random weight and return nested dict
def create_completed_graph(nodes):

    new_complete_graph = {}
    nodes_list = [node for node in range(nodes)]

    for starting_node in nodes_list:

        end_nodes_dict = {} # create a dict for all end_nodes
        end_nodes_list = nodes_list.copy()  # copy from the nodes_list
        end_nodes_list.pop(starting_node)   # remove the self value in the list

        for end_node in end_nodes_list: # iterate through each elements in the list
            weight = np.random.randint(1, cfg.maximum_weight)  # random generate an integer for weight
            if end_node in new_complete_graph: # check is edge exist
                if starting_node in new_complete_graph[end_node].keys():    # check is starting node exist in previous nodes
                    end_nodes_dict[end_node] = new_complete_graph[end_node][starting_node]  # add the same weight to the corresponding end_node
            else:
                end_nodes_dict[end_node] = weight   # add the random weight to the end_node

        new_complete_graph[starting_node] = end_nodes_dict

    return new_complete_graph

#
def compare():

    print("Please wait... \nGenerating weighted graphs")

    no_nodes = [2**i for i in range(2,10)]
    compared_csv = []

    def compare_nodes(queue):

        k_alg_nodes_list, k_alg_time_list = [], []
        p_alg_nodes_list, p_alg_time_list = [], []

        for node in no_nodes:

            temp_graph = create_completed_graph(node)
            temp_k_mean = []
            temp_p_mean = []

            if queue is True:
                k_alg_dict = kruskal_queue(temp_graph)
                p_alg_dict = prim_queue(temp_graph)
            else:
                k_alg_dict = kruskal(temp_graph)
                p_alg_dict = prim(temp_graph)

            k_alg_nodes_list.append(k_alg_dict["Number of Nodes"])  # append spceific value to list for x,y
            k_alg_time_list.append(float(k_alg_dict["Computation Time"]))

            p_alg_nodes_list.append(p_alg_dict["Number of Nodes"])  # append spceific value to list for x,y
            p_alg_time_list.append(float(p_alg_dict["Computation Time"]))

            compared_csv.append(k_alg_dict) # append the dict to the list for csv purpose
            compared_csv.append(p_alg_dict)

        return k_alg_dict, k_alg_nodes_list, k_alg_time_list, p_alg_dict, p_alg_nodes_list, p_alg_time_list

    k_alg_dict, k_alg_nodes_list, k_alg_time_list, p_alg_dict, p_alg_nodes_list, p_alg_time_list = compare_nodes(False)

    plt.subplot(1, 2, 1)    # create subgraph
    plt.plot(p_alg_nodes_list, p_alg_time_list, label=p_alg_dict["Algorithm"])
    plt.plot(k_alg_nodes_list, k_alg_time_list, label=k_alg_dict["Algorithm"])
    plt.xlabel("Number of Nodes")
    plt.ylabel("Computation Time (s)")
    plt.title('Comparing algorithm (without queue) computation time against the number of vertices')
    plt.grid()
    plt.legend(loc='upper left')

    print("Found MST using both algorithms (without queue) with complete weighted graph 1/2")
    k_alg_dict, k_alg_nodes_list, k_alg_time_list, p_alg_dict, p_alg_nodes_list, p_alg_time_list = compare_nodes(True)

    plt.subplot(1, 2, 2)    # create subgraph
    plt.plot(p_alg_nodes_list, p_alg_time_list, label=p_alg_dict["Algorithm"])
    plt.plot(k_alg_nodes_list, k_alg_time_list, label=k_alg_dict["Algorithm"])
    plt.xlabel("Number of Nodes")
    plt.ylabel("Computation Time (s)")
    plt.title('Comparing algorithm (with queue) computation time against the number of vertices')
    plt.grid()
    plt.legend(loc='upper left')

    print("Found MST using both algorithms (with queue) with complete weighted graph 2/2")












    plt.tight_layout()
    plt.show()
    plt.ion()

    input("\nEnter to return to menu...")   # pause the program to show graph
    plt.close('all')

    return compared_csv


# compare()