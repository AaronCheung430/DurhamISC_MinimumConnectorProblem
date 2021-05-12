# compare.py
# to create graph and compare it

import numpy as np
import util.config as cfg
from util.alg_kruskal import kruskal, kruskal_queue
from util.alg_prim import prim, prim_queue
import matplotlib.pyplot as plt
import random
import pandas as pd

compared_csv = []   # create list to store all info from algorithms ran

# create complete weighted graph with random weight and return nested dict
def create_completed_graph(nodes):

    new_complete_graph = {} # create a dict to store graph
    nodes_list = [node for node in range(nodes)]    # create list with all nodes

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

    return new_complete_graph   # return nested dict

# generate weighted graph when node is constant and edge is variable
def create_edges_graph(edges, nodes):

    new_edges_graph = {} # create a dict to store graph
    all_available_nodes = []    # create a list for all all_available_nodes
    weight_list = []    # create list to store weight
    nodes_list = [node for node in range(nodes)]   # create list with all nodes
    last_node = True    # set up variable

    for node in nodes_list: # iterate through each elements in the list
        new_edges_graph[node] = {}  # create empty dict

    for weight in range(edges): # create weight list
        weights = np.random.randint(1, cfg.maximum_weight)  # random generate an integer for weight
        weight_list.append(weights)  # append weight to weight_list

    for starting_node in nodes_list:    # iterate through each elements in the list
        end_nodes_list = nodes_list.copy()  # copy from the nodes_list
        end_nodes_list.remove(starting_node)    # remove the self value in the list
        all_available_nodes.append(end_nodes_list)  # append end_nodes_list to list, and it become nested list

    while weight_list:  # run following when weight_list is not empty

        for starting_node in nodes_list:    # iterate through each elements in the list
            if not weight_list: # check is weight_list empty
                break
            if not all_available_nodes[starting_node]:  # check is there any element in this index of the nested list
                continue

            weights = random.choice(weight_list) # random choose a element from weight_list
            weight_list.remove(weights)  # remove the corresponding element
            end_node = random.choice(all_available_nodes[starting_node])    # random choose a element from nested list

            if edges == nodes - 1 and last_node == True:    # to prevent all nodes are not connected
                last_node = False
                end_node = all_available_nodes[starting_node][-1]

            all_available_nodes[starting_node].remove(end_node) # remove the self value in the starting_node of all_available_nodes
            all_available_nodes[end_node].remove(starting_node) # remove the starting_node value in the end_node of all_available_nodes

            new_edges_graph[starting_node][end_node] = weights   # store weight to corresponding dict
            new_edges_graph[end_node][starting_node] = weights   # store weight to corresponding dict

    return new_edges_graph  # return nested dict

# run all algorithms and store it's data to a list
def find_comapre(temp_graph, Nodes, k_alg_no_list, k_alg_time_list, k_alg_no_queue_list, k_alg_time_queue_list, p_alg_no_list, p_alg_time_list, p_alg_no_queue_list, p_alg_time_queue_list):

    if Nodes == True:   # determine it is comparing nodes or edges
        key = "Number of Nodes"
    else:
        key = "Number of Edges"

    k_alg_queue_dict = kruskal_queue(temp_graph)    # run algorithm and store it's return value to a variable
    p_alg_queue_dict = prim_queue(temp_graph)
    k_alg_dict = kruskal(temp_graph)
    p_alg_dict = prim(temp_graph)

    k_alg_no_list.append(k_alg_dict[key])  # append spceific value to list for x,y
    k_alg_time_list.append(float(k_alg_dict["Computation Time"]))
    k_alg_no_queue_list.append(k_alg_queue_dict[key])
    k_alg_time_queue_list.append(float(k_alg_queue_dict["Computation Time"]))

    p_alg_no_list.append(p_alg_dict[key])  # append spceific value to list for x,y
    p_alg_time_list.append(float(p_alg_dict["Computation Time"]))
    p_alg_no_queue_list.append(p_alg_queue_dict[key])
    p_alg_time_queue_list.append(float(p_alg_queue_dict["Computation Time"]))

    compared_csv.append(k_alg_dict) # append the dict to the list for csv purpose
    compared_csv.append(p_alg_dict)
    compared_csv.append(k_alg_queue_dict)
    compared_csv.append(p_alg_queue_dict)

    # return all data
    return (k_alg_dict, k_alg_no_list, k_alg_time_list, k_alg_queue_dict, k_alg_no_queue_list, k_alg_time_queue_list,
    p_alg_dict, p_alg_no_list, p_alg_time_list, p_alg_queue_dict, p_alg_no_queue_list, p_alg_time_queue_list)

# compare algorithm in running time against number of edges and vertices
def compare():

    print("Please wait... \nGenerating weighted graphs (It may takes up to 1-2 minutes) \n")

    # compare running time against nodes
    def compare_nodes():

        no_nodes_list = [2**i for i in range(2,10)] # create a list with the number of nodes

        # set up variables
        k_alg_nodes_list, k_alg_time_list, k_alg_nodes_queue_list, k_alg_time_queue_list = [], [], [], []
        p_alg_nodes_list, p_alg_time_list, p_alg_nodes_queue_list, p_alg_time_queue_list = [], [], [], []

        for node in no_nodes_list:  # iterate through each elements in list

            temp_graph = create_completed_graph(node)   # generate complete weighted graph with the number of nodes

            # call function to run all algorithms
            (k_alg_dict, k_alg_nodes_list, k_alg_time_list, k_alg_queue_dict, k_alg_nodes_queue_list, k_alg_time_queue_list, p_alg_dict, p_alg_nodes_list,
            p_alg_time_list, p_alg_queue_dict, p_alg_nodes_queue_list, p_alg_time_queue_list) = find_comapre(temp_graph, True,
            k_alg_nodes_list, k_alg_time_list, k_alg_nodes_queue_list, k_alg_time_queue_list,
            p_alg_nodes_list, p_alg_time_list, p_alg_nodes_queue_list, p_alg_time_queue_list)

        # return all data
        return (k_alg_dict, k_alg_nodes_list, k_alg_time_list, k_alg_queue_dict, k_alg_nodes_queue_list, k_alg_time_queue_list
        , p_alg_dict, p_alg_nodes_list, p_alg_time_list, p_alg_queue_dict, p_alg_nodes_queue_list, p_alg_time_queue_list)

    # compare running time against edges
    def compare_edges(nodes = cfg.no_nodes):

        # set up variables
        k_alg_edges_list, k_alg_time_list, k_alg_edges_queue_list, k_alg_time_queue_list = [], [], [], []
        p_alg_edges_list, p_alg_time_list, p_alg_edges_queue_list, p_alg_time_queue_list = [], [], [], []

        min_edge = nodes    # set minimum number of edges
        max_egde = int(nodes*(nodes-1)/2)+1   # set maximum number of edges +1

        for edge in range(min_edge, max_egde, 50):  # iterate over a sequence incrementally

            temp_edge_graph = create_edges_graph(edge, nodes)   # generate weighted graph with the number of edges

            # call function to run all algorithms
            (k_alg_dict, k_alg_edges_list, k_alg_time_list, k_alg_queue_dict, k_alg_edges_queue_list, k_alg_time_queue_list, p_alg_dict, p_alg_edges_list,
            p_alg_time_list, p_alg_queue_dict, p_alg_edges_queue_list, p_alg_time_queue_list) = find_comapre(temp_edge_graph, False,
            k_alg_edges_list, k_alg_time_list, k_alg_edges_queue_list, k_alg_time_queue_list,
            p_alg_edges_list, p_alg_time_list, p_alg_edges_queue_list, p_alg_time_queue_list)

        # return all data
        return (k_alg_dict, k_alg_edges_list, k_alg_time_list, k_alg_queue_dict, k_alg_edges_queue_list, k_alg_time_queue_list,
        p_alg_dict, p_alg_edges_list, p_alg_time_list, p_alg_queue_dict, p_alg_edges_queue_list, p_alg_time_queue_list)

    # find moving average
    def moving_average(time_list, window_size = cfg.window_size):
        moving_averages_list = pd.Series(time_list).rolling(window_size).mean().tolist()
        return moving_averages_list

    # set variables with returned values
    (k_alg_dict, k_alg_nodes_list, k_alg_time_list, k_alg_queue_dict, k_alg_nodes_queue_list, k_alg_time_queue_list, p_alg_dict,
    p_alg_nodes_list, p_alg_time_list, p_alg_queue_dict, p_alg_nodes_queue_list, p_alg_time_queue_list) = compare_nodes()

    plt.figure(figsize=(9, 6))  # set figure size
    plt.rcParams.update({'font.size': 9})   # set title size

    plt.subplot(2, 1, 1)    # create subgraph
    plt.plot(p_alg_nodes_list, p_alg_time_list, label=p_alg_dict["Algorithm"])  # plot graphs using list for x,y and corresponding label
    plt.plot(k_alg_nodes_list, k_alg_time_list, label=k_alg_dict["Algorithm"])
    plt.plot(p_alg_nodes_queue_list, p_alg_time_queue_list, label=p_alg_queue_dict["Algorithm"])
    plt.plot(k_alg_nodes_queue_list, k_alg_time_queue_list, label=k_alg_queue_dict["Algorithm"])
    plt.xlabel("Number of Nodes")   # set the first subgraph attributes
    plt.ylabel("Computation Time (s)")
    plt.title('Comparing algorithm computation time against the number of nodes')
    plt.grid()
    plt.legend(loc='upper left', fontsize='small')

    print("Found MST using both algorithms with complete weighted graph. 1/2")

    # set variables with returned values
    (k_alg_dict, k_alg_edges_list, k_alg_time_list, k_alg_queue_dict, k_alg_edges_queue_list, k_alg_time_queue_list, p_alg_dict,
    p_alg_edges_list, p_alg_time_list, p_alg_queue_dict, p_alg_edges_queue_list, p_alg_time_queue_list) = compare_edges()

    plt.subplot(2, 1, 2)    # create subgraph
    plt.plot(p_alg_edges_list, moving_average(p_alg_time_list), label=p_alg_dict["Algorithm"] + " Moving Average")  # plot graphs using list for x,y and corresponding label
    plt.plot(k_alg_edges_list, moving_average(k_alg_time_list), label=k_alg_dict["Algorithm"] + " Moving Average")
    plt.plot(p_alg_edges_queue_list, moving_average(p_alg_time_queue_list), label=p_alg_queue_dict["Algorithm"] + " Moving Average")
    plt.plot(k_alg_edges_queue_list, moving_average(k_alg_time_queue_list), label=k_alg_queue_dict["Algorithm"] + " Moving Average")

    plt.xlabel("Number of Edges")   # set the second subgraph attributes
    plt.ylabel("Computation Time (s)")
    plt.title(f'Comparing algorithm computation time against the number of edges with {cfg.no_nodes} nodes weighted graph')
    plt.grid()
    plt.legend(loc='upper left', fontsize='small')

    print(f"Found MST using both algorithms with a {p_alg_dict['Number of Nodes']} nodes weighted graph. 2/2")

    # show graph and save figure
    plt.tight_layout()
    plt.savefig('data/comparison_algorithms.png')
    plt.show()
    plt.ion()

    input("\nEnter to return to menu...")   # pause the program to show graph
    plt.close('all')

    return compared_csv # return a list of dicts
