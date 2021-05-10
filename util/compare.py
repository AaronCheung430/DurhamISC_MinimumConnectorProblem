# compare.py
# to create networks and compare it

import numpy as np
# import config as cfg
import util.config as cfg
from util.alg_kruskal import kruskal, kruskal_queue
from util.alg_prim import prim, prim_queue
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pylab
import random

compared_csv = []

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

def create_edges_graph(edges, nodes):

    new_edges_graph = {} # create a dict to store graph
    all_available_nodes = []    # create a list for all all_available_nodes
    weight_list = []    # create list to store weight
    nodes_list = [node for node in range(nodes)]   # create list with all nodes
    last_node = True    # set up variable

    for node in nodes_list: # iterate through each elements in the list
        new_edges_graph[node] = {}  # create empty dict

    for weight in range(edges): # create weight list
        weight = np.random.randint(1, 101)  # random generate an integer for weight
        weight_list.append(weight)  # append weight to weight_list

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

            weight = random.choice(weight_list) # random choose a element from weight_list
            weight_list.remove(weight)  # remove the corresponding element
            end_node = random.choice(all_available_nodes[starting_node])    # random choose a element from nested list

            if edges == nodes - 1 and last_node == True:    # to prevent all nodes are not connected
                last_node = False
                end_node = all_available_nodes[starting_node][-1]

            all_available_nodes[starting_node].remove(end_node) # remove the self value in the starting_node of all_available_nodes
            all_available_nodes[end_node].remove(starting_node) # remove the starting_node value in the end_node of all_available_nodes

            new_edges_graph[starting_node][end_node] = weight   # store weight to corresponding dict
            new_edges_graph[end_node][starting_node] = weight   # store weight to corresponding dict

    return new_edges_graph  # return nested dict

def find_comapre(temp_graph, k_alg_no_list, k_alg_time_list, k_alg_no_queue_list, k_alg_time_queue_list, p_alg_no_list, p_alg_time_list, p_alg_no_queue_list, p_alg_time_queue_list):

    k_alg_queue_dict = kruskal_queue(temp_graph)
    p_alg_queue_dict = prim_queue(temp_graph)
    k_alg_dict = kruskal(temp_graph)
    p_alg_dict = prim(temp_graph)

    k_alg_no_list.append(k_alg_dict["Number of Nodes"])  # append spceific value to list for x,y
    k_alg_time_list.append(float(k_alg_dict["Computation Time"]))
    k_alg_no_queue_list.append(k_alg_queue_dict["Number of Nodes"])
    k_alg_time_queue_list.append(float(k_alg_queue_dict["Computation Time"]))

    p_alg_no_list.append(p_alg_dict["Number of Nodes"])  # append spceific value to list for x,y
    p_alg_time_list.append(float(p_alg_dict["Computation Time"]))
    p_alg_no_queue_list.append(p_alg_queue_dict["Number of Nodes"])
    p_alg_time_queue_list.append(float(p_alg_queue_dict["Computation Time"]))

    compared_csv.append(k_alg_dict) # append the dict to the list for csv purpose
    compared_csv.append(p_alg_dict)
    compared_csv.append(k_alg_queue_dict)
    compared_csv.append(p_alg_queue_dict)

    return (k_alg_dict, k_alg_no_list, k_alg_time_list, k_alg_queue_dict, k_alg_no_queue_list, k_alg_time_queue_list,
    p_alg_dict, p_alg_no_list, p_alg_time_list, p_alg_queue_dict, p_alg_no_queue_list, p_alg_time_queue_list)


# compare algorithm in running time against number of edges and vertices
def compare():

    print("Please wait... \nGenerating weighted graphs (It may takes up to 1-2 minutes) \n")

    # compared_csv = []

    def compare_nodes():

        no_nodes_list = [2**i for i in range(2,10)]

        k_alg_nodes_list, k_alg_time_list, k_alg_nodes_queue_list, k_alg_time_queue_list = [], [], [], []
        p_alg_nodes_list, p_alg_time_list, p_alg_nodes_queue_list, p_alg_time_queue_list = [], [], [], []

        for node in no_nodes_list:

            temp_graph = create_completed_graph(node)

            (k_alg_dict, k_alg_nodes_list, k_alg_time_list, k_alg_queue_dict, k_alg_nodes_queue_list, k_alg_time_queue_list, p_alg_dict, p_alg_nodes_list,
            p_alg_time_list, p_alg_queue_dict, p_alg_nodes_queue_list, p_alg_time_queue_list) = find_comapre(temp_graph,
            k_alg_nodes_list, k_alg_time_list, k_alg_nodes_queue_list, k_alg_time_queue_list,
            p_alg_nodes_list, p_alg_time_list, p_alg_nodes_queue_list, p_alg_time_queue_list)


        return (k_alg_dict, k_alg_nodes_list, k_alg_time_list, k_alg_queue_dict, k_alg_nodes_queue_list, k_alg_time_queue_list
        , p_alg_dict, p_alg_nodes_list, p_alg_time_list, p_alg_queue_dict, p_alg_nodes_queue_list, p_alg_time_queue_list)

    def compare_edges(nodes = cfg.no_nodes):

        k_alg_edges_list, k_alg_time_list, k_alg_edges_queue_list, k_alg_time_queue_list = [], [], [], []
        p_alg_edges_list, p_alg_time_list, p_alg_edges_queue_list, p_alg_time_queue_list = [], [], [], []

        min_edge = nodes-1
        max_egde = int(nodes*(nodes-1)/2)

        for edge in range(min_edge, max_egde, 50):

            temp_edge_graph = create_edges_graph(edge, nodes)

            (k_alg_dict, k_alg_edges_list, k_alg_time_list, k_alg_queue_dict, k_alg_edges_queue_list, k_alg_time_queue_list, p_alg_dict, p_alg_edges_list,
            p_alg_time_list, p_alg_queue_dict, p_alg_edges_queue_list, p_alg_time_queue_list) = find_comapre(temp_edge_graph,
            k_alg_edges_list, k_alg_time_list, k_alg_edges_queue_list, k_alg_time_queue_list,
            p_alg_edges_list, p_alg_time_list, p_alg_edges_queue_list, p_alg_time_queue_list)

            # # if queue is True:
            # #     k_alg_dict = kruskal_queue(temp_edge_graph)
            # #     p_alg_dict = prim_queue(temp_edge_graph)
            # # else:
            # #     k_alg_dict = kruskal(temp_edge_graph)
            # #     p_alg_dict = prim(temp_edge_graph)

            # k_alg_edges_list.append(k_alg_dict["Number of Edges"])  # append spceific value to list for x,y
            # k_alg_time_list.append(float(k_alg_dict["Computation Time"]))

            # p_alg_edges_list.append(p_alg_dict["Number of Edges"])  # append spceific value to list for x,y
            # p_alg_time_list.append(float(p_alg_dict["Computation Time"]))

            # compared_csv.append(k_alg_dict) # append the dict to the list for csv purpose
            # compared_csv.append(p_alg_dict)

        return (k_alg_dict, k_alg_edges_list, k_alg_time_list, k_alg_queue_dict, k_alg_edges_queue_list, k_alg_time_queue_list,
        p_alg_dict, p_alg_edges_list, p_alg_time_list, p_alg_queue_dict, p_alg_edges_queue_list, p_alg_time_queue_list)


    (k_alg_dict, k_alg_nodes_list, k_alg_time_list, k_alg_queue_dict, k_alg_nodes_queue_list, k_alg_time_queue_list, p_alg_dict,
    p_alg_nodes_list, p_alg_time_list, p_alg_queue_dict, p_alg_nodes_queue_list, p_alg_time_queue_list) = compare_nodes()

    pylab.rcParams["axes.titlesize"] = 8

    plt.subplot(1, 2, 1)    # create subgraph
    plt.plot(p_alg_nodes_list, p_alg_time_list, label=p_alg_dict["Algorithm"])
    plt.plot(k_alg_nodes_list, k_alg_time_list, label=k_alg_dict["Algorithm"])

    plt.plot(p_alg_nodes_queue_list, p_alg_time_queue_list, label=p_alg_queue_dict["Algorithm"])
    plt.plot(k_alg_nodes_queue_list, k_alg_time_queue_list, label=k_alg_queue_dict["Algorithm"])

    plt.xlabel("Number of Nodes")
    plt.ylabel("Computation Time (s)")
    plt.title('Comparing algorithm (without queue) computation time against the number of nodes')
    plt.grid()
    plt.legend(loc='upper left', fontsize='small')

    print("Found MST using both algorithms (without queue) with complete weighted graph. 1/2")

    # k_alg_dict, k_alg_nodes_list, k_alg_time_list, p_alg_dict, p_alg_nodes_list, p_alg_time_list = compare_nodes(True)

    # plt.subplot(2, 2, 2)    # create subgraph
    # plt.plot(p_alg_nodes_list, p_alg_time_list, label=p_alg_dict["Algorithm"])
    # plt.plot(k_alg_nodes_list, k_alg_time_list, label=k_alg_dict["Algorithm"])
    # plt.xlabel("Number of Nodes")
    # plt.ylabel("Computation Time (s)")
    # plt.title('Comparing algorithm (with queue) computation time against the number of nodes')
    # plt.grid()
    # plt.legend(loc='upper left', fontsize='small')

    # print("Found MST using both algorithms (with queue) with complete weighted graph. 2/4")


    (k_alg_dict, k_alg_edges_list, k_alg_time_list, k_alg_queue_dict, k_alg_edges_queue_list, k_alg_time_queue_list, p_alg_dict,
    p_alg_edges_list, p_alg_time_list, p_alg_queue_dict, p_alg_edges_queue_list, p_alg_time_queue_list) = compare_edges()

    plt.subplot(1, 2, 2)    # create subgraph
    plt.plot(p_alg_edges_list, p_alg_time_list, label=p_alg_dict["Algorithm"])
    plt.plot(k_alg_edges_list, k_alg_time_list, label=k_alg_dict["Algorithm"])

    plt.plot(p_alg_edges_queue_list, p_alg_time_queue_list, label=p_alg_queue_dict["Algorithm"])
    plt.plot(k_alg_edges_queue_list, k_alg_time_queue_list, label=k_alg_queue_dict["Algorithm"])

    plt.xlabel("Number of Edges")
    plt.ylabel("Computation Time (s)")
    plt.title('Comparing algorithm (without queue) computation time against the number of edges')
    plt.grid()
    plt.legend(loc='upper left', fontsize='small')

    print(f"Found MST using both algorithms (without queue) with a {p_alg_dict['Number of Nodes']} nodes weighted graph. 2/2")

    # k_alg_dict, k_alg_edges_list, k_alg_time_list, p_alg_dict, p_alg_edges_list, p_alg_time_list = compare_edges(True)

    # plt.subplot(2, 2, 4)    # create subgraph
    # plt.plot(p_alg_edges_list, p_alg_time_list, label=p_alg_dict["Algorithm"])
    # plt.plot(k_alg_edges_list, k_alg_time_list, label=k_alg_dict["Algorithm"])
    # plt.xlabel("Number of Edges")
    # plt.ylabel("Computation Time (s)")
    # plt.title('Comparing algorithm (with queue) computation time against the number of edges')
    # plt.grid()
    # plt.legend(loc='upper left', fontsize='small')

    # print(f"Found MST using both algorithms (with queue) with a {p_alg_dict['Number of Nodes']} nodes weighted graph. 4/4")



    plt.savefig('data/comparison_algorithms.png')
    plt.tight_layout()
    plt.show()
    plt.ion()

    input("\nEnter to return to menu...")   # pause the program to show graph
    plt.close('all')

    return compared_csv


# print(create_edges_graph(99))